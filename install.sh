#!/bin/bash

if [[ -n python && -n pip ]]
then 
    python -m venv venv;
    source ./venv/bin/activate;
    pip install -r requirements.txt;
else 
    echo "Python and/or pip not found!";
fi