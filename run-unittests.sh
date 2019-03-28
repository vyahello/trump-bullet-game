#!/bin/bash

TESTS_DIR='tests/'


clear_trash(){
    local trash='.pytest_cache'
    [[ -d "$trash" ]] && echo "removing ${trash} testing trash" && rm -rf ${trash} && echo "environment is cleared"
}


function run_unittests {
    pytest ${TESTS_DIR}
}


function start_test_coverage {
    run_unittests
    clear_trash
}

start_test_coverage
