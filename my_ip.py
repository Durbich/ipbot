import requests

def gimme():
    myip = requests.get('https://api.ipify.org/?format=json').json()['ip']
    return myip

def help():
    return "Тебе нужно подключится через SSH. Чтобы скопировать файлы используй SCP. Для винды есть SSH-клиент PuTTY, с ним идёт PSCP (для копипасты). Короткой статьи в нэте хватит, чтоб разобраться как это использовать. Чтоб прочитать файл без скачивания - используй vim. В качестве файлового менеджера есть mc. Если вдруг поменялся IP - напиши мне 'ip'. Порт поменятся не должен (322). Удачи"