import json
import requests
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


def get_contract_events(from_block: int, to_block: int):
    api_key_token = "ApiKeyToken"
    url_host = "https://api.snowtrace.io/api?module=logs&action=getLogs"
    url_request = f"&fromBlock={from_block}&toBlock={to_block}&address=0x66357dCaCe80431aee0A7507e2E361B7e2402370"
    api_key = f"&apikey={api_key_token}"
    result_url = url_host + url_request + api_key

    r = requests.get(result_url)
    print(json.loads(r.content)['result'])

    return
    web3 = get_blockchain_w3(BlockchainName.Avalanche)
    with open('abi_avax_token.json') as json_file:
        abi_data = json.load(json_file)
    avalanche_contract = web3.eth.contract(address=config.AVALANCHE_SMART_CONTRACT_ADDRESS,
                                           abi=abi_data)
    print(avalanche_contract.address)

    # events = avalanche_contract.pastEvents('Transfer').call()

    # avalanche_contract.methods.getC1().call()

    from web3._utils.events import get_event_data
    from web3._utils.filters import construct_event_filter_params

    # events = avalanche_contract.events\

    # events.eventFilter('Transfer', {'fromBlock': 0, 'toBlock': 'latest'})
    # print(events)
    # for even in events:
    #     print(1)
    #     print(even.event_name)

    # event_filter = web3.eth.filter({"address": avalanche_contract})

    event_filter = avalanche_contract.events.create_filter(fromBlock="latest", argument_filters={'arg1': 10})
    event_filter.get_new_entries()

    # event_filter = web3.eth.filter({
    #     # "fromBlock": 0,
    #     # "toBlock": "latest",
    #     "address": avalanche_contract,
    # })

    print(event_filter)


    # res_event = events.eventFilter('Transfer', {'fromBlock': 0, 'toBlock': 'latest'})

    # events = avalanche_contract.eventFilter('Transfer', {'fromBlock': 0, 'toBlock': 'latest'})

    # print('events', events)
    # ('MyEvent', fromBlock: 0, toBlock: 'latest').call()

    return avalanche_contract


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


get_contract_events(21753727, 21753909)
# print(get_avalanche_balance('0x66357dCaCe80431aee0A7507e2E361B7e2402370'))
