#!/bin/sh
set -e

BASE_DIR="./data"
RAND_DIR=$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 10 | head -n 1)
FULL_PATH="$BASE_DIR/$RAND_DIR"

mkdir -p $FULL_PATH

RAND_FLAG=$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 16 | head -n 1)
FLAG="LKflag-xdd{$RAND_FLAG}"
echo "$FLAG" > "$FULL_PATH/flag.txt"

echo "[+] Flag generated at: $FULL_PATH/flag.txt"
echo "[!] Remember: path changes every container start"

exec "$@"
