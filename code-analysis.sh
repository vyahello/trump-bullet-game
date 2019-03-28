#!/bin/bash

declare -a RESULT


function store_failures() {
    RESULT+=("$1")
}


function install_dependencies () {
    pip install -r requirements.txt
}


function run_code_analysis () {
    echo "Running code analysis..."
    echo "Remove __pycache__ directories if present"
    ( find . -d -name "__pycache__" | xargs rm -r ) || echo "No __pycache__"
    echo "Installing python packages..." && install_dependencies || store_failures "Python packages installation is failed!"
    echo "Running unittests..." && ./run-unittests.sh || store_failures "Unittests are failed!"

    if [[ ${#RESULT[@]} -ne 0 ]]; then
        echo "There are some errors identified while analysing the code."
        for item in "${RESULT[@]}"; do
          echo "- ${item}"
        done
        exit 1
    fi
    echo "Code analysis is passed."
}


run_code_analysis
