#!/bin/bash -x

pip install -U "pip<23"
python -m pytest --pyargs tests -m "" --cov=eds_scikit
