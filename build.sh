find src/ -name \*.docx -exec ./convert_pandoc.sh {} \;
rsync --exclude=*.docx -r src/ docs

rsync -rv  --include="*/" --include="*.jpg" --exclude="*"  src/ docs