#!/bin/env bash

source <(../etc/set-env-linux.sh)

./RunCmdServer/main.py server "$@"

exit
