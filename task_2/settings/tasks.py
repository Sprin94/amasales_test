import asyncio

from api.services import go_parser
from celery import shared_task


@shared_task
async def task_go_parser(vendor_codes):
    res = asyncio.run_coroutine_threadsafe(go_parser(vendor_codes))
    return res
