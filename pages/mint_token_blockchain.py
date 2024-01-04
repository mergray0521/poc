import streamlit as st
from web3 import Web3, HTTPProvider
import base64

# Connect to Kaleido
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

# Initialize the Web3 instance
web3 = Web3(HTTPProvider(endpoint_uri=RPC_ENDPOINT, request_kwargs={'headers': headers}))

# ABI obtained from Kaleido
contract_abi = [
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "tokenType",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "materials",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "color",
        "type": "string"
      }
    ],
    "name": "TokenMinted",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "getTokenDetails",
    "outputs": [
      {
        "components": [
          {
            "internalType": "string",
            "name": "tokenType",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "materials",
            "type": "string"
          },
          {
            "internalType": "string",
            "name": "color",
            "type": "string"
          },
          {
            "internalType": "bool",
            "name": "minted",
            "type": "bool"
          }
        ],
        "internalType": "struct TokenMinter.Token",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "tokenType",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "materials",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "color",
        "type": "string"
      }
    ],
    "name": "mintToken",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "tokens",
    "outputs": [
      {
        "internalType": "string",
        "name": "tokenType",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "materials",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "color",
        "type": "string"
      },
      {
        "internalType": "bool",
        "name": "minted",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]  

# Contract address obtained from Kaleido
contract_address = "0xYourContractAddress"  # Replace with the actual contract address

# Initialize the Contract Instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Streamlit App
st.title("Mint Token")
with st.form("mint_token"):
    st.header("Create New Token")
    token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
    token_type = st.text_input('Token Type', "")
    materials = st.text_input('Materials', "")
    color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
    mint = st.form_submit_button(label="Mint")
    
    if mint:
        # Mint the token on the Kaleido blockchain
        transaction_data = contract.functions.mintToken(token_id, token_type, materials, color).buildTransaction()
        signed_transaction = web3.eth.account.sign_transaction(transaction_data, private_key="0xYourPrivateKey")
        transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        
        st.success(f"New Token Minted and saved to Kaleido: {token_id}")
