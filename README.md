# CamLookupBridge

A Flask server exposing an API enabling limited access to the University of Cambridge Lookup Service API from outside the CUDN to authorised users only, via the SRCF.

## Installation

```
git clone https://github.com/fpervaiz/CamLookupBridge.git
cd CamLookupBridge
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Local Development

```
CAMLOOKUPBRIDGE_ADMIN_PWD=<password>
python3 server.py
```

## Deployment

https://docs.srcf.net/app-hosting/index.html
