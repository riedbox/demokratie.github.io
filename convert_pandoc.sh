#!/bin/bash

BASE=`basename $1 .docx`
DIR=`dirname $1`

METADATA_FILENAMES=(beschreibung name geburtsdaten)

echo "Processing $1"

IS_METADATA_FILE=false

for METADATA_FILENAME in ${METADATA_FILENAMES[@]}; do
	if [ "$BASE" = "$METADATA_FILENAME" ]
	then
		IS_METADATA_FILE=true
	fi
done

if [ "$IS_METADATA_FILE" = true ] ; then
	pandoc -t plain $1 -o $DIR/$BASE.txt
else
	pandoc -t markdown_strict $1 -o $DIR/$BASE.md
fi