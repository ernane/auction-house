from datetime import date, timedelta
from uuid import UUID, uuid4

from src.domain.entities.auction import Auction
from src.domain.entities.bid import Bid
from src.domain.entities.item import Item
from src.domain.value_objects.price import Price


def test_auction_creation():
    item = Item(name='Test Item', description='A test item')
    seller_id = uuid4()
    start_date = date.today()
    end_date = date.today() + timedelta(days=10)
    start_price = Price(value=100.0, currency='BRL')

    auction = Auction(
        item=item,
        seller_id=seller_id,
        start_date=start_date,
        end_date=end_date,
        start_price=start_price,
    )

    assert isinstance(auction, Auction)
    assert auction.item == item
    assert auction.seller_id == seller_id
    assert auction.start_date == start_date
    assert auction.end_date == end_date
    assert auction.start_price == start_price
    assert isinstance(auction.id, UUID)
    assert auction.bids == []


def test_auction_is_active():
    item = Item(name='Test Item', description='A test item')
    seller_id = uuid4()
    start_date = date.today() - timedelta(days=1)
    end_date = date.today() + timedelta(days=1)
    start_price = Price(value=100.0, currency='BRL')

    auction = Auction(
        item=item,
        seller_id=seller_id,
        start_date=start_date,
        end_date=end_date,
        start_price=start_price,
    )

    assert auction.is_active is True

    auction.end_date = date.today() - timedelta(days=1)
    assert auction.is_active is False


def test_auction_minimal_bid_price():
    item = Item(name='Test Item', description='A test item')
    seller_id = uuid4()
    start_date = date.today()
    end_date = date.today() + timedelta(days=10)
    start_price = Price(value=100.0, currency='BRL')

    auction = Auction(
        item=item,
        seller_id=seller_id,
        start_date=start_date,
        end_date=end_date,
        start_price=start_price,
    )

    assert auction.minimal_bid_price == start_price

    bid1 = Bid(
        bidder_id=uuid4(),
        price=Price(value=150.0, currency='BRL'),
        auction_id=auction.id,
    )
    bid2 = Bid(
        bidder_id=uuid4(),
        price=Price(value=200.0, currency='BRL'),
        auction_id=auction.id,
    )

    auction.bids.append(bid1)
    assert auction.minimal_bid_price == bid1.price

    auction.bids.append(bid2)
    assert auction.minimal_bid_price == bid2.price
