#!/bin/bash

if [ type python >/dev/null 2>&1 && if type pip >/dev/null 2>&1 ]
    then 
    python -m venv venv;
    source ./venv/bin/activate;
    pip install -r requirements.txt;
fi;