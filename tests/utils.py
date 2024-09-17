from uuid import UUID, uuid4

from src.domain.entities.bid import Bid
from src.domain.value_objects.price import CurrencyOption, Price


def create_bid(
    auction_id: UUID | None = None,
    price_value: float = 100.0,
    price_currency: CurrencyOption = CurrencyOption.real,
) -> Bid:
    return Bid(
        bidder_id=uuid4(),
        price=Price(value=price_value, currency=price_currency),
        auction_id=auction_id if auction_id else uuid4(),
    )
