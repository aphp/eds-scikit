#!/bin/bash -e

pip install -U "pip<23"
pip install --progress-bar off --upgrade ".[dev, doc]"
