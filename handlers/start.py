import os

from pyrogram import Client, filters # Ik this is weird as this shit is already imported in line 6! anyway ... Fuck Off!
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat

from helpers.filters import command, other_filters, other_filters2
from helpers.database import db, Database
from helpers.dbthings import handle_user_status
from config import LOG_CHANNEL, BOT_USERNAME, UPDATES_CHANNEL

@Client.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/start":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**ð¢ News ** \n#New_Music_Lover **Started To Using Me!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )      
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention} ð¤ !</b>
        
<b>I'm  Yakari 2.O version  Music Bot! A Powerful Bot to Play Music in Your Group Voice Chat ð! </b>

<b>Also I have more features! Please hit on **/help** to see them ð¨âð» !</b>

<b>Made byâ¤ï¸</b> **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð  Add Me To Your Group â", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð   Help Menu ð ", callback_data="cbhelpmenu"
                    ),
                    InlineKeyboardButton(
                        "â Support group ð¦", url="https://t.me/KicchaRequest"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ð¬ Support Channel ", url="https://t.me/AnikhaX_Music2"
                    )
                ]
            ]
        )
    )

    
# Help Menu

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]))
async def help(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/help":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**ð¢ News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention} ðï¸!</b>

**<b>Here is the Help Menu For This Bot ð! </b>**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "âï¸ How To Use Me âï¸", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "âï¸  Get Lyrics ", callback_data="cbgetlyrics"
                    ),
                    InlineKeyboardButton(
                        "ð YT Search", callback_data="cbytsearch"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¥ Music Downloader ", callback_data="cbmusicdown"
                    ),
                    InlineKeyboardButton(
                        "ð  YT Video Downloader", callback_data="cbytviddown"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð  Delete Commands", callback_data="cbdelcmds"
                    ),
                    InlineKeyboardButton(
                        "ð§° Quotely", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("credits") & other_filters2)
async def credits2(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/credits":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**ð¢ News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_sticker("CAACAgEAAxkBAAJ8LGD_g_8YHC71w0gzRJxhhKL23XZaAAIjCQAC43gEAAGfWaD2uhnQOSAE")        
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ð¤!</b>

Special Thanks ð For all of first code owners ð</b> !

â Credits To,

<b>1ï¸â£ <a href="https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA">sl geek show youtube </a></b> -  (â¤ï¸) !
<b>2ï¸â£ Left-TG |ã åä¹ï¾ï¾ ä¹ã®ï½²ä¸ ã</b> - (First code owner â¤ï¸)
<b>3ï¸â£ N.M.Dinura Uthsara Nikalansuriya</b> - ( Heroku supporterð¨âð»)
<b>4ï¸â£ AbirHasan2005</b>
<b>5ï¸â£ DevsExpo</b>
<b>6ï¸â£ TeamDaisyX</b>
<b>7ï¸â£ Vivek-Tp</b>- ( Fsub & more help â¤ï¸â¤ï¸)

Made  â¤ï¸ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¬ Support Group", url="https://t.me/KicchaRequest"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )   


@Client.on_message(command(["vc", f"vc@{BOT_USERNAME}"]) & other_filters)
async def vc(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/vc":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**ð¢ News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    VC_LINK = f"https://t.me/{message.chat.username}?voicechat"
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} ðï¸!</b>


             ð§  **Voice Chat Link** ð§
____________________------------______________________

ðï¸ [Here Is Your Voice Chat Linkð¸ ](https://t.me/{message.chat.username}?voicechat) ðï¸
____________________------------______________________

Enjoy â¤ï¸!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð­ Share Voice Chat Invitation ð­ ", url=f"https://t.me/share/url?url=**Join%20Our%20Group%20Voice%20Chat%20ð%20%20{VC_LINK}%20â¤ï¸**"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð  My Update Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ð¬ Support Group", url="https://t.me/KicchaRequest"
                    )
                ]
            ]
        ),
        disable_web_page_preview=True
    )

    
@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def search(_, message: Message):
    usr_cmd = message.text.split("_")[-1]
    if usr_cmd == "/search":
        chat_id = message.chat.id
        if not await db.is_user_exist(chat_id):
            await db.add_user(chat_id)
            await Client.send_message(
        chat_id=LOG_CHANNEL,
        text=f"**ð¢ News ** \n#New_Music_Lover **Started To Using Meh!** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nProfile Link: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
        parse_mode="markdown"
    )
    await message.reply_text(
        "ðð»ââï¸ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Yeah", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Nope â", callback_data="close"
                    )
                ]
            ]
        )
    )
