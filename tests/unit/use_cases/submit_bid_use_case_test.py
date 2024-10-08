import uuid
from datetime import date, timedelta

import pytest

from src.adapters.repositories.auction_repository.in_memory_repository import (
    InMemoryAuctionRepository,
)
from src.ports.repositories.auction_repository import AuctionRepository
from src.use_cases.exceptions import (
    AuctionNotActiveError,
    AuctionNotFoundError,
    LowBidError,
)
from src.use_cases.submit_bid_use_case import SubmitBidUseCase
from tests.utils import create_auction, create_bid


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


async def test_auction_not_active(
    auctions_repository: InMemoryAuctionRepository,
    submit_bid_use_case: SubmitBidUseCase,
):
    auction = create_auction(end_date=date.today() - timedelta(days=1))
    auctions_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id)
    with pytest.raises(AuctionNotActiveError):
        await submit_bid_use_case(bid)


async def test_bid_price_lower_than_start_price(
    auctions_repository: InMemoryAuctionRepository,
    submit_bid_use_case: SubmitBidUseCase,
):
    auction = create_auction(start_price_value=10)
    auctions_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id, price_value=9)
    with pytest.raises(LowBidError):
        await submit_bid_use_case(bid)


async def test_bid_successfully_added(
    auctions_repository: InMemoryAuctionRepository,
    submit_bid_use_case: SubmitBidUseCase,
):
    auction = create_auction()
    auctions_repository.auctions.append(auction)
    bid = create_bid(auction_id=auction.id)
    await submit_bid_use_case(bid)
    result = await auctions_repository.get(id=auction.id)
    assert result is not None
    assert bid in result.bids
