import os, ast

from pyrogram.emoji import *
from pyrogram.errors import UserBannedInChannel, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client as kinu6, filters
from ..tools.text import TEXT
from ..config import Config
from ..plugins.commands import *
import logging
logger = logging.getLogger(__name__)


@kinu6.on_callback_query()
async def cb_handler(client, query):
    ## Callback For Home ##
    if query.data=='back':
        await query.answer()
        keyboard= InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Help", callback_data="help_data"),
                ],
                [
                    InlineKeyboardButton("Close", callback_data="close_data")

                ]
            ]
        )
        
        await query.message.edit_text(
            text=TEXT.START_TEXT.format(
            user_mention=query.from_user.mention),
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return
    
    elif query.data=='help_data':
        ## CallBack For Help ##
        await query.answer()
        keyboard= InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Home', callback_data='back'),
                ],
                [
                    InlineKeyboardButton("Close", callback_data="close_data")
                ]
            ]
        )
        
        await query.message.edit_text(
            text=TEXT.HELP_USER.format(query.from_user.first_name),
            reply_markup=keyboard,
            disable_web_page_preview=True
        )
        return

    
    elif query.data == 'close_data':
        ## CallBack For Close
        await query.message.delete()
