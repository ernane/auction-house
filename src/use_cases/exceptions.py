from uuid import UUID


class AuctionNotFoundError(Exception):
    def __init__(self, auction_id: UUID):
        self.auction_id = auction_id

    def __str__(self) -> str:
        return f'Auction not found: {self.auction_id}'
