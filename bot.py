import telebot
from telebot import types
from database import top_5
import json
from gapi import nearest_10


def start():
    bot = telebot.TeleBot('374322077:AAE3Ef7mjY0dkpQ0utCClXRFT0D79w9mJDs')
    markup = types.ReplyKeyboardMarkup(True, False, row_width=5)
    usd_b = types.KeyboardButton(text='Продажа доллара',request_location=True)
    usd_s = types.KeyboardButton(text='Покупка доллара',request_location=True)
    eu_b = types.KeyboardButton(text='Продажа евро', request_location=True)
    eu_s = types.KeyboardButton(text='Покупка евро', request_location=True)
    markup.row(usd_s, usd_b)
    markup.row(eu_s, eu_b)

    GAPI = 'AIzaSyA4TW4MaPG_YUkCrUWJypsFIgO1OGre6m8'

    # @bot.message_handler(commands=['start'])
    # def send_welcome(message):
    #     bot.send_message(message.chat.id, "Welcome to the tavern")

    # bot.polling()

    def handle_messages(messages):

        msg = 'ТОП-5 самых выгодных предложений: '
        
        for message in messages:
            print(message)
            #if message.location:
                #URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=2000&type=bank&key='+GAPI
                #bot.send_message(message.chat.id, URL.format(str(message.location.latitude), str(message.location.longitude), str(message.location.longitude), #str(message.location.latitude)), reply_markup=markup)
            if message.text=='Продажа доллара': #1
                t = top_5('usd sell')
                s = msg + '\n'
                number = 0
                print(t)
                for i in t:
                    number+=1
                    s = s + str(number) + '. '+ i[0].rstrip() + ': $1 = ' + str(i[1]) + '₽   ' + str(i[5]) + '\n'
                URL = 'https://static-maps.yandex.ru/1.x/?ll={1},{0}&spn=0.016457,0.00619&l=map&pt={2},{3}'
                banks = nearest_10(str(message.location.latitude),str(message.location.longitude))
                print(banks)
                bot.send_message(message.chat.id, s, reply_markup=markup)
            elif message.text=='Покупка доллара': #2
                t = top_5('usd buy')
                s = msg + '\n'
                number = 0
                for i in t:
                    number+=1
                    s = s + str(number) + '. '+i[0].rstrip() + ': $1 = ' + str(i[2]) + '₽   ' + str(i[5]) + '\n'
                bot.send_message(message.chat.id, s, reply_markup=markup)
            elif message.text=='Продажа евро': #3
                t = top_5('eu sell')
                s = msg + '\n'
                number = 0
                for i in t:
                    number+=1
                    s = s + str(number) + '. '+i[0].rstrip() + ': €1 = ' + str(i[3]) + '₽   ' + str(i[5]) + '\n'
                bot.send_message(message.chat.id, s, reply_markup=markup)
            elif message.text=='Покупка евро': #4
                t = top_5('eu buy')
                s = msg + '\n'
                number = 0
                for i in t:
                    number+=1
                    s = s + str(number) + '. '+i[0].rstrip() + ': €1 = ' + str(i[4]) + '₽   ' + str(i[5]) + '\n'
                bot.send_message(message.chat.id, s, reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Желаете узнать актуальный курс обмена валют? \nВыберите подходящий вариант на клавиатуре.', reply_markup=markup)

    bot.set_update_listener(handle_messages)
    bot.polling()
