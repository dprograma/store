#!/bin/bash

# Run black
echo "Running black..."
black inventory
black tests

# Run isort
echo "Running isort..."
isort inventory
isort tests

# Run django migrations check to ensure that there are no migrations left to create
echo "Running makemigrations..."
python manage.py makemigrations

echo "Running migrate..."
python manage.py migrate

# run python static validation
echo "Running pylint"
pylint inventory

# Run mypy
echo "Running mypy..."
mypy inventory

# Run pytest
echo "Running pytest..."
pytest tests
