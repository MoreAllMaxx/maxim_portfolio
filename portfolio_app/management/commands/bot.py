from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from django.core.management.base import BaseCommand
from portfolio_app.models import Feedback
from django.conf import settings
import asyncio

bot = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


async def send_msg_from_queryset(recall_queryset, new_recall=False):
    _recall = 'Recall' if not new_recall else 'New recall'
    recalls = [
        (f'{_recall}:\nFeedback from: {recall.name}\n' +
         f'Email: {recall.email}\nText: {recall.message}\n') for recall in recall_queryset
    ]
    await bot.send_message(settings.USER_ID, '\n'.join(recalls))


async def main(*args):
    old_recalls = Feedback.objects.all()
    old_recall_ids = [recall.id for recall in old_recalls]
    await send_msg_from_queryset(old_recalls)

    while True:
        new_recalls = Feedback.objects.all().exclude(id__in=old_recall_ids)
        if new_recalls:
            await send_msg_from_queryset(new_recalls, new_recall=True)
            old_recall_ids += [recall.id for recall in new_recalls]
        await asyncio.sleep(5)


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        executor.start_polling(dp, skip_updates=True, on_startup=main)
