from brownie import Contract
from typing import Dict

from ..core.config import settings


CONTRACTS = {}

def get_contract(k: str) -> Contract:
    return CONTRACTS.get(k)


def update_contract(k: str, c: Contract) -> None:
    return CONTRACTS.update({k: c})
