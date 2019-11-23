#!/bin/bash


clear-trash(){
    local trash='.pytest_cache'
    [[ -d "$trash" ]] && echo "removing ${trash} testing trash" && rm -rf ${trash} && echo "environment is cleared"
}


function run-unittests {
    echo "Running unittests ..." && pytest
}


function start-tests-coverage {
    run-unittests
    clear-trash
}

start-tests-coverage
