import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import BOT_START_TIME, ADMINS
from utils import humanbytes  


@Client.on_message(filters.private & filters.command("status") & filters.user(ADMINS))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b><u>Bot Status</b></u>

⚡ Uᴘᴛɪᴍᴇ: <code>{currentTime}</code>
⚡ CPU Usᴀɢᴇ: <code>{cpu_usage}%</code>
⚡ RAM Usᴀɢᴇ: <code>{ram_usage}%</code>
⚡ Tᴏᴛᴀʟ Dɪsᴋ Sᴘᴀᴄᴇ: <code>{total}</code>
⚡ Usᴇᴅ Sᴘᴀᴄᴇ: <code>{used} ({disk_usage}%)</code>
⚡ Fʀᴇᴇ Sᴘᴀᴄᴇ: <code>{free}</code>
⚡ Tᴏᴛᴀʟ Bᴏᴛs: <code>18</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__Processing...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)
   
@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    try:
        await message.reply_document('BotLog.txt')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)



