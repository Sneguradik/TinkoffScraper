import asyncio

from tinkoff.invest.async_services import AsyncServices


async def get_last_price(id : str, client : AsyncServices) -> float :
    return await client.market_data.get_last_prices(figi=id)