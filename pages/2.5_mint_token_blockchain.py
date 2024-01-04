import streamlit as st
import base64
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

# Check and install 'web3' package if not already installed
try:
    import web3
except ImportError:
    st.warning("Installing required package. This may take a moment...")
    import subprocess
    subprocess.run(["pip", "install", "web3"])
    st.success("Package installed successfully. Please run the script again.")
    st.stop()

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

# Construct a Web3 object by constructing and passing the HTTP Provider
provider = HTTPProvider(endpoint_uri=RPC_ENDPOINT, request_kwargs=headers)
w3 = Web3(provider)

# Add the Geth POA middleware needed for ExtraData Header size discrepancies between consensus algorithms
w3.middleware_stack.inject(geth_poa_middleware, layer=0)

st.title("Mint Token")
with st.form("mint_token"):
    st.header("Create New Token")
    token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
    token_type = st.text_input('Token Type', "")
    materials = st.text_input('Materials', "")
    color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
    mint = st.form_submit_button(label="Mint")
    if not mint and not st.session_state.get("Mint"):
        st.stop()

    # Save form data to Kaleido blockchain
    contract_address = "0x3d7fa7fd572cb6a95ad3e0a971e6ab48094ae67f"  
    contract_abi = [...]  # Replace with your actual contract ABI

    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    transaction = contract.functions.mintToken(token_id, token_type, materials, color).transact()

    st.session_state["Mint"] = True
    st.success(f"New Token Created and saved to Kaleido: {token_id}")

