import json

import httpx
import pytest
from decimal import Decimal
from fastapi.testclient import TestClient
from src.service.server import app
from web3 import Web3
from web3.middleware import geth_poa_middleware
from src.service.models import BlockchainName
from src.service.settings import config
from src.service.rest import avalanche_methods
from src.service.avalanche_utils import (get_balance_back, get_contract_events, normalize_value, get_blockchain_w3)

app.include_router(avalanche_methods.router)
client = TestClient(app)


def test_normalize_value():
    value = 1149708503369357175
    value_func = normalize_value(value)
    assert Decimal("1.149708503369357175") == value_func


def test_get_blockchain_w3():
    # get ethereum rpc connect to node
    address_eth = "0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5"
    ethereum_client = get_blockchain_w3(BlockchainName.Ethereum)
    balance = ethereum_client.eth.get_balance(address_eth, 15866820)
    assert 1149708503369357175 == balance

    # get avalanche rpc connect to node
    address_avax = "0x9AA0B87c5af1a8dED6819b1e73c8cD6F59c20Cb4"
    avalanche_client = get_blockchain_w3(BlockchainName.Avalanche)
    balance = avalanche_client.eth.get_balance(address_avax, 21753992)
    assert 2942863244046906814 == balance
