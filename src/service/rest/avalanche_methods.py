from typing import Optional

from fastapi import APIRouter, Query, Path

from ..models import BalanceResponse, BalanceBlockResponse, ErrorResponse, BalanceBlockchainBlockResponse
from src.service.settings import config
from ..avalanche_utils import get_avalanche_balance, get_avalanche_balance_block, get_blockchain_balance_block

router = APIRouter()


@router.get(
    config.API_ROOT + "/balance/{address}/",
    responses={
        200: {"model": BalanceResponse},
        500: {"model": ErrorResponse},
    },
)
async def get_balance(address: str = Path(None, description="Avalanche account address")) -> BalanceResponse:
    return get_avalanche_balance(address)


@router.get(
    config.API_ROOT + "/balance/{block}/{address}/",
    responses={
        200: {"model": BalanceBlockResponse},
        500: {"model": ErrorResponse},
    },
)
async def get_balance(address: str = Path(None, description="Avalanche account address"),
                      block: int = Path(None, description="Number of block")) -> BalanceBlockResponse:
    return get_avalanche_balance_block(address, block)


@router.get(
    config.API_ROOT + "/balance/{blockchain}/{block}/{address}/",
    responses={
        200: {"model": BalanceBlockchainBlockResponse},
        500: {"model": ErrorResponse},
    },
)
async def get_balance(address: str = Path(None, description="Avalanche account address"),
                      block: int = Path(None, description="Number of block"),
                      blockchain: int = Path(None, description="Blockchain name")
                      ) -> BalanceBlockchainBlockResponse:
    return get_blockchain_balance_block(address, block, blockchain)

# async def get_balance(address: str = Path(None, description="XRPL account address")) -> BalanceResponse:
#     return await get_account_balance(address)
