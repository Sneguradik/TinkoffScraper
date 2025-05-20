from datetime import datetime

from tinkoff.invest import TradeDirection
from tinkoff.invest.async_services import AsyncServices

class LastPosition:

    price: float
    volume:float
    direction:str
    time: datetime

    def __init__(self, price: float ,volume: float, direction: str ,time: datetime):
        self.price = price
        self.volume = volume
        self.time = time
        self.direction = direction

    def to_dict(self):
        return {"price": self.price, "volume": self.volume, "direction": self.direction,"time": self.time.isoformat()}


class InstrumentInfo:
    def __init__(self, figi: str, isin: str, ticker: str, class_code: str,best_bid: LastPosition, best_offer: LastPosition, last_deal: LastPosition):
        self.figi = figi
        self.isin = isin
        self.ticker = ticker
        self.class_code = class_code
        self.best_bid = best_bid
        self.best_offer = best_offer
        self.last_deal = last_deal

    def to_dict(self):
        return {
            "figi": self.figi,
            "isin": self.isin,
            "ticker": self.ticker,
            "class_code": self.class_code,
            "best_bid": self.best_bid.to_dict(),
            "best_offer": self.best_offer.to_dict(),
            "last_deal": self.last_deal.to_dict()
        }