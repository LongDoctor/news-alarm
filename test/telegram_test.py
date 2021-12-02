import telegram

telgm_token1 = '2022372478:AAEnCQ15sf9Cgtw-1e_BtS4I8aFMH9lzo5c'
chat_id = "1472478647"

bot = telegram.Bot(token = telgm_token1)

updates = bot.getUpdates()

# for u in updates :
#     print(u)
#     print(u.channel_post.sender_chat)
#     data = u.channel_post
#     if  data["text"]:
#         print("1")
#     else:
#         print("2")


bot.sendMessage(chat_id=chat_id, text="보낼 메세지")
# bot.sendMessage(chat_id = '1472478647', text="안녕하세요 GGCoding 채봇입니다.")
# https://api.telegram.org/bot2022372478:AAEnCQ15sf9Cgtw-1e_BtS4I8aFMH9lzo5c/getUpdates