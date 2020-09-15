from configparser import ConfigParser
import requests
import json
import identity
# Этот модуль делает запросы к ВК и больше ничего


class API:
    
    def __init__(self):   
        cfg = ConfigParser()
        cfg.read("config.ini")
        self.HOME = cfg["API"]["HOME"]
        self.VER = cfg["API"]["VER"]
        self.WAIT = int(cfg["API"]["WAIT"])
        self.GROUP_ID = cfg["GROUP"]["ID"]
        self.TOKEN = cfg["GROUP"]["TOKEN"]
        self.TAIL = f"&v={self.VER}&access_token={self.TOKEN}"
        self.lp_err = 0

    def get_long_poll(self, reason):
        while True:
            try:
                lp = requests.get(f"{self.HOME}groups.getLongPollServer?group_id={self.GROUP_ID}{self.TAIL}", timeout = self.WAIT).json()["response"]
            except TimeoutError:
                print('-- catch LP timeout --')
            except ConnectionError:
                print('-- catch connect error --')
            except ConnectionAbortedError:
                print('-- connection aborted --')
            else:
                break # Ток после успешного подключения выйдет из цикла (сделано против Таймаута или если сеть присела)
        if reason == 'full':
            self.lp_server = lp["server"]
        if reason == 'full' or reason == 'key':
            self.lp_key = lp["key"]
        if reason == 'full' or reason == 'ts':
            self.lp_ts = lp["ts"]
    
    def listen_LP(self):
        question = f"{self.lp_server}?act=a_check&key={self.lp_key}&ts={self.lp_ts}&wait={self.WAIT}"
        lp_answer = requests.get(question, timeout = self.WAIT + 2).json()
        # lp_answer = json.loads(answer)
        try:
            self.lp_ts = lp_answer["ts"]
            return ('good', lp_answer["updates"])
        except:
            try:
                if 'failed' in lp_answer:
                    if lp_answer['failed'] == 1:
                        return ('err', 'update')
                    if lp_answer['failed'] == 2:
                        return ('err', 'relogin')
                    if lp_answer['failed'] == 3:
                        return ('err', 'full')
            except TimeoutError:
                print('-- Listen LP timeout --')
                return ('err', 'relogin')
            except ConnectionError:
                print('-- Listen LP connect error --')
                return ('err', 'relogin')
            except ConnectionAbortedError:
                print('-- Listen LP connection aborted --')
                return ('err', 'relogin')
    
    def exe(self, order):
        full_order = self.HOME + order + self.TAIL
        try:
            answer = requests.get(full_order, timeout = self.WAIT).content.decode('utf-8')
        except:
            print ('ERR CONNECT')
        else:
            if 'error' in answer:
                edit = json.loads(answer)
                edit['request'] = str(f"{self.HOME}{order}&{self.VER}")
                with open (f"errors/{identity.unique('report')}.json",'w') as f:
                    f.write(str(json.dumps(edit)))