import argparse
import asyncio
import os

from logger_config import logger

from dotenv import load_dotenv
from tinkoff.invest import AsyncClient

from api import scrap_data, get_instruments

from io_csv import import_tickers, write_instruments_to_csv

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def main():
    parser = argparse.ArgumentParser(description="Парсер Tinkoff API")
    parser.add_argument("--i", required=True, help="Путь до CSV с тикерами")
    parser.add_argument("--o", default="output.csv", help="Путь CSV для экспорта")
    args = parser.parse_args()

    tickers = import_tickers(args.i)

    instruments_data = []
    async with AsyncClient(TOKEN) as client:

        for i in range(0,len(tickers),10):
            tasks = []
            for ticker in tickers[i:i+10]:
                logger.info("Request tickers")
                instruments = await get_instruments(ticker, client)
                logger.info(f"Got {len(instruments)} tickers")
                for j in range(0,len(instruments),10):
                    for instrument in instruments[j:j+10]:
                        tasks.append(scrap_data(instrument, client))
                    data = await asyncio.gather(*tasks)

                    instruments_data += [item for item in data if item is not None]

                    await asyncio.sleep(3)
            await asyncio.sleep(5)

    write_instruments_to_csv(args.o, instruments_data)


if __name__ == '__main__':
    asyncio.run(main())
