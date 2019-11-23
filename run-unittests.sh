#!/bin/bash

PROJECT_FILES="./"


clear-trash(){
    local trash='.pytest_cache'
    [[ -d "$trash" ]] && echo "removing ${trash} testing trash" && rm -rf ${trash} && echo "environment is cleared"
}


function run-unittests {
    echo "Running unittests ..." && pytest
}


function run-black-analysis {
    echo "Running black analysis ..." && ( black --check "${PROJECT_FILES}" )
}


function start-tests-coverage {
    run-unittests
    run-black-analysis
    clear-trash
}

start-tests-coverage
