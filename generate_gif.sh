#!/bin/bash

TMP_DIR=tmp
OUT_GIF=output/output.gif
echo -n 'Generating GIF...'
# Resize images.
(
    cd $TMP_DIR
    for img in `ls *.png`
    do
	    convert $img -resize 40% "tmp.png"
	    mv "tmp.png" $img
    done
)

convert -delay 10 -loop 0 -layers optimize $( ls $TMP_DIR/*.png | sort -V ) $OUT_GIF
echo -e "\t$OUT_GIF"