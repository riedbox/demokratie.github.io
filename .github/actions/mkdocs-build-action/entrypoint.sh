#!/bin/bash

cd ${GITHUB_WORKSPACE}

echo "" > custom_theme/css/desktop.css
mkdocs build

lftp -u ${FTP_USERNAME},${FTP_PASSWORD} ${FTP_HOST} << EOF
mirror -vRn ./site ${FTP_TARGET_DIR}
EOF