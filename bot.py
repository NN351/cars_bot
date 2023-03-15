from aiogram import executor
from router import dp # импорт dp(Dispatcher) из файла router


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=False)