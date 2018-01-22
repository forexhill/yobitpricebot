import requests
import misc
# import json
from yobit import get_btc
from time import sleep

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0

# https://api.telegram.org/botTOKEN

def get_updates():
    url = URL + 'getupdates'
    # print(url)
    r = requests.get(url)
    # print(r)
    # print(r.json())

    return r.json()

def get_message():
    data = get_updates()

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:

        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                    'text': message_text}
        # print(message)
        return message

    return None

def send_message(chat_id, text='Wait a second pls...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    print(url)
    requests.get(url)


def main():
    # d = get_updates()
    # print(type(d))

    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)

    # get_message()

    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue
        sleep(2)





if __name__ == '__main__':
    main()
