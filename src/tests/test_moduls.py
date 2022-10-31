import json

import httpx
import pytest
from decimal import Decimal
from fastapi.testclient import TestClient
from service.server import app
from web3 import Web3
from web3.middleware import geth_poa_middleware
from service.models import BlockchainName
from service.settings import config
from service.rest import avalanche_methods
from service.avalanche_utils import (
    get_balance_back, get_contract_events,
    normalize_value, get_blockchain_w3,
)

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


def test_get_contract_events():
    from_block = 21767581
    events_history = get_contract_events(from_block)

    if len(events_history) > 0:
        assert "0x66357dcace80431aee0a7507e2e361b7e2402370" == events_history[0]['address']
    else:
        assert [] == events_history


def test_get_balance_back():

    def select_blockchain(blockchain):
        address_select, block_select = "", 0
        if blockchain == "ethereum":
            address_select = "0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5"
            block_select = 15866820
        elif blockchain == "avalanche":
            address_select = "0x9AA0B87c5af1a8dED6819b1e73c8cD6F59c20Cb4"
            block_select = 21767581
        return address_select, block_select

    # Ethereum balance test
    address, block = select_blockchain("ethereum")
    balance = get_balance_back(address, block, "ethereum")
    assert 1149708503369357175 == balance

    # Avalanche balance test
    address, block = select_blockchain("avalanche")
    balance = get_balance_back(address, block, "avalanche")
    assert 2942863244046906814 == balance
