#!/bin/bash -x

pip install -u "pip<23"
python -m pytest --pyargs tests -m "" --cov=eds_scikit
