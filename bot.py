#requests import
import requests

#basic information
file = open('./boturl.txt')
url = file.read()
limit = 5
offset = 0
timeout = 2

#getting bitcoin course
def get_btc(): 
  url_btc = "https://api.cryptonator.com/api/ticker/btc-usd" 
  result_btc = requests.get(url_btc)
  decoded = result_btc.json()
  return decoded['ticker']['price']

#getting etherium course
def get_eth(): 
  url_eth = "https://api.cryptonator.com/api/ticker/eth-usd" 
  result_eth = requests.get(url_eth)
  decoded = result_eth.json()
  return decoded['ticker']['price']

def get_ltc(): 
  url_ltc = "https://api.cryptonator.com/api/ticker/ltc-usd" 
  result_ltc = requests.get(url_ltc)
  decoded = result_ltc.json()
  return decoded['ticker']['price']

#getting all updates
def get_bot_updates(limit, offset, timeout):
  method = url + "getUpdates" 
  params = {'limit': limit, 'offset': offset, 'timeout': timeout}
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

  #getting message text and user id
  for msg in bot_updates:
    if 'message' in msg:
      text_message = msg['message']['text']
      user_id = msg['message']['from']['id']
    else: 
      text_message = msg['edited_message']['text']
      user_id = msg['edited_message']['from']['id']

    #running user command
    if text_message == '/btc':
      btc_course = 'Bitcoin = ' + str(get_btc()) + ' usd'
      send_message(user_id, btc_course) 
    if text_message == '/eth':
      eth_course = 'Ethreum =' + str(get_eth()) + ' usd'
      send_message(user_id, eth_course) 
    if text_message == '/ltc':
      ltc_course = 'Litecoin =' + str(get_ltc()) + ' usd'
      send_message(user_id, ltc_course) 
    if text_message == '/pew':
      pew_course = 'There is no need for insults, dear! \n Please invest only such an amount that you can loose!'
      send_message(user_id, pew_course) 
    if text_message == '/start': 
      send_message(user_id,"Welcome to the cryptocurrency bot! \n Push /start for information, \n /btc for Bitcoin course, \n /eth for Ethereum course, \n /ltc for Litecoin course.")
  return



#whole bot cycle 
while True: 
  bot_updates = get_bot_updates(limit, offset, timeout)
  if bot_updates: 
    offset = bot_updates[-1]['update_id'] + 1
    run_user_command(bot_updates)