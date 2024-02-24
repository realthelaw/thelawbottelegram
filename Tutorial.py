import time
import random
import telebot
import json
from datetime import datetime
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import bd

api_key = '6898034776:AAEXtOH-ElSFhUSo4fDT9rBQ-fah46j7rRM'
chat_id = '-1002091401570'

bot = telebot.TeleBot(token=api_key)

# Defina as funções ALERT_GALE1 e DELETE_GALE1 como antes
def ALERT_GALE1():
    h = datetime.now().hour
    m = datetime.now().minute + 1
    s = datetime.now().second
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    message_id = bot.send_message(chat_id=chat_id, text=f'''
SPAM INICIANDO''').message_id
    bd.message_ids1 = message_id
    time.sleep(7)
    bd.message_delete1 = True

def DELETE_GALE1():
    if bd.message_delete1 == True:
        bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
        bd.message_delete1 = False

def gerar_minas(quantidade):
    minas = ['💣'] * quantidade + ['💎'] * (25 - quantidade)
    random.shuffle(minas)
    return minas

# Resto do código
def button_link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text="INFECTE-SE AQUI", url="http://xvideos.com"))
    return markup

while True:
    h = datetime.now().hour
    m = datetime.now().minute + 1
    s = datetime.now().second
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')

    minas_configuracoes = [3, 4]
    for minas in minas_configuracoes:
       cores = ['💎', '🟦', '🟦', '🟦', '🟦', '💎', '🟦', '🟦', '🟦', '🟦', '💎', '🟦', '🟦', '🟦', '🟦', '💎', '🟦', '🟦', '🟦', '🟦', '💎', '🟦', '🟦', '💎', '🟦']

    ALERT_GALE1()  # Chama a função de alerta

    DELETE_GALE1()  # Chama a função de exclusão do alerta

    sample = random.sample(cores, k=25)
    message_text = f'''
🕛 Válido até: {h}:{m}
✅ Apostar 5% da sua BANCA                                                    
💣 Minas: {minas}
⏰ Valido Durante: 2 minutos
🔁 Nº de entradas: 1

{' '.join(sample[:5])}
{' '.join(sample[5:10])}
{' '.join(sample[10:15])}
{' '.join(sample[15:20])}
{' '.join(sample[20:])}
'''

    dados = bot.send_message(chat_id=chat_id, text=message_text, reply_markup=button_link())

    time.sleep(60)


    bot.edit_message_text(f'''
✅Sinal concluido às: {h}:{m}✅
 Volte daqui a pouco !
    ''', dados.chat.id, dados.message_id)


    time.sleep(1)
    time.sleep(1) 
    time.sleep(1)
  #by the law
