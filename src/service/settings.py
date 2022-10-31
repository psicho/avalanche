from pydantic import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = "local.env"

    HOST: str = "0.0.0.0"  # '127.0.0.1'
    PORT: int = 8920
    API_ROOT: str = "/api"

    AVALANCHE_RPC_ADDRESS: str = "https://rpc.ankr.com/avalanche"
    AVALANCHE_DECIMALS: int = 18

    ETHEREUM_RPC_ADDRESS: str = "https://rpc.ankr.com/eth"
    ETHEREUM_DECIMALS: int = 18

    AVALANCHE_SMART_CONTRACT_ADDRESS: str = "0x66357dCaCe80431aee0A7507e2E361B7e2402370"


config = Config()
