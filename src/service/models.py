from enum import Enum

from pydantic import BaseModel, Field


class BlockchainName(str, Enum):
    Ethereum = "ethereum"
    Avalanche = "avalanche"


class EventsResponse(BaseModel):
    from_block: int = Field(None, description="from Block")


class BalanceResponse(BaseModel):
    address: str = Field(None, description="Avalanche address")
    block: int = Field(None, description="Block number")
    blockchain: str = Field(None, description="Blockchain select")


class ErrorResponse(BaseModel):
    message: str = Field(None, description="Error message")
