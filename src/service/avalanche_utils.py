from web3 import Web3
from web3.middleware import geth_poa_middleware
from src.service.settings import config
from src.service.models import BlockchainName
from decimal import Decimal
from fastapi.responses import JSONResponse


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


def get_avalanche_balance(address):
    web3 = get_blockchain_w3(BlockchainName.Avalanche)
    balance = web3.eth.get_balance(address, web3.eth.get_block('latest')['number'])

    return balance


def get_avalanche_balance_block(address, block):
    web3 = get_blockchain_w3(BlockchainName.Avalanche)
    balance = web3.eth.get_balance(address, block)

    return Decimal(balance) / Decimal(10**config.AVALANCHE_DECIMALS)


def get_blockchain_balance_block(address, block, blockchain):
    blockchain = BlockchainName.Avalanche if blockchain == 1 else BlockchainName.Ethereum
    decimals = config.AVALANCHE_DECIMALS if blockchain == 1 else config.ETHEREUM_DECIMALS
    web3 = get_blockchain_w3(blockchain)
    balance = web3.eth.get_balance(address, block)

    return JSONResponse({Decimal(balance) / Decimal(10**decimals)})


# print(get_avalanche_balance('0x66357dCaCe80431aee0A7507e2E361B7e2402370'))
