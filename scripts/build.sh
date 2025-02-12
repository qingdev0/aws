#!/bin/bash
set -e

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
echo "Created temporary directory: ${TEMP_DIR}"

# Install dependencies to the temporary directory
poetry export -f requirements.txt --without-hashes | pip install -r /dev/stdin --target "${TEMP_DIR}"

# Copy source code
cp -r src/steps "${TEMP_DIR}"/

# Create zip file
cd "${TEMP_DIR}"
zip -r9 ../lambda.zip .

# Cleanup
cd ..
rm -rf "${TEMP_DIR}"

echo "Created lambda.zip"
