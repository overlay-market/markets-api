import json
import os

from brownie import Contract, network
from typing import Dict

from ..core.config import settings


def load_abi(fp: str) -> Dict:
    abi = {}
    with open(fp) as f:
        abi = json.load(f)
    return abi


def init_chain(contracts: Dict) -> None:
    network.connect(settings.BROWNIE_NETWORK)

    # TODO: load contracts from abi


def close_chain(contracts: Dict) -> None:
    contracts.clear()
    network.disconnect()
