#!/bin/bash -x

pip install -U "pip<23"
coverage run -m pytest
