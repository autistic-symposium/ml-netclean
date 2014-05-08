#!/bin/bash


cd ./src/1-cleasing_for_display/
python parse_vectors.py
cd ../1-cleasing_for_processing/
python parse_vectors.py
cd ../3-all_together/
python parse_vectors.py
cd ../..
