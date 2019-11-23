#!/bin/bash

declare -a RESULT

TESTS_DIR='tests/'
RED_OUT='\033[0;31m'
GREEN_OUT='\033[0;32m'


function store-failures {
    RESULT+=("$1")
}


function remove-pycache {
    local trash=".pytest_cache"
    echo "Removing __pycache__ directories if present..."
    ( find . -d -name "__pycache__" | xargs rm -r ) || echo -e "No __pycache__"
}


function clear-trash {
    local trash='.pytest_cache'
    echo "Removing pytest trash if present..."
    [[ -d "$trash" ]] && rm -rf ${trash} && echo "Environment is clean!"
}


function install-dependencies {
   echo "Installing python packages..." && ( pip install --upgrade pip )  && ( pip install -r requirements-dev.txt )
}


function run-unittests {
    echo "Running unittests..." && ( pytest ${TESTS_DIR} )
}


function run-black-analysis {
    echo "Running black analysis ..." && ( black --check "${PROJECT_FILES}" )
}


function run-code-analysis {
    echo "Running code analysis..."
    remove-pycache
    install-dependencies || store-failures "Python packages installation is failed!"
    run-unittests || store-failures "Unittests are failed!"
    run-black-analysis || store-failures "black analysis is failed!"

    if [[ ${#RESULT[@]} -ne 0 ]]; then
        echo -e "${RED_OUT}There are some errors identified while analysing the code.${RED_OUT}"
        for item in "${RESULT[@]}"; do
            echo "- ${item}"
        done
        clear-trash
        exit 1
    fi
    clear-trash
    echo -e "${GREEN_OUT}Code analysis is passed.${GREEN_OUT}"
}

run-code-analysis
