from aiogram import F, Router
from filters import *
import asyncio
from pagination import pagin_dict, reportagen
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from aiogram.exceptions import TelegramBadRequest
from keyboards import *
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from inline_keyboard import create_pagination_keyboard
from bookmark_kb import create_edit_keyboard
from external_functions import show_slide_show
from postgres_functions import (set_pages, insert_data_in_kadr, page_listai,
                                return_page_index, return_base,
                                insert_data_in_base, insert_text_in_msg,
                                reset_base, return_bookmarks, add_new_bookmark,
                                return_kadr, del_bookmarck, return_msg, reset_msg)
from lexicon import *
from bot_instance import bot
import json
from FSM import FSM_ST
cb_router = Router()

@cb_router.callback_query(PORT_FILTER())
async def go_to_port(callback: CallbackQuery, state:FSMContext):
    await state.set_state(FSM_ST.slide)
    user_id = callback.from_user.id
    msg_data = await return_msg(user_id)
    if msg_data != '':
        return_to_message = Message(**json.loads(msg_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_msg(user_id)

    page_index = 2
    await set_pages(user_id, page_index)
    try:
        att = await callback.message.edit_media(
            media=InputMediaPhoto(
                media=pagin_dict[page_index]),
            reply_markup=pagination_keyboard)
        if await return_kadr(user_id) != '':
            json_att = att.model_dump_json(exclude_none=True)
            await insert_data_in_kadr(user_id, json_att)
    except TelegramBadRequest:
        print('go to port into Exeption')
    await callback.answer()

@cb_router.callback_query(MOVE_PAGE(), StateFilter(FSM_ST.slide))
async def portfolio_page_moving(callback: CallbackQuery):
    print(f'{callback.data = }')
    shift = -1 if callback.data == 'backward' else 1
    user_id = callback.from_user.id
    await page_listai(user_id, shift)
    pagin_index = await return_page_index(user_id)
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=pagin_dict[pagin_index]),
            reply_markup=create_pagination_keyboard(pagin_index)
        )
    except TelegramBadRequest:
        print('Into Exeption')
    await callback.answer()



@cb_router.callback_query(REPORT_FILTER(), StateFilter(FSM_ST.general))
async def go_to_reportagen(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media=reportagen[0]),
            reply_markup=reportagen_keyboard)
    except TelegramBadRequest:
        print('go to REPOR into Exeption')
    await callback.answer()

@cb_router.callback_query(SIX_FILTER(), StateFilter(FSM_ST.general))
async def go_into_reportagen(callback: CallbackQuery):

    user_id = callback.from_user.id
    last_message = await return_base(user_id)
    return_to_message = Message(**json.loads(last_message))
    msg = Message.model_validate(return_to_message).as_(bot)
    if callback.data == 'Trier':
        data = await msg.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC0GaNSycoDDPCt6tO4Ph5svVs3vYrAAIl3zEb3B5xSPGg2CfWya7rAQADAgADeQADNQQ',
            ), reply_markup=trier_kb)
        json_att = data.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, json_att)

    elif callback.data == 'Bornheim':
        data = await msg.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC0maNSz5RnGT7CIbAcOL25pgKA7sNAAIm3zEb3B5xSEBxdidk6hrDAQADAgADeQADNQQ', ),
            reply_markup=bornheim_kb)
        json_att = data.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, json_att)

    elif callback.data == 'Bamberg':
        data = await msg.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC1GaNTDWPqO9Ivu3G-3wZrz5dlZpcAAIr3zEb3B5xSPVqrzfIG6BvAQADAgADeQADNQQ'),
            reply_markup=bamberg_kb)
        json_att = data.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, json_att)

    elif callback.data == 'Kleeburg':
        data = await msg.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC1maNTTrBV5srJ9FZ3zPJ4vLoeoaeAAIx3zEb3B5xSGYMCsH0-mhOAQADAgADeQADNQQ'),
            reply_markup=kleeburg_kb)
        json_att = data.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, json_att)

    elif callback.data == 'Kastanienhof':
        data = await msg.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC2GaNTamWZrwm06RnzwKVL5MEgOzkAAIy3zEb3B5xSDOCY8d3y-V3AQADAgADeQADNQQ'),
            reply_markup=koeln_kb)
        json_att = data.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, json_att)

    elif callback.data == 'Juchen':
        data = await msg.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC2maNTjK8FsW0iPO5pC4K9VOW0zEEAAI33zEb3B5xSA6sLkZytxfeAQADAgADeQADNQQ'),
            reply_markup=juechen_kb)
        json_att = data.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, json_att)
    await callback.answer()


