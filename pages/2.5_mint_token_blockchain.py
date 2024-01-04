import streamlit as st

try:
    import web3
except ImportError:
    st.warning("Installing required package. This may take a moment...")
    import subprocess
    subprocess.run(["pip", "install", "web3"])
    st.success("Package installed successfully. Please run the script again.")
    st.stop()

import base64
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

# Rest of your code...
# Connect to Kaleido
USER = "U0a89q50kn"
PASS = "mSpzLoL2--2IkF4Tne1zgg9geLFl9TYsQR_8lDNZ6mQ"
RPC_ENDPOINT = "https://u0ujx62qc8-u0elgom1m1-rpc.us0-aws.kaleido.io/"

# Encode the app creds into USER:PASS 
auth = USER + ":" + PASS
encodedAuth = base64.b64encode(auth.encode('ascii')).decode('ascii')

# Build the header object with the Basic auth and the standard headers
headers = {'headers': {'Authorization': 'Basic %s' % encodedAuth,
                       'Content-Type': 'application/json',
                       'User-Agent': 'kaleido-web3py'}}

# Constru
