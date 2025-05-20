from tinkoff.invest import AsyncClient, GetOrderBookResponse
from tinkoff.invest.async_services import AsyncServices


async def get_order_book(id : str, client: AsyncServices)->GetOrderBookResponse:
    return await client.market_data.get_order_book(instrument_id=id, depth=1)