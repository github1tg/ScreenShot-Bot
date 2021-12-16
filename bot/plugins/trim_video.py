from pyrogram import filters
from pyrogram.types import ForceReply

from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("trim"))
)
async def _(c, m):
    await m.answer()
    dur = m.message.text.markdown.split("\n")[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f"#trim_video\n{dur}\n\n┈••┈••✿••✿••✿••✿••✿••✿••┈••┈\n\n𝙽𝚘𝚠 𝚜𝚎𝚗𝚍 𝚢𝚘𝚞𝚛 𝚜𝚝𝚊𝚛𝚝 𝚊𝚗𝚍 𝚎𝚗𝚍 𝚜𝚎𝚌𝚘𝚗𝚍𝚜 𝚒𝚗 𝚝𝚑𝚎 𝚐𝚒𝚟𝚎𝚗 𝚏𝚘𝚛𝚖𝚊𝚝 𝚊𝚗𝚍 𝚜𝚑𝚘𝚞𝚕𝚍 "
        f"𝚋𝚎 𝚞𝚙𝚝𝚘 {Config.MAX_TRIM_DURATION}s.\t**𝕤𝕥𝕒𝕣𝕥\t:\t𝕖𝕟𝕕**\n\nEɢ: 𝟺𝟶𝟶:𝟻𝟶𝟶 ==> Tʜɪs ᴛʀɪᴍs ᴠɪᴅᴇᴏ ғʀᴏᴍ 𝟺𝟶𝟶s ᴛᴏ 𝟻𝟶𝟶s",
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply(),
    )
