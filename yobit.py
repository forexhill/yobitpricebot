import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    # response = requests.get(url).json()
    response = requests.get(url).content
    # price = response['ticker']['last']
    # return str(price) + ' usd'
    return response


get_btc()
