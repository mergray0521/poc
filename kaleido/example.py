import web3
import base64

from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

# TESTED WITH python 3.6

# Fill these in to test, ex. remove @RPC_ENDPOINT@
USER = "U0a89q50kn"
PASS = "mSpzLoL2--2IkF4Tne1zgg9geLFl9TYsQR_8lDNZ6mQ"
RPC_ENDPOINT = "https://u0ujx62qc8-u0elgom1m1-rpc.us0-aws.kaleido.io/"

# Encode the username and password from the app creds into USER:PASS base64 encoded string
auth = USER + ":" + PASS
encodedAuth = base64.b64encode(auth.encode('ascii')).decode('ascii')

# Build the header object with the Basic auth and the standard headers
headers = {'headers': {'Authorization': 'Basic %s' % encodedAuth,
                       'Content-Type': 'application/json',
                       'User-Agent': 'kaleido-web3py'}}

# Construct a Web3 object by constructing and passing the HTTP Provider
provider = HTTPProvider(endpoint_uri=RPC_ENDPOINT, request_kwargs=headers)
w3 = Web3(provider)


# Add the Geth POA middleware needed for ExtraData Header size discrepancies between consensus algorithms
# See: http://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority
# ONLY for GETH/POA; If you are using quorum, comment out the line below
w3.middleware_stack.inject(geth_poa_middleware, layer=0)

# Get the latest block in the chain
block = w3.eth.getBlock("latest")

# Print the block out to the console
print(block)