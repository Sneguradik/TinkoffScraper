from typing import List

from tinkoff.invest import AsyncClient, Client, InstrumentType, InstrumentShort
from tinkoff.invest.async_services import AsyncServices


async def get_instruments(ticker : str, client : AsyncServices) -> List[InstrumentShort] :

    return list(filter(lambda x: True, (await client
       .instruments
       .find_instrument(query=ticker, instrument_kind= InstrumentType.INSTRUMENT_TYPE_SHARE))
       .instruments))   