#!/bin/bash
NODEP=`pgrep node`
for id in $NODEP; do
    kill $id
done
