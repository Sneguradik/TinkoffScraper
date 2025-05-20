import csv
from os import PathLike
from typing import List

from api import InstrumentInfo


def import_tickers(path: PathLike, ticker_column='Tickers')->List[str]:
    tickers = []
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            ticker = row.get(ticker_column)

            if ticker:
                tickers.append(ticker)
    return tickers

def write_instruments_to_csv(path: PathLike, instruments: list[InstrumentInfo]):
    with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        headers = [
            "figi", "isin", "ticker", "class_code",
            "best_bid_price", "best_bid_volume", "best_bid_direction", "best_bid_time",
            "best_offer_price", "best_offer_volume", "best_offer_direction", "best_offer_time",
            "last_deal_price", "last_deal_volume", "last_deal_direction", "last_deal_time"
        ]
        writer.writerow(headers)


        for instrument in instruments:
            row = [
                instrument.figi,
                instrument.isin,
                instrument.ticker,
                instrument.class_code,

                instrument.best_bid.price,
                instrument.best_bid.volume,
                instrument.best_bid.direction,
                instrument.best_bid.time.isoformat(),

                instrument.best_offer.price,
                instrument.best_offer.volume,
                instrument.best_offer.direction,
                instrument.best_offer.time.isoformat(),

                instrument.last_deal.price,
                instrument.last_deal.volume,
                instrument.last_deal.direction,
                instrument.last_deal.time.isoformat(),
            ]
            writer.writerow(row)