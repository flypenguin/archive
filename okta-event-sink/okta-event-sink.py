#!/usr/bin/env python3

from json import dumps

from sanic import Sanic
from sanic.response import json, text


app = Sanic()


def yo(request, path_arg):
    rv = text("")
    if "X-Okta-Verification-Challenge" in request.headers:
        rv = json({"verification": request.headers["X-Okta-Verification-Challenge"]})
    print(f"{request.method} {path_arg}")
    print(dumps(dict(request.headers), sort_keys=True, indent=2))
    if request.headers.get("content-type", "") == "application/json":
        print(dumps(request.json, sort_keys=True, indent=2))
    else:
        print(request.body)
    return rv


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def root(request):
    return yo(request, "/")


@app.route("/<path_arg:path>", methods=["GET", "POST", "PUT", "DELETE"])
async def debugger(request, path_arg):
    return yo(request, path_arg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
