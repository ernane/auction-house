from datetime import datetime
from uuid import UUID, uuid4

from src.domain.entities.bid import Bid
from src.domain.value_objects.price import Price


def test_bid_creation():
    bidder_id = uuid4()
    price = Price(value=100.0, currency='BRL')
    auction_id = uuid4()

    bid = Bid(bidder_id=bidder_id, price=price, auction_id=auction_id)

    assert isinstance(bid, Bid)
    assert bid.bidder_id == bidder_id
    assert bid.price == price
    assert bid.auction_id == auction_id
    assert isinstance(bid.id, UUID)
    assert isinstance(bid.created_at, datetime)


def test_bid_default_values():
    bidder_id = uuid4()
    price = Price(value=100.0, currency='BRL')
    auction_id = uuid4()

    bid = Bid(bidder_id=bidder_id, price=price, auction_id=auction_id)

    assert bid.id is not None
    assert bid.created_at is not None


def test_bid_currency():
    bidder_id = uuid4()
    price = Price(value=100.0, currency='BRL')
    auction_id = uuid4()

    bid = Bid(bidder_id=bidder_id, price=price, auction_id=auction_id)

    assert bid.price.currency == 'BRL'
