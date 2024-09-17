from src.domain.entities.bid import Bid
from src.ports.repositories.auction_repository import AuctionRepository
from src.use_cases.exceptions import (
    AuctionNotActiveError,
    AuctionNotFoundError,
)


class SubmitBidUseCase:
    def __init__(self, auction_repository: AuctionRepository):
        self._auction_repository = auction_repository

    async def __call__(self, bid: Bid) -> None:
        auction = await self._auction_repository.get(id=bid.auction_id)
        if not auction:
            raise AuctionNotFoundError(bid.auction_id)
        if not auction.is_active:
            raise AuctionNotActiveError(auction.id)
