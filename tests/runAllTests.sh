#!/bin/bash

echo "Initialize virtuel Environment" 
python3 -m venv venv

echo "Install dependencies"
./venv/bin/pip3 install -e ../Backend/
./venv/bin/pip3 install -r requirements.txt

echo "run tests"
venv/bin/python3 validatortest.py
venv/bin/python3 basepingertest.py
venv/bin/python3 geneartclienttest.py
venv/bin/python3 geneartpingertest.py
