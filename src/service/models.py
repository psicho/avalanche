from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, AnyUrl, RedisDsn as OriginalRedisDsn


class BlockchainName(str, Enum):
    Ethereum = "ethereum"
    Avalanche = "avalanche"


class BalanceResponse(BaseModel):
    address: str = Field(None, description="Avalanche address")


class BalanceBlockResponse(BaseModel):
    address: str = Field(None, description="Avalanche address")
    block: int = Field(None, description="Block number")


class BalanceBlockchainBlockResponse(BaseModel):
    address: str = Field(None, description="Avalanche address")
    block: int = Field(None, description="Block number")
    # blockchain: str = Field(None, description="Blockchain select")
    blockchain: BlockchainName = BlockchainName.Avalanche


class ErrorResponse(BaseModel):
    message: str = Field(None, description="Error message")
