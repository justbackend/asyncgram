from asyncgram.bot.bot import Bot
from asyncgram.dispatcher.dispatcher import Dispatcher

token = '7660557154:AAEzzBHpyIPuQrveXdRKcttK1kNtclB2ZjQ'
bot = Bot(token=token)
dp = Dispatcher()
dp.start_polling(bot)