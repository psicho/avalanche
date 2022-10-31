from typing import Optional

from fastapi import APIRouter, Query, Path

from ..models import BalanceResponse, ErrorResponse, EventsResponse
from service.settings import config
from ..avalanche_utils import get_balance_back, get_contract_events

router = APIRouter()


@router.get(
    config.API_ROOT + "/balance/{blockchain}/{block}/{address}/",
    responses={
        200: {"model": BalanceResponse},
        404: {"model": ErrorResponse},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
async def get_balance(address: str = Path(None, description="Avalanche account address"),
                      block: int = Path(None, description="Number of block"),
                      blockchain: str = Path(None, description="Blockchain name")
                      ) -> BalanceResponse:
    return get_balance_back(address, block, blockchain)


@router.get(
    config.API_ROOT + "/events/{from_block}/",
    responses={
        200: {"model": EventsResponse},
        404: {"model": ErrorResponse},
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
async def get_events(from_block: int = Path(None, description="Start block number"),
                     ) -> EventsResponse:
    return get_contract_events(from_block)
