import time
import json
import discord
from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from colorama import Fore, Style
import subprocess
import requests
import time
from os import system
from discord import Webhook, RequestsWebhookAdapter, Embed


h = open('message.txt','r',encoding='utf-8')
mes = h.read()





with open('config.json') as f:
    config = json.load(f)
    TOKEN = config.get('token')
    chaid1 = config.get('channel_id1')
    chaid2 = config.get('channel_id2')
    chaid3 = config.get('channel_id3')
    chaid4 = config.get('channel_id4')
    chaid5 = config.get('channel_id5')
    chaid6 = config.get('channel_id6')
    chaid7 = config.get('channel_id7')
    chaid8 = config.get('channel_id8')
    chaid9 = config.get('channel_id9')
    chaid10 = config.get('channel_id10')
    pmdelay = config.get('delay')
    status = config.get('status')
    pic = config.get('Picture')
    WhTF = config.get('Webhook True/False')
    whurl = config.get('WebhookUrl')

if WhTF == "True":
    webhook = Webhook.from_url(whurl, adapter=RequestsWebhookAdapter())
else:
    pass


def EZPRINT():
    system('cls')
    print(Fore.RED + """
    
        ███████╗██████╗ ███████╗███████╗██╗  ██╗    ██████╗ ██████╗  ██████╗ ███╗   ███╗ ██████╗ ████████╗███████╗
        ██╔════╝██╔══██╗██╔════╝██╔════╝██║  ██║    ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔═══██╗╚══██╔══╝██╔════╝
        █████╗  ██████╔╝█████╗  ███████╗███████║    ██████╔╝██████╔╝██║   ██║██╔████╔██║██║   ██║   ██║   █████╗  
        ██╔══╝  ██╔══██╗██╔══╝  ╚════██║██╔══██║    ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██║   ██║   ██║   ██╔══╝  
        ██║     ██║  ██║███████╗███████║██║  ██║    ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝


"""+ Style.RESET_ALL)

EZPRINT()
system("title " + f"Ez promote │ Dev By เกี้ยวซ่า#0001 │ discord.gg/freshshop")
print(f"""{Fore.BLUE}               [1] Last Promote │ [2] Last Promote Picture │ [3] Dm Promote │ [4] Delay Promote {Style.RESET_ALL}""")
choice = int(input(f"""{Fore.BLUE}
Type : """))
Style.RESET_ALL



if (choice == 1):
    system('cls')
    class MyClient(discord.Client):
        async def on_ready(self):
            activity = discord.Game(name=status)
            await self.change_presence(status=discord.Status.idle, activity=activity)
            system('cls')
            EZPRINT()
            print(f'{Fore.GREEN}Ready To Promote')
            print(Style.RESET_ALL)
            
        async def on_message(self,ctx):
            if ctx.channel.id == int(chaid1) or ctx.channel.id == int(chaid2) or ctx.channel.id == int(chaid3) or ctx.channel.id == int(chaid4) or ctx.channel.id == int(chaid5) or ctx.channel.id == int(chaid6) or ctx.channel.id == int(chaid7) or ctx.channel.id == int(chaid8) or ctx.channel.id == int(chaid9) or ctx.channel.id == int(chaid10):
                if ctx.content == "":
                    system("title " + f"Ez promote │ Dev By เกี้ยวซ่า#0001 │ Guild : {ctx.channel.name} │ Type : Last Promote │ Username : {self.user}")
                    await ctx.channel.send(mes)
                    print(f'Guild : {ctx.channel.name} │ Promoted')
                    if WhTF == "True":
                        embed = discord.Embed(title=f"Promoted │ Type Last Promote",color=0x1AF9C6)
                        embed.add_field(name=f"Promote To : {ctx.channel.name}", value=f'{mes}')
                        embed.set_footer(text = f'User Activity : {status}')
                        webhook.send(username="Fresh Promote", avatar_url="https://i.pinimg.com/736x/03/4b/de/034bde783ea726b922100c86547831e8.jpg",embed = embed)
                    else:
                        pass


    client = MyClient()
    client.run(TOKEN,bot = False)
