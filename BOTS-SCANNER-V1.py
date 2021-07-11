print("""


██████╗░░█████╗░████████╗░██████╗░░░░░░░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝░░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██████╦╝██║░░██║░░░██║░░░╚█████╗░█████╗╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██╔══██╗██║░░██║░░░██║░░░░╚═══██╗╚════╝░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝░░░██║░░░██████╔╝░░░░░░██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
""")
print("BY : @KRAKEN.OPS")
print("BOT-SCANNER-V1")

print("""###################################################################################################""")

x = input("Put the Name of txt file example (mybot) :")
print(" ")

with open(f"{x}.txt") as f:
    if 'discord' in f.read():
        print("FOUND (DISCORD URL)")
    elif "telegram" in f.read():
        print("FOUND (TELEGRAM BOT)")
    elif "pastebin" in f.read():
        print("FOUND SOMETHING (PASTEBIN URL)")
    elif "ngrok" in f.read():
        print("FOUND SOMTHING")
    elif "tcp" in f.read():
        print("FOUND A VIRUS")
    elif "raw" in f.read():
        print("FOUND SOMETHING")
    else:
        print("everything is ok")
