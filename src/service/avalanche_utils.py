import json
import requests
from web3 import Web3
from web3.middleware import geth_poa_middleware
from src.service.settings import config
from src.service.models import BlockchainName
from decimal import Decimal


def normalize_value(value):
    return Decimal(value) / Decimal(10 ** config.AVALANCHE_DECIMALS)


def get_blockchain_w3(blockchain):
    rpc_client = (config.AVALANCHE_RPC_ADDRESS
                  if blockchain == BlockchainName.Avalanche
                  else config.ETHEREUM_RPC_ADDRESS
                  )

    w3 = Web3(Web3.HTTPProvider(rpc_client))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    return w3


def get_contract_events(from_block: int):
    web3 = get_blockchain_w3(BlockchainName.Avalanche)
    latest_block = web3.eth.get_block('latest')['number']
    api_key_token = "ApiKeyToken"
    url_host = "https://api.snowtrace.io/api?module=logs&action=getLogs"
    url_request = f"&fromBlock={from_block}&toBlock={latest_block}&address=0x66357dCaCe80431aee0A7507e2E361B7e2402370"
    api_key = f"&apikey={api_key_token}"
    result_url = url_host + url_request + api_key

    r = requests.get(result_url)

    return json.loads(r.content)['result']


def get_balance_back(address: str, block: int, blockchain: str):
    blockchain_select = BlockchainName.Avalanche if blockchain == 'avalanche' else BlockchainName.Ethereum
    decimals = config.AVALANCHE_DECIMALS if blockchain == 'avalanche' else config.ETHEREUM_DECIMALS
    web3 = get_blockchain_w3(blockchain_select)
    balance = web3.eth.get_balance(address, block)

    return balance
