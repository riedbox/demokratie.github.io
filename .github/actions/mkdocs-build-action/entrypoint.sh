#!/bin/bash

cd ${GITHUB_WORKSPACE}

echo "" > custom_theme/css/desktop.css
echo "" > custom_theme/js/timeout.js
cp docs/project-video-embed.md docs/project-video-desktop.md
mkdocs build

lftp -u ${FTP_USERNAME},${FTP_PASSWORD} ${FTP_HOST} << EOF
set file:charset utf-8
mirror -vRn ./site ${FTP_TARGET_DIR}
EOF