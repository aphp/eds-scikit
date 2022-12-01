#!/bin/bash -x

python -m pytest --pyargs tests -m "" --cov=eds_scikit
