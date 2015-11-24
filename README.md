# Minigun Recorder

This package can be used to create [Minigun](http://minigun.io) scenarios from a browser session.

1. Start Minigun Recorder with `sh minigun_recorder.sh`
2. Set your browser's proxy to `http://localhost:10888`
3. Interact with a web application using your browser
4. Stop Minigun Recorder and use the test script it has created from the
browser session

## Installation

The recorder relies on [mitmproxy](https://mitmproxy.org).

1. [Install mitmproxy](http://docs.mitmproxy.org/en/stable/install.html)
2. [Configure certificates](http://docs.mitmproxy.org/en/stable/certinstall.html#installing-the-mitmproxy-ca-certificate-manually) if you want to record HTTPS-based sessions

## License

[ISC](https://en.wikipedia.org/wiki/ISC_license) (same as Minigun)
