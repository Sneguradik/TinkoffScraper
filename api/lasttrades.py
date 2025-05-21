import datetime

from tinkoff.invest import AsyncClient, GetLastTradesResponse
from tinkoff.invest.async_services import AsyncServices


async def get_last_trades(id : str, client: AsyncServices, start_time: datetime.datetime|None = None, end_time: datetime.datetime|None = None)->GetLastTradesResponse:
    if start_time and end_time:
        return await client.market_data.get_last_trades(instrument_id=id, from_=start_time, to=end_time)
    return await client.market_data.get_last_trades(figi=id)