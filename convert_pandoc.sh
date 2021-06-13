#!/bin/bash

BASE=`basename $1 .docx`
DIR=`dirname $1`

METADATA_FILENAMES=(beschreibung name geburtsdaten)

echo "Processing $1"

for METADATA_FILENAME in ${METADATA_FILENAMES[@]}; do
	if [ "$BASE" = "$METADATA_FILENAME" ]
	then
		pandoc -t plain $1 -o $DIR/$BASE.txt
	else
		pandoc -t markdown $1 -o $DIR/$BASE.md
	fi
done