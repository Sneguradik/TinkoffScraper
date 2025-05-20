from tinkoff.invest import AsyncClient, GetLastTradesResponse
from tinkoff.invest.async_services import AsyncServices


async def get_last_trades(id : str, client: AsyncServices)->GetLastTradesResponse:
    return await client.market_data.get_last_trades(figi=id)