@cb_router.callback_query(KONTAKT_FILTER(), StateFilter(FSM_ST.general))
async def go_to_kontakt(callback: CallbackQuery):
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC-WaNVEr7BJjtbZ4FRZ4szxLPT3qJAAJd3zEb3B5xSOVGm3eFQvajAQADAgADeQADNQQ',
            caption=kontakt_capture),
            reply_markup=None)
    except TelegramBadRequest:
        print('go to Kontact into Exeption')
        contact_foto_atw = await callback.message.answer_photo(
            'AgACAgIAAxkBAAIC-WaNVEr7BJjtbZ4FRZ4szxLPT3qJAAJd3zEb3B5xSOVGm3eFQvajAQADAgADeQADNQQ',
            caption=kontakt_capture,
            reply_markup=None)
        js_contact_foto_atw = contact_foto_atw.model_dump_json(exclude_none=True)
        user_id = callback.from_user.id
        last_msg = await return_base(user_id)
        return_to_message = Message(**json.loads(last_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await insert_data_in_base(user_id, js_contact_foto_atw)

    await callback.answer()

@cb_router.callback_query(FAQ_FILTER())
async def go_to_faq(callback: CallbackQuery, state:FSMContext):
    user_id = callback.from_user.id
    jetzt_state = await state.get_state()
    if jetzt_state == 'FSM_ST:text_mess':
        faq_msg = await return_msg(user_id)
        return_to_message = Message(**json.loads(faq_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        try:
            await msg.edit_text(text=faq, reply_markup=None)
        except TelegramBadRequest:
            faq_msg = await callback.message.answer(text=faq, reply_markup=None)
            text_msg = faq_msg.model_dump_json(exclude_none=True)
            await insert_text_in_msg(user_id, text_msg)
            await msg.delete()
    else:
        faq_msg = await callback.message.answer(text=faq, reply_markup=None)
        text_msg = faq_msg.model_dump_json(exclude_none=True)
        await insert_text_in_msg(user_id, text_msg)

    await state.set_state(FSM_ST.text_mess)
    await callback.answer()

@cb_router.callback_query(PREISE_FILTER())
async def go_to_preise(callback: CallbackQuery, state:FSMContext):
    user_id = callback.from_user.id
    jetzt_state = await state.get_state()
    if jetzt_state == 'FSM_ST:text_mess':
        prise_msg = await return_msg(user_id)
        return_to_message = Message(**json.loads(prise_msg))
        msg = Message.model_validate(return_to_message).as_(bot)
        try:
            await msg.edit_text(text=preise, reply_markup=None)
        except TelegramBadRequest:
            prise_msg = await callback.message.answer(text=preise, reply_markup=None)
            text_msg = prise_msg.model_dump_json(exclude_none=True)
            await insert_text_in_msg(user_id, text_msg)
            await msg.delete()
    else:
        prise_msg = await callback.message.answer(text=preise, reply_markup=None)
        text_msg = prise_msg.model_dump_json(exclude_none=True)
        await insert_text_in_msg(user_id, text_msg)

    await state.set_state(FSM_ST.text_mess)
    await callback.answer()

@cb_router.callback_query(SLIDE_FILTER(), StateFilter(FSM_ST.general))
async def show_sleiden(callback: CallbackQuery, state:FSMContext):
    user_id = callback.from_user.id
    await state.set_state(FSM_ST.show)
    print('we are into sleiden handler')
    slide_ant = await callback.message.answer(text='Drücken Sie Menü, um den Vorgang zu beenden',
                                  reply_markup=menu_clava)
    text_msg = slide_ant.model_dump_json(exclude_none=True)
    await insert_text_in_msg(user_id, text_msg)

    first_foto_atw = await callback.message.answer_photo(pagin_dict[1])
    json_att = first_foto_atw.model_dump_json(exclude_none=True)
    await insert_data_in_kadr(user_id, json_att)

    del_menu_msg = await return_base(user_id)
    return_to_message = Message(**json.loads(del_menu_msg))
    msg = Message.model_validate(return_to_message).as_(bot)
    await msg.delete()
    await reset_base(user_id)
    await show_slide_show(first_foto_atw)
    # await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером текущей страницы и добавлять текущую страницу в закладки
@cb_router.callback_query(ADD_BM_FILTER(), StateFilter(FSM_ST.slide))
async def process_page_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    print('calback add bm works')
    bm_list = await return_bookmarks(user_id)
    current_page = await return_page_index(user_id)
    if (len(bm_list)< 11 and current_page not in bm_list):
        await add_new_bookmark(user_id, current_page)
        await callback.answer(bookmark_add)
    else:
        att = await callback.message.answer(bookmark_10)
        await asyncio.sleep(3)
        await att.delete()


@cb_router.callback_query(IS_DIGIT_CALLBACK_DATA(), StateFilter(FSM_ST.slide))
async def process_bookmark_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    await set_pages(user_id, int(callback.data))

    current_index = int(callback.data)

    last_message = await return_kadr(user_id)
    return_to_message = Message(**json.loads(last_message))
    msg = Message.model_validate(return_to_message).as_(bot)
    try:
        att = await msg.edit_media(
            media=InputMediaPhoto(
                media=pagin_dict[current_index]),
            reply_markup=create_pagination_keyboard(current_index))
        str_att = att.model_dump_json(exclude_none=True)
        await insert_data_in_kadr(user_id, str_att)
    except TelegramBadRequest:
        print('Into Exeption')
        await insert_data_in_kadr(user_id, last_message)
    await callback.message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "редактировать" под списком закладок
@cb_router.callback_query(F.data == 'edit_bookmarks', StateFilter(FSM_ST.slide))
async def process_edit_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    bm_list = await return_bookmarks(user_id)
    await callback.message.edit_text(
        text=edit_bookmarks,
        reply_markup=create_edit_keyboard(*bm_list))
    await callback.answer()
    # await callback.message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "отменить" во время работы со списком закладок (просмотр и редактирование)
@cb_router.callback_query(F.data == 'cancel', StateFilter(FSM_ST.slide))
async def process_cancel_press(callback: CallbackQuery):
    print('process_cancel_press works ')
    await callback.message.delete()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок к удалению
@cb_router.callback_query(IS_DEL_BUCKMARK(), StateFilter(FSM_ST.slide))
async def process_del_bookmark_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    print('callback.data[:-3] = ', callback.data[:-3])
    #  Интересно поглядеть, как это реализован в Постгрессе
    del_page_index = int(callback.data[:-3])
    await del_bookmarck(user_id, del_page_index)
    bm_list = await return_bookmarks(user_id)

    if bm_list:
        await (
            callback.message.edit_text(
                text=bookmark_list,
                reply_markup=create_edit_keyboard(*bm_list)))
    else:
        no_marks_respond = await callback.message.edit_text(text=no_bookmarks)
        await asyncio.sleep(2)
        await no_marks_respond.delete()
        await reset_msg(user_id)
    await callback.answer()


@cb_router.message()
async def send_echo(message: Message):
    print("Works send_echo")
    if message.text == "/bookmarks":
        att = await message.answer('Um Ihre Lesezeichen anzuzeigen, gehen Sie zum Portfolio')
        await asyncio.sleep(3)
        await att.delete()
        await message.delete()

    elif message.text =='/kontactiere':
        att = await message.answer(', gehen Sie zum Portfolio')
        await asyncio.sleep(3)
        await att.delete()
        await message.delete()

    else:
        att = await message.answer(text=echo)
        await asyncio.sleep(7)
        await message.delete()
        await att.delete()




