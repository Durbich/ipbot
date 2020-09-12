from API import API
import logic
import my_ip
"""Этот чорт всем управляет"""

print('start')

bot = API()
bot.get_long_poll('full')

print('ready to work')

while True:
    update = bot.listen_LP()
    if update[0] == 'good':
        for obj in update[1]:
            if obj['type'] == 'message_new':
                graal = obj['object']['message']
                conclusion = logic.analyse(graal)
                if conclusion[0] == "ignore": pass
                elif conclusion[0] == "vk": bot.exe(conclusion[1])
                elif conclusion[0] == "database": pass
                else : print("illogical answer")
    if update[0] == 'err':
        if update[1] == "update":
            bot.get_long_poll('ts')
        if update[1] == "relogin": # ключ от LP - временный
            bot.get_long_poll('key')
            print('LP key changed')
        if update[1] == "full":
            bot.get_long_poll('full')