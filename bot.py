#requests import
import requests

#getting bitcoin course
def get_btc(): 
  url_btc = "https://api.cryptonator.com/api/ticker/btc-usd" 
  resultbtc = requests.get(url_btc)
  decoded = resultbtc.json()
  return decoded['ticker']['price']
btc = get_btc()

#getting ethirium course
def get_eth(): 
  url_eth = "https://api.cryptonator.com/api/ticker/eth-usd" 
  resulteth = requests.get(url_eth)
  decoded = resulteth.json()
  return decoded['ticker']['price']
eth = get_eth()

#send message to user
def send_message(chat, text):
  url = "https://api.telegram.org/bot597179716:AAFxtGS5TlmDk4tF4u_iAcyig9P1lwc_Lac/sendMessage" 
  params = {'chat_id': chat, 'text': text}
  response = requests.post(url, params = params)
  return response

#getting all updates
def get_bot_updates(limit, offset):
  url = "https://api.telegram.org/bot597179716:AAFxtGS5TlmDk4tF4u_iAcyig9P1lwc_Lac/getUpdates" 
  params = {'limit': limit, 'offset': offset}
  result = requests.get(url, params = params)
  decoded = result.json()
  return decoded['result']

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

last_update_id = last_update['update_id']
offset = last_update_id + 1

#response to user
def runUserCommand(botUpdates):
  for msg in botUpdates:
    textMessage = msg['message']['text'].lower()
    userId = msg['message']['from']['id']
    if textMessage == '/btc':
      btcCourse = 'Bitcoin = ' + str(get_btc()) + ' usd' 
      send_message(userId, btcCourse) 
    if textMessage == '/eth':
        ethCourse = 'Ethreum =' + str(get_eth()) + ' usd'
        send_message(userId, ethCourse)   
    if textMessage == '/start': 
        send_message(userId,"Welcome to the cryptocurrency bot! Push /start for information, /btc for bitcoin course, /eth for ethereum course.")


#whole bot cycle 
while True:
  limit = 5
  offset = None
  botUpdates = get_bot_updates(limit, offset)
  runUserCommand(botUpdates)

#basic information
botId = 597179716
chatId = 56350945



""" 
switch(variable):
  'btc':
    doSomething
  'value2':
    dosOmethingElse
  'valueN':
    doSomethingDeff
  default:
    do something default 
"""
