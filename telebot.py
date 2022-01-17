import telebot
from telebot import types
from datetime import datetime
from API import token
import requests
import json 
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

bot = telebot.TeleBot(token)
driver = webdriver.Chrome()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Новости')
    item2 = types.KeyboardButton('Курсы Валют')
    item3 = types.KeyboardButton('Погода')
    item4 = types.KeyboardButton('Youtube')
    item5 =  types.KeyboardButton('Другое')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        if message.text == 'Новости':
            url = 'https://ria.ru/world/'
            HEADERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
            }

            response = requests.get(url, headers = HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            texts = soup.find_all('a','list-item__title')

            for i in range(len(texts[:-5]), -1, -1):
                txt = str(i + 1) + ') ' + texts[i].text
                bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')

        elif message.text == 'Курсы Валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('USD')
            item2 = types.KeyboardButton('EUR')
            item3 = types.KeyboardButton('GBP')
            item4 = types.KeyboardButton('BTC')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'Курсы Валют', reply_markup = markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Новости')
            item2 = types.KeyboardButton('Курсы Валют')
            item3 = types.KeyboardButton('Погода')
            item4 = types.KeyboardButton('Youtube')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Назад', reply_markup = markup)
    #ВАЛЮТА
        elif message.text == 'USD':
            req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js') 
            response = req.json()
            sell_price = response["Valute"]["USD"]["Value"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USD price : {sell_price}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USD price : {sell_price}")
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
        
        elif message.text == 'EUR':
            req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js') 
            response = req.json()
            sell_price = response["Valute"]["EUR"]["Value"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell EUR price : {sell_price}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell EUR price : {sell_price}")
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
        
        elif message.text == 'GBP':
            req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js') 
            response = req.json()
            sell_price = response["Valute"]["GBP"]["Value"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell GBP price : {sell_price}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell GBP price : {sell_price}")
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
        
        elif message.text == "BTC":
            req = requests.get('https://yobit.net/api/3/ticker/btc_usd') 
            response = req.json()
            sell_price = response["btc_usd"]["sell"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTc price : {sell_price}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price : {sell_price}")
    #ПОГОДА
        elif message.text == 'Погода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Волгоград')
            item2 = types.KeyboardButton('Лос-Анджелес')
            item3 = types.KeyboardButton('Токио')
            item4 = types.KeyboardButton('Назад')


            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Погода', reply_markup = markup)
        
        elif message.text == 'Волгоград':
            req = requests.get('http://api.weatherapi.com/v1/current.json?key=e59a93487bb644dc97a170626212007&q=Volgograd&aqi=no') 
            response = req.json()
            weather = response["location"]["name"]
            weather1 = response["current"]["temp_c"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nГород:  {weather}\nТемпература:  {weather1}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nГород:  {weather}\nТемпература:  {weather1}")
        
        elif message.text == 'Лос-Анджелес':
            req = requests.get('http://api.weatherapi.com/v1/current.json?key=e59a93487bb644dc97a170626212007&q=Los Angeles&aqi=no') 
            response = req.json()
            weather = response["location"]["name"]
            weather1 = response["current"]["temp_c"]
            weather2 = response["current"]["condition"]["text"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nГород:  {weather}\nТемпература:  {weather1}\n{weather2}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nГород:  {weather}\nТемпература:  {weather1}\n{weather2}")
        
        elif message.text == 'Токио':
            req = requests.get('http://api.weatherapi.com/v1/current.json?key=e59a93487bb644dc97a170626212007&q=Tokyo&aqi=no') 
            response = req.json()
            weather = response["location"]["name"]
            weather1 = response["current"]["temp_c"]
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nГород:  {weather}\nТемпература:  {weather1}")
            bot.send_message(
                message.chat.id, 
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nГород:  {weather}\nТемпература:  {weather1}")
        if message.text == 'Youtube':
            msg1 = bot.send_message(message.chat.id, "Введите текст который вы хотите найти в ютуб")
            bot.register_next_step_handler(msg1, search_v)
def search_v(message):
            bot.send_message(message.chat.id, "Начинаю поиск")
            video_href = "https://www.youtube.com/results?search_query=" + message.text
            driver.get(video_href)
            sleep(2)
            videos = driver.find_elements_by_id("video-title")
            for i in range(len(videos)):
                yt = bot.send_message(message.chat.id, videos[i].get_attribute('href'))
                if i == 1:
                    break



bot.polling(none_stop=True)
#reset