BASE=`basename $1 .docx`
DIR=`dirname $1`
pandoc -t markdown $1 -o $DIR/$BASE.md