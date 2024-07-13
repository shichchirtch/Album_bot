from aiogram.exceptions import TelegramBadRequest
from asyncio import sleep
from pagination import pagin_dict
from aiogram.types import InputMediaPhoto
from random import shuffle


async def show_slide_show(kadr):
    counter = 0
    d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
         24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
    shuffle(d)
    arr = d
    while counter < 30:
        counter += 1
        for page in arr:
            try:
                await sleep(2.4)
                await kadr.edit_media(
                    media=InputMediaPhoto(media=pagin_dict[page]
                                          ))
                print('*******')
            except TelegramBadRequest:
                print('Into Exeption SLide func')
                break
    return

# async def edit_repeat_text_window(message:Message):
#     """Эта асинхронная функция редактирует открытую прежде страницу, если юзер нажал
#     на какую нибудь кнопку создающее новое окно, а не редактирующее старое с текстом"""
#     print("edit FUNC WORKS")
#     user_id = message.from_user.id
#     current_index = users_db[message.from_user.id]['page']
#     last_message = users_db[user_id]['base']  # получаю его
#     print('type last_message = ', type(last_message))
#     return_to_message = Message(**json.loads(last_message))
#     print('type return_to_message = ', type(return_to_message), '\n\n', return_to_message)
#     msg = Message.model_validate(return_to_message).as_(bot)
#     print('msg = ', msg)
#
#     att = await msg.edit_media(
#         media=InputMediaPhoto(
#             media=pagin_dict[current_index][0], caption=pagin_dict[current_index][1]),
#         reply_markup=create_pagination_keyboard(current_index))
#     str_att = att.model_dump_json(exclude_none=True)
#     print(str_att)
#     users_db[user_id]['base'].append(str_att)



