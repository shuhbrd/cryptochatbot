#requests import
import requests

url = "https://api.telegram.org/bot597179716:AAFxtGS5TlmDk4tF4u_iAcyig9P1lwc_Lac/"

#getting bitcoin course
def get_btc(): 
  url_btc = "https://api.cryptonator.com/api/ticker/btc-usd" 
  result_btc = requests.get(url_btc)
  decoded = result_btc.json()
  return decoded['ticker']['price']
btc = get_btc()

#getting etherium course
def get_eth(): 
  url_eth = "https://api.cryptonator.com/api/ticker/eth-usd" 
  result_eth = requests.get(url_eth)
  decoded = result_eth.json()
  return decoded['ticker']['price']
eth = get_eth()

#getting all updates
def get_bot_updates(limit, offset):
  method = url + "getUpdates" 
  params = {'limit': limit, 'offset': offset}
  result = requests.get(method, params = params)
  decoded = result.json()
  return decoded['result']

#send message to user
def send_message(chat, text):
  method = url + "sendMessage" 
  params = {'chat_id': chat, 'text': text}
  response = requests.post(method, params = params)
  return response

#response to user
def run_user_command(bot_updates):
  for msg in bot_updates:
    text_message = msg['message']['text'].lower()
    user_id = msg['message']['from']['id']
    if text_message == '/btc':
      btc_course = 'Bitcoin = ' + str(get_btc()) + ' usd' 
      send_message(user_id, btc_course) 
    if text_message == '/eth':
        eth_course = 'Ethreum =' + str(get_eth()) + ' usd'
        send_message(user_id, eth_course)   
    if text_message == '/start': 
        send_message(user_id,"Welcome to the cryptocurrency bot! \b \n Push /start for information, /btc for bitcoin course, /eth for ethereum course.")

limit = 100
offset = 0

#whole bot cycle 
while True:
<<<<<<< HEAD
  for offset in 
=======
  for offset in get_bot_updates
>>>>>>> 9a1816ae037ce57ae9d01722248ddb578bff8aeb

  bot_updates = get_bot_updates(limit, offset)
  run_user_command(bot_updates)

#basic information
botId = 597179716
chatId = 56350945