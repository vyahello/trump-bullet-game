#!/bin/bash

declare -a RESULT

TESTS_DIR='tests/'
RED_OUT='\033[0;31m'
GREEN_OUT='\033[0;32m'


function store_failures {
    RESULT+=("$1")
}


function remove_pycache {
    local trash=".pytest_cache"
    echo "Removing __pycache__ directories if present..."
    ( find . -d -name "__pycache__" | xargs rm -r ) || echo -e "No __pycache__"
}


function clear_trash {
    local trash='.pytest_cache'
    echo "Removing pytest trash if present..."
    [[ -d "$trash" ]] && rm -rf ${trash} && echo "Environment is clean!"
}


function install_dependencies {
   echo "Installing python packages..." && ( pip install -r requirements.txt )
}


function run_unittests {
    echo "Running unittests..." && ( pytest ${TESTS_DIR} )
}


function run_code_analysis {
    echo "Running code analysis..."
    remove_pycache
    install_dependencies || store_failures "Python packages installation is failed!"
    run_unittests || store_failures "Unittests are failed!"

    if [[ ${#RESULT[@]} -ne 0 ]]; then
        echo -e "${RED_OUT}There are some errors identified while analysing the code.${RED_OUT}"
        for item in "${RESULT[@]}"; do
            echo "- ${item}"
        done
        clear_trash
        exit 1
    fi
    clear_trash
    echo -e "${GREEN_OUT}Code analysis is passed.${GREEN_OUT}"
}

run_code_analysis
