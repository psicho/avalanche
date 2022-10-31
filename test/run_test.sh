#!/usr/bin/env bash

#### Install ####
rm -rf build
mkdir build

python3 -m virtualenv build/env

build/env/bin/pip install --upgrade pip
build/env/bin/pip install -r test_requirements.txt

#### Test & Coverage ####
echo "Running coverage tests ..."
cd ../src/tests
PYTHONPATH=/build/src ../../test/build/env/bin/python -m coverage run --source ../service -m pytest -v .
TEST_RESULT=$?
echo "Test result: $TEST_RESULT"

echo "Coverage results:"
PYTHONPATH=/ ../../test/build/env/bin/python -m coverage report
PYTHONPATH=/ ../../test/build/env/bin/python -m coverage html
tar caf coverage.tar.gz htmlcov

#### Exit ####
exit $((TEST_RESULT))
