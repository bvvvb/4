from telebot import types, TeleBot
import requests
import random
import threading
import time
from user_agent import generate_user_agent

hits = 0
bad = 0
errors = 0
total = 0
token = input("[#] Enter Token : ")
bot = TeleBot(token, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == "st":
        bot.send_message(call.message.chat.id, "wait ...")
        Tik(call.message)
    elif call.data == "kill":
        bot.send_message(call.message.chat.id, "is stopped")
        bot.stop()

def Tik(message):
    def mahos(user):
        global hits, bad, errors
        headers = {
            "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": generate_user_agent(),
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
        }
        tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=headers)
        if tikinfo.status_code == 200:
            try:
                getting = tikinfo.text.split('webapp.user-detail"')[1].split('"RecommendUserList"')[0]
                id = getting.split('id":"')[1].split('",')[0]
                followers = getting.split('followerCount":')[1].split(',"')[0]
                following = getting.split('followingCount":')[1].split(',"')[0]
                bad += 1
                hh = f'''

                bad user : [{bad}]
                checked : {user}
                id : {id}
                followers : {followers}
                following : {following}
                '''
                print(hh)
            except (KeyError, IndexError):
                hits += 1
                msg = f'''
New Clime !! [{hits}]
user climed : {user} 
After : {hits}{hits}{hits}'''
                print(msg)
                bot.reply_to(message, msg)
        else:
            errors += 1
            print('erorr')

    def randomusers():
        global total
        while True:
            v1 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
            v2 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
            v3 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
            v4 = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(1))
            v5 = ''.join(random.choice('._') for i in range(1))
            v6 = ''.join(random.choice('_') for i in range(1))
            user1 = v6 + v1 + v2 + v3
            user2 = v1 + v2 + v3 + v4
            user3 = v2 + v5 + v3 + v4
            user4 = v2 + v3 + v5 + v4
            user5 = v1 + v5 + v6 + v2
            user6 = v1 + v5 + v2
            user7 = v1 + v2
            user8 = v1 + v2 + v3
            user9 = v5 + v1 + v1
            user10 = v5 + v2 + v3
            user11 = v1 + v1 + v1 + v2
            user12 = v1 + v2 + v1 + v2
            user13 = v1 + v1 + v2 + v2
            user14 = v1 + v5 + v1
            ahmed = (user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14)
            user = random.choice(ahmed)
            total += 1
            mahos(user)

    Threads = []
    for _ in range(1):
        t = threading.Thread(target=randomusers)
        t.start()
        Threads.append(t)
    for thread in Threads:
        thread.join()
@bot.message_handler(commands=['start'])
def start(message):
    hits = 0
    bad = 0
    errors = 0
    total = 0
    mes = types.InlineKeyboardMarkup(row_width=2)
    but2 = types.InlineKeyboardButton(text="- run", callback_data='st')    
    but3 = types.InlineKeyboardButton(f"- stop : ", callback_data='kill')
    mes.add(but2, but3)
    bot.send_message(message.chat.id, '''cHecker uSer TikTok !''', reply_markup=mes)

print('Done')
bot.polling()