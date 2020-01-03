# Okta event sink

This is my pet project to debug / test / evaluate the Okta Events API from my home system.

Basically it's a ...

* traefik proxy, which uses Let's Encrypt and DynU to provide a valid HTTPS endpoint to the outside world, ...
* ... forwards them to ...
* ... a Python Sanic application which accepts all streamed Okta events and dumps them to stdout.

Some niceties:

* `localhost` is not being secured with ACME, because why?
* the DynU URL is.

## QUICKSTART

* Mac / Linux
* Install traefik & postman
* Set up an event hook with postman
* Before veryfying, ...
    * forward your ports 80 and 443 to your loal machine
    * run `./start-traefik.sh YOUR_URL` (where `YOUR_URL` is a public URL where you machine can be reached under form the internet)
    * create a virtualenv, install the requirements with pip
    * run `python3 okta-event-sink.py`
* done.

## Common pitfalls

### Traefik errors

#### TLS handshake error from <some-ip>:<some-port>: remote error: tls: unknown certificate authority

Your CLIENT cut the connection. If it's curl, try `--insecure` so the certificate validation does not fail.