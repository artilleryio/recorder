#!/bin/sh

set -eu

if [ -z $(which mitmdump) ]; then
  echo "Error: cannot find mitmproxy (http://mitmproxy.org)"
  echo "  On Linux: pip install mitmproxy"
  echo "  On OSX: brew install mitmproxy"
  exit 0
fi

echo "***** Starting HTTP proxy on http://localhost:10888"
mitmdump -s request_writer.py --port 10888

if [ ! -e recording.json ]; then
    exit 1
fi

echo "***** Processing captured requests"
node process.js recording.json > minigun_recorded_script.json
rm recording.json
echo "***** Minigun script created in recorded_script.json"
