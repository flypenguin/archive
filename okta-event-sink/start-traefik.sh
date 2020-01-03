#!/usr/bin/env bash

CA="https://acme-staging-v02.api.letsencrypt.org/directory"
if [ "$1" == "prod" ] ; then
    echo "Using Let's Encrypt's **PRODUCTION** CA."
    CA="https://acme-v02.api.letsencrypt.org/directory"
else
    echo "Using Let's Encrypt's STAGING CA."
    echo "Enable production using '$(basename $0) prod'."
fi

MYDIR=$(realpath $(dirname $0))
LOGDIR="$MYDIR/log"
TCONF="$MYDIR/traefik.toml"
TTEMP="$TCONF.template"

mkdir -p "$LOGDIR"

cat "$TTEMP" | sed -e "s!%%CASERVER%%!$CA!g" > "$TCONF"

echo "Logs in $LOGDIR"
traefik --configFile="$TCONF" "$@" || echo "An error happened, see the logs."
