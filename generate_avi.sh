#!/bin/bash
TMP_DIR=tmp
OUT_VID=output/solution.avi

echo -n 'Generating AVI...'
avconv -r 10 -i $TMP_DIR/%5d.png $OUT_VID 2> /dev/null
echo -e "\t$OUT_VID"