import requests
import json
import base64
from web3 import Web3, HTTPProvider

# Kaleido node credentials
USER = "U0a89q50kn"
PASS = "mSpzLoL2--2IkF4Tne1zgg9geLFl9TYsQR_8lDNZ6mQ"
RPC_ENDPOINT = "https://u0ujx62qc8-u0elgom1m1-rpc.us0-aws.kaleido.io/"


# Encode credentials
auth = USER + ":" + PASS
encodedAuth = base64.b64encode(auth.encode('ascii')).decode('ascii')

# Headers for API request
headers = {
    'Authorization': 'Basic %s' % encodedAuth,
    'Content-Type': 'application/json',
    'User-Agent': 'kaleido-web3py'
}

# ABI obtained from Kaleido
contract_abi = [...]  # Replace with the actual ABI you obtained

# Contract address obtained from Kaleido
contract_address = "0xYourContractAddress"  # Replace with the actual contract address

# Initialize the Web3 instance
web3 = Web3(HTTPProvider(endpoint_uri=RPC_ENDPOINT, request_kwargs={'headers': headers}))

# Initialize the Contract Instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Your data for mintToken function
token_id = 123
token_type = "example_type"
materials = "example_materials"
color = "example_color"

# Create data for transaction
transaction_data = contract.functions.mintToken(token_id, token_type, materials, color).buildTransaction()

# Sign the transaction
signed_transaction = web3.eth.account.sign_transaction(transaction_data, private_key="0xYourPrivateKey")

# Send the transaction
transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

print(f"Transaction Hash: {transaction_hash}")
