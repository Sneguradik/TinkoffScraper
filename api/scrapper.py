import asyncio

from tinkoff.invest import InstrumentShort, TradeDirection
from tinkoff.invest.async_services import AsyncServices

from logger_config import logger
from .InstrumentInfo import InstrumentInfo, LastPosition
from .lasttrades import get_last_trades
from .orderbook import get_order_book


async def scrap_data(instrument:InstrumentShort, client: AsyncServices)->InstrumentInfo|None:
    try:
        logger.info(f"Scraping data for {instrument.ticker} ({instrument.figi})")
        done = await asyncio.gather(get_last_trades(instrument.figi, client), get_order_book(instrument.figi, client))

        if done[0].trades[0].direction == TradeDirection.TRADE_DIRECTION_BUY:
            side = "buy"
        elif done[0].trades[0].direction == TradeDirection.TRADE_DIRECTION_SELL:
            side = "sell"
        else:
            side = "unspecified"
        last_trade = LastPosition(float(str(done[0].trades[0].price.units)+"."+str(done[0].trades[0].price.nano)),
            done[0].trades[0].quantity, side, done[0].trades[0].time)
        best_bid = LastPosition(float(str(done[1].bids[0].price.units)+"."+str(done[1].bids[0].price.nano)),
            done[1].bids[0].quantity,"bid", done[1].last_price_ts)
        best_offer = LastPosition(float(str(done[1].asks[0].price.units) + "." + str(done[1].asks[0].price.nano)),
            done[1].asks[0].quantity, "offer", done[1].last_price_ts)

        return InstrumentInfo(instrument.figi, instrument.isin, instrument.ticker, instrument.class_code, best_bid, best_offer, last_trade)

    except Exception as e:
        logger.error(f"Failed to scrape data for {instrument.ticker} ({instrument.figi}): {e}", exc_info=True)
        return None

