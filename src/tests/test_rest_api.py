import json

import httpx
import pytest
from fastapi.testclient import TestClient
from service.server import app
from service.settings import config
from service.rest import avalanche_methods


app.include_router(avalanche_methods.router)
client = TestClient(app)


def test_get_events():
    response = client.get("/api/events/21767581/")
    assert response.status_code == 200

    if len(json.loads(response.content)) > 0:
        assert "0x66357dcace80431aee0a7507e2e361b7e2402370" == json.loads(response.content)[0]['address']
    else:
        assert [] == json.loads(response.content)


def test_get_events_bad_block_number():
    response = client.get("/api/events/block/")
    assert response.status_code >= 400


def test_get_balance_avalanche():
    response = client.get("/api/balance/avalanche/21750537/0x9AA0B87c5af1a8dED6819b1e73c8cD6F59c20Cb4/")
    assert response.status_code == 200
    assert 2942863244046906814 == int(response.content)


def test_get_balance_avalanche_bad_block_number():
    response = client.get("/api/balance/avalanche/block/0x9AA0B87c5af1a8dED6819b1e73c8cD6F59c20Cb4/")
    assert response.status_code >= 400


def test_get_balance_ethereum():
    response = client.get("/api/balance/ethereum/15866820/0xDAFEA492D9c6733ae3d56b7Ed1ADB60692c98Bc5/")
    assert response.status_code == 200
    assert 1149708503369357175 == int(response.content)
