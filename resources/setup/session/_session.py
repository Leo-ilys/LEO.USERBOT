# Leo - Userbot
# 𝐋𝐄𝐎 𝐒𝐎𝐔𝐑𝐂𝐄 - 𝐒𝐓𝐑𝐈𝐍𝐆-𝐒𝐄𝐒𝐒𝐈𝐎𝐍
# Owner ~ @QHR_1

from telethon.sessions import StringSession as ss
from telethon.sync import TelegramClient as tc

print("𓆩 SOURCE LEO -  STRING SESSION 𓆪")
print("")

APP_ID = int(input("⌔∮ ENTER APP ID HERE - "))
API_HASH = input("⌔∮ ENTER API HASH HERE - ")

with tc(ss(), APP_ID, API_HASH) as client:
    ics = client.send_message("me", client.session.save())
    ics.reply("⌔∮ هذا هو كود التيرمكس الخاص بك.\n⌔∮ المطور - @QHR_1. ")
    print("")
    print("")
    print(
        "⌔∮ Below is the STRING_SESSION. You can also find it in your Telegram Saved Messages."
    )
    print("")
    print("")
    print(client.session.save())
