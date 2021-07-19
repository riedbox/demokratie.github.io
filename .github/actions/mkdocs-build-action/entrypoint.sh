#!/bin/bash

cd ${GITHUB_WORKSPACE}

echo "" > custom_theme/css/desktop.css
echo "" > custom_theme/js/timeout.js
mkdocs build

lftp -u ${FTP_USERNAME},${FTP_PASSWORD} ${FTP_HOST} << EOF
mirror -vRn ./site ${FTP_TARGET_DIR}
EOF