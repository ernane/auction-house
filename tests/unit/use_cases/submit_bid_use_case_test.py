import uuid

import pytest

from src.adapters.repositories.auction_repository.in_memory_repository import (
    InMemoryAuctionRepository,
)
from src.ports.repositories.auction_repository import AuctionRepository
from src.use_cases.exceptions import AuctionNotFoundError
from src.use_cases.submit_bid_use_case import SubmitBidUseCase
from tests.utils import create_bid


@pytest.fixture
def auctions_repository() -> AuctionRepository:
    return InMemoryAuctionRepository()


@pytest.fixture
def submit_bid_use_case(
    auctions_repository: AuctionRepository,
) -> SubmitBidUseCase:
    return SubmitBidUseCase(auctions_repository)


async def test_auction_not_found(submit_bid_use_case: SubmitBidUseCase):
    bid = create_bid(auction_id=uuid.uuid4())

    with pytest.raises(AuctionNotFoundError):
        await submit_bid_use_case(bid)
