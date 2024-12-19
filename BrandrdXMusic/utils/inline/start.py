from pyrogram.types import InlineKeyboardButton

import config
from BrandrdXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source")
        ],
        [InlineKeyboardButton("waifu", callback_data='waifu')],
    ]
    return buttons

    waifu = """
    ***❖ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs sᴇᴄᴛɪᴏɴ ❖***
    
***⬤ /guess ➥ ᴛᴏ ɢᴜᴇss ᴄʜᴀʀᴀᴄᴛᴇʀ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ).***
***⬤ /fav ➥ ᴀᴅᴅ ʏᴏᴜʀ ғᴀᴠʀᴀᴛᴇ.***
***⬤ /trade ➥ ᴛᴏ ᴛʀᴀᴅᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs.***
***⬤ /gift ➥ ɢɪᴠᴇ ᴀɴʏ ᴄʜᴀʀᴀᴄᴛᴇʀ ғʀᴏᴍ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs).***
***⬤ /collection ➥ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ.***
***⬤ /topgroups ➥ sᴇᴇ ᴛᴏᴘ ɢʀᴏᴜᴘs, ᴘᴘʟ ɢᴜᴇssᴇs ᴍᴏsᴛ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘs.***
***⬤ /top ➥ ᴛᴏᴏ sᴇᴇ ᴛᴏᴘ ᴜsᴇʀs.***
***⬤ /ctop ➥ ʏᴏᴜʀ ᴄʜᴀᴛ ᴛᴏᴘ.***
***⬤ /changetime ➥ ᴄʜᴀɴɢᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ᴀᴘᴘᴇᴀʀ ᴛɪᴍᴇ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs).***
   """
