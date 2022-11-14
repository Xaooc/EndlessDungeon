from aiogram import F, Router, Bot
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER
from aiogram.types import ChatMemberUpdated

router = Router()
router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))

chats_variants = {
    "group": "группу",
    "supergroup": "супергруппу"
}



@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> MEMBER
    )
)
async def bot_added_as_member(event: ChatMemberUpdated, bot: Bot):
    # Вариант посложнее: бота добавили как обычного участника.
    # Но может отсутствовать право написания сообщений, поэтому заранее проверим.
    chat_info = await bot.get_chat(event.chat.id)
    if chat_info.permissions.can_send_messages:
        await bot.send_message(
            chat_id=event.chat.id,
            text='Вижу, хотите посоревноваться в походах в Dungeons?\n'
                 'Тогда создавайте своих персонажей командой /new\n'
                 'Отправляйте в подземелье командой /go\n'
                 'Почитать подробнее о боте командой /info'
        )
    else:
        print("не удалось отправить сообщение")