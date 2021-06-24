#!/bin/bash

cd tiffs
for f in *.tif
do
  echo ${f%.*}
  convert $f ../jpgs/${f%.*}.jpg
done

cd ..