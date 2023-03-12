import asyncio
import json
import platform

from openpyxl import load_workbook

from aiohttp import ClientSession


from api.schemas import Goods


async def _get_response(code):
    url = (r'https://card.wb.ru/cards/detail?spp=0&regions=80,64,38,4,115,83,'
           r'33,68,70,69,30,86,75,40,1,66,31,48,110,22,71&pricemarginCoeff=1.'
           r'0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,'
           rf'3,18,15,21&dest=-1257786&nm={code}')

    async with ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return json.loads(text)


async def _get_responses(vendor_codes: list[str]):
    tasks = []
    for i in vendor_codes:
        task = asyncio.create_task(_get_response(i))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


def _get_code_from_file(file):
    file_im = load_workbook(file.file)
    sheet = file_im.get_sheet_names()[0]
    return [str(i.value) for i in file_im[sheet]['A'] if i.value is not None]


def _parse_json(goods_json: list[dict]) -> list[Goods]:
    res = []
    for good in goods_json:
        data = good.get('data')
        if not data:
            continue
        products = data.get('products')
        if not products:
            continue
        product = products[0]
        res.append(Goods(
            article=product.get('id'),
            brand=product.get('brand'),
            title=product.get('name')
        ))
    return res


def get_goods_info(file, code):
    if file:
        codes = _get_code_from_file(file)
    else:
        codes = [code]
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    goods_json = asyncio.run(_get_responses(codes))
    goods = _parse_json(goods_json)
    return goods
