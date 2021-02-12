#!/bin/sh

# Decrypt the file
mkdir "$HOME/secrets"
# --batch to prevent interactive command
# --yes to assume "yes" for questions
echo 'Directory structure'
ls -la
gpg --quiet --batch --yes --decrypt --passphrase="$SECRET_PASSPHRASE" \
--output "$HOME/secrets/config.yml" "random_word/config.yml.gpg"
