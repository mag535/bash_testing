#!/bin/bash
#$ chmod u+x pyscript.sh
#$ -j y

### trying to run do_things.py
SRCDIR="C:/Users/milkg/OneDrive/Desktop/Local_repo/bash_testing/Python_Stuff/-.-"

python.exe ${SRCDIR/-.-/do_things.py} > ../py_scripting/do_output.txt

