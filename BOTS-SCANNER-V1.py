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
print(" ")
print("Put the Bot here and press enter :")

lines = []
while True:
    line = str(input())
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
x = str(text)
words = ["discord","pastebin","telegram"]
if "discord" in x:
    print("[!] Found Discord bot")
elif "telegram" in x:
    print("[!] Found Telegram bot")
elif "tcp" in x:
    print("[!] Found Virus")
elif "pastebin" in x:
    print("[!] Found pastebin url")
elif "raw" in x:
    print("[!] Found raw text")
else :
    print("everything is ok")
