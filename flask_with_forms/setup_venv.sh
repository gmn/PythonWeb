#!/bin/bash

SLEEP='sleep 1.5'
READ_ONLY=
if [ "x$@" != "x" ]; then
    READ_ONLY="1"
    VIRTUAL_ENV=xyz
fi

EE() {
    echo "$@"
    if [ "x$READ_ONLY" != "x1" ]; then
        echo
        $SLEEP
        $@
        echo
    fi
}

if [ ! -e venv ]; then
    EE python3 -m venv venv
fi

if [ "x$VIRTUAL_ENV" == "x" ]; then
    EE . venv/bin/activate
fi

if [ "x$VIRTUAL_ENV" == "x" ]; then
    echo not in virtual env
else
    EE pip install --upgrade pip
    #EE pip install config
    EE pip install flask
    EE pip install flask_wtf
    EE pip install flask-sqlalchemy
    EE python3 ./create_db.py

    echo
    echo 'Run this to start venv: "source venv/bin/activate"'
    echo
    echo 'Then from inside venv, run: ./run.sh to start the server'
    echo
    #EE ./run.sh
    #EE cat run.sh
fi
