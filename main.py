from datetime import datetime
import asyncio

async def tick():
    while True:
        Element("caixa_mensagem").write(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        await asyncio.sleep(1)

asyncio.ensure_future(tick())