elif (choice == 2):
    system('cls')
    class MyClient(discord.Client):
        async def on_ready(self):
            activity = discord.Game(name=status)
            await self.change_presence(status=discord.Status.idle, activity=activity)
            system('cls')
            EZPRINT()
            print(f'{Fore.GREEN}Ready To Promote')
            print(Style.RESET_ALL)
        
        async def on_message(self,ctx):
            if ctx.channel.id == int(chaid1) or ctx.channel.id == int(chaid2) or ctx.channel.id == int(chaid3) or ctx.channel.id == int(chaid4) or ctx.channel.id == int(chaid5) or ctx.channel.id == int(chaid6) or ctx.channel.id == int(chaid7) or ctx.channel.id == int(chaid8) or ctx.channel.id == int(chaid9) or ctx.channel.id == int(chaid10):         
                if ctx.content == "":
                    system("title " + f"Ez promote │ Dev By เกี้ยวซ่า#0001 │ Guild : {ctx.channel.name} │ Type : Last Promote │ Username : {self.user}")
                    await ctx.channel.send(mes,file=discord.File(pic))
                    print(f'Guild : {ctx.channel.name} │ Promoted')
                    if WhTF == "True":
                        embed = discord.Embed(title=f"Promoted │ Type Last Promote Picture",color=0x1AF9C6)
                        embed.add_field(name=f"Promote To : {ctx.channel.name}", value=f'{mes}')
                        embed.set_footer(text = f'User Activity : {status}')
                        webhook.send(username="Fresh Promote", avatar_url="https://i.pinimg.com/736x/03/4b/de/034bde783ea726b922100c86547831e8.jpg",embed = embed)
                    else:
                        pass

    client = MyClient()
    client.run(TOKEN,bot = False)
elif (choice == 3):
    system('cls')
    class MyClient(discord.Client):
        async def on_ready(self):
            system('cls')
            EZPRINT()
            print(f'{Fore.GREEN}Ready To Promote')
            print(Style.RESET_ALL)
            
        async def on_message(self,ctx):
            if ctx.channel.id == int(chaid1) or ctx.channel.id == int(chaid2) or ctx.channel.id == int(chaid3) or ctx.channel.id == int(chaid4) or ctx.channel.id == int(chaid5) or ctx.channel.id == int(chaid6) or ctx.channel.id == int(chaid7) or ctx.channel.id == int(chaid8) or ctx.channel.id == int(chaid9) or ctx.channel.id == int(chaid10):
                if ctx.content == "":
                    system("title " + f"Ez promote │ Dev By เกี้ยวซ่า#0001 │ Guild : {ctx.channel.name} │ Type : Dm Promote │ Username : {self.user}")
                    await ctx.author.send(mes)
                    print(f'Guild : {ctx.channel.name} │ Promoted to {ctx.author}')
                    if WhTF == "True":
                        embed = discord.Embed(title=f"Promoted │ Type Dm Promote",color=0x1AF9C6)
                        embed.add_field(name=f"Promote To :  {ctx.author}", value=f'{mes}')
                        embed.set_footer(text = f'User Activity : {status}')
                        webhook.send(username="Fresh Promote", avatar_url="https://i.pinimg.com/736x/03/4b/de/034bde783ea726b922100c86547831e8.jpg",embed = embed)
                    else:
                        pass
                        
    client = MyClient()
    client.run(TOKEN,bot = False)
elif choice == 4:
    total = 0
    def countdown(t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1





    def get_connection(): 
        return HTTPSConnection("discordapp.com", 443) 

    def send_message(conn, channel_id, message_data): 
        try: 
            conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
            resp = conn.getresponse() 
            
            if 199 < resp.status < 300: 
                print(f"[+] Promoted │ {total}") 
                pass 
    
            else: 
                stderr.write(f"[!] Error: {resp.reason}\n") 
                pass 
    
        except: 
            stderr.write("[!] Error\n") 
    
    def main(): 
        message_data = { 
            "content": mes, 
            "tts": "false", 
        }
    
        send_message(get_connection(), chaid1, dumps(message_data)) 


    system('cls')


    h = open('message.txt','r',encoding='utf-8')
    mes = h.read()


    for i in range(2):
        system('cls')
        time.sleep(0.2)
    EZPRINT()


    print(f"""
    Promote Every : {pmdelay} Seccond

    Message is :"""
    + Fore.GREEN+f"""
    {mes}""")
    print(Style.RESET_ALL)
    input("[!] Press Enter to continue")

    system('cls')

    header_data = { 
        "content-type": "application/json", 
        "user-agent": "discordapp.com", 
        "authorization": TOKEN, 
        "host": "discordapp.com"
    } 


    EZPRINT()
    
    

    for i in range(10000):
        total = int(total + 1)
        main()
        system("title " + f"Ez promote │ Dev By เกี้ยวซ่า#0001 │ Guild : {chaid1} │ Type : Delay Promote │ Promoted : {total}  ")
        countdown(int(pmdelay))