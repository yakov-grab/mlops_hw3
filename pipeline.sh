#!/bin/bash

# Запуск скриптов по порядку
python3 src/data_creation.py
python3 src/model_preprocessing.py
python3 src/model_preparation.py
python3 src/model_testing.py
