import telegram

telgm_token1 = '1958129912:AAFLQ0pn56FhI_fpyJCl8-opWQx6xpn2XOU'

bot = telegram.Bot(token = telgm_token1)

updates = bot.getUpdates()

for u in updates :
    print(u)
    print(u.channel_post.sender_chat)
    data = u.channel_post
    if  data["text"]:
        print("1")
    else:
        print("2")

# bot.sendMessage(chat_id = '1472478647', text="안녕하세요 GGCoding 채봇입니다.")