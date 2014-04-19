#!/bin/sh

for f in *.png; do echo "Converting $f"; convert "$f" -background '#ddd'  -alpha remove -resize 28x28 "$(basename "$f" .png).gif"; done

