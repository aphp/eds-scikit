#!/bin/bash
# will generate files:
#  - report.xml
#  - report.html

# pyclean removes __pycache__ files
# that prevent python imports when in docker
# because the path of python files changed
pyclean eds_scikit/ tests/

python -m pytest tests/ \
    --cov=eds_scikit --junitxml=report.xml --html=report.html --self-contained-html \
    -m "" \
