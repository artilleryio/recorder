import datetime
import os

import json

exclude_extensions = [ "jpg", "png", "gif", "txt", "css", "js", "html" ]
exclude_headers = [ "proxy-connection", "host", "user-agent", "content-length", "connection" ]
target = ""
if "TARGET" in os.environ:
  target = os.environ["TARGET"]

def response(context, flow):

  if not(target in flow.request.host):
    print target
    print flow.request.host
    return

  for ext in exclude_extensions:
    if flow.request.path.endswith(ext):
      return

  with open("recording.json", "a") as f:

    #
    # headers
    #
    headers = []

    for h in flow.request.headers:
      if not(h[0].lower() in exclude_headers):
        headers.append([h[0].lower(), h[1]])

    headers_str = "{"
    for h in headers:
      headers_str += """ "%s" : "%s" """ % (h[0].lower(), h[1])
    headers_str += "}"

    #
    # request body
    #
    is_json = False
    for h in headers:
      if (h[0] == "content-type")  and ("json" in h[0]):
        is_json = True
        break

    #
    # write out JSON
    #
    opts = {}
    opts["url"] = flow.request.path
    if len(h) > 0:
      opts["headers"] = {}
      for h in headers:
        opts["headers"][h[0]] = h[1]

    if "content-type" in opts["headers"]:
      if "json" in opts["headers"]["content-type"]:
        if len(flow.request.content) > 0:
          opts["json"] = json.loads(flow.request.content)
      else:
        opts["body"] = flow.request.content

    request_spec = { flow.request.method.lower() : opts }

    #f.write(json.dumps(request_spec, indent=2) + "\n")
    f.write(json.dumps(request_spec) + "\n")
