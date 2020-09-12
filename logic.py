import my_ip
import identity
# Этот модуль анализирует входящие сообщения

def analyse(msg):
    if msg['peer_id'] == 163206068 or msg['peer_id'] == 203688551:
        kudablyat = msg['peer_id']
        if msg["text"].lower() == 'ip':
            myip = my_ip.gimme()
            return ("vk" ,f"messages.send?peer_id={kudablyat}&message={myip}&random_id={identity.unique('r_id')}")
        if msg["text"].lower() == "help":
            return ("vk" ,f"messages.send?peer_id={kudablyat}&message={my_ip.help()}&random_id={identity.unique('r_id')}")
        else: return ("ignore",)
    else: return ("ignore",)