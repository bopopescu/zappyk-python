#!/bin/env bash

PRG_NAME='GoogleSheets'
PRG_VERS='0.0.1b1'
PRG_VERS='0.0.2b1'
HOSTARCH='32bit_ELF'
HOSTARCH='64bit_ELF'
HOSTARCH="$(getconf LONG_BIT)bit_ELF"
PYTHON_V="3.4.2"
PYTHON_V=($(python3 -V 2>&1))

DIR_NAME=$(dirname "$0")
DIR_BASE="$PRG_NAME-$PRG_VERS"
DIR_ARCH="exe.linux-$HOSTARCH-python-${PYTHON_V[1]}"

PRG_BASE="$DIR_NAME/$DIR_BASE"
PRG_EXEC="$DIR_ARCH/$PRG_NAME"
PROGRAMM="$PRG_BASE/$PRG_EXEC"

[ ! -e "$PROGRAMM" ] && echo "Programma '$PRG_NAME' non installato..." && exit 1
[ ! -x "$PROGRAMM" ] && echo "Programma '$PRG_NAME' non eseguibile..." && exit 1

cd "$PRG_BASE" && $PRG_EXEC "$@"

exit
