from abc import ABC, abstractmethod
from typing import Any

from src.domain.entities.auction import Auction
from src.domain.entities.bid import Bid


class AuctionRepository(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> Auction | None:
        raise NotImplementedError

    @abstractmethod
    async def add_bid(self, bid: Bid) -> bool:
        raise NotImplementedError
