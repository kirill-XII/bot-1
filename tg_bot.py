import telebot
from telebot import types
from currency_converter import CurrencyConverter


token='7408941702:AAFm2E1bI8Z35m7RbxjfGJ_Ja_Ai3ubMTJg'
bot = telebot.TeleBot(token)
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
      amount = int(message.text.strip())
    except ValueError:
      bot.send_message(message.chat.id, 'Некорректная сумма')
      bot.register_next_step_handler(message, summa)
      return

    if amount>0:
      markup = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
      btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
      btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
      btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
      markup.add(btn1, btn2, btn3, btn4)
      bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть за 0. Впишите корретное значение')
        bot.register_next_step_handler(message, summa)


bot.polling(none_stop=True)