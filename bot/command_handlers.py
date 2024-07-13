from aiogram import Router, F
import asyncio
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message,InputMediaPhoto
from aiogram.filters import CommandStart, Command, StateFilter
from external_functions import show_slide_show
from postgres_functions import (insert_new_user_in_table,
                                check_user_in_table,
                                insert_text_in_msg,
                                insert_data_in_kadr,
                                return_msg, reset_msg,
                                return_base, return_kadr, reset_kadr,
                                insert_data_in_base, reset_base, return_bookmarks)
from pagination import pagin_dict, menu_foto
from keyboards import pre_start_clava, menu_clava, inline_kb
from aiogram.fsm.context import FSMContext
import json
from bot_instance import bot
from filters import PRE_START
from lexicon import *
from FSM import FSM_ST
from bookmark_kb import create_bookmarks_keyboard

ch_router = Router()

@ch_router.message(~F.text)
async def delete_not_text_type_messages(message: Message):
    await message.delete()


@ch_router.message(CommandStart())
async def process_start_command(message: Message,  state: FSMContext):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    if not await check_user_in_table(user_id):
        await insert_new_user_in_table(user_id, user_name)
        await state.set_state(FSM_ST.slide)
        first_antwort = await message.answer(text=f'<b>{user_name}</b>, '
                                                  f'Willkommen im Bot des Hochzeitsfotografen '
                                                  f'Georgij Shugol',
                                             reply_markup=menu_clava)
        json_first = first_antwort.model_dump_json(exclude_none=True)
        await insert_text_in_msg(user_id, json_first)
        first_foto_atw = await message.answer_photo(pagin_dict[1])
        json_att = first_foto_atw.model_dump_json(exclude_none=True)
        await insert_data_in_kadr(user_id, json_att)
        await show_slide_show(first_foto_atw)
    else:
        await message.delete()



@ch_router.message(PRE_START())
async def before_start(message: Message):
    prestart_ant = await message.answer(text='Klicken <b>start</b> !',
                                        reply_markup=pre_start_clava)
    await message.delete()
    await asyncio.sleep(6)
    await prestart_ant.delete()

@ch_router.message(Command(commands='help'), ~StateFilter(FSM_ST.waiting))
async def process_help_command(message: Message):
    print('help works')
    att = await message.answer(help_answer)
    await message.delete()
    await asyncio.sleep(10)
    await att.delete()


@ch_router.message(Command('menu'), ~StateFilter(FSM_ST.waiting))
async def process_menu_command(message: Message, state:FSMContext):
    await message.delete()
    await state.set_state(FSM_ST.general)
    user_id = message.from_user.id
    data = await return_msg(user_id)
    if data != '':
        print('data = ', data, type(data))
        return_to_message = Message(**json.loads(data))
        info_msg = Message.model_validate(return_to_message).as_(bot)
        await info_msg.delete()
        await reset_msg(user_id)


    second_data = await return_base(user_id)
    print('second_data = ', second_data)
    first_foto_atw = await message.answer_photo(photo=menu_foto,
                                                reply_markup=inline_kb)

    third_data = await return_kadr(user_id)
    if third_data != '':
        print('3data')
        return_to_message = Message(**json.loads(third_data))
        del_msg = Message.model_validate(return_to_message).as_(bot)
        await del_msg.delete()
        await reset_kadr(user_id)
    js_first_foto_atw = first_foto_atw.model_dump_json(exclude_none=True)
    await insert_data_in_base(user_id, js_first_foto_atw)



@ch_router.message(Command('back'), ~StateFilter(FSM_ST.waiting))
async def process_back_command(message: Message, state:FSMContext):
    await state.set_state(FSM_ST.general)
    user_id = message.from_user.id
    del_report_msg = await return_base(user_id)
    return_to_message = Message(**json.loads(del_report_msg))
    msg = Message.model_validate(return_to_message).as_(bot)
    await message.delete()
    await msg.delete()

    kadr_data = await return_kadr(user_id)
    if kadr_data != '':
        return_to_message = Message(**json.loads(kadr_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_kadr(user_id)

    first_foto_atw = await message.answer_photo(photo=menu_foto,
                                                reply_markup=inline_kb)
    js_first_foto_atw = first_foto_atw.model_dump_json(exclude_none=True)
    await insert_data_in_base(user_id, js_first_foto_atw)
    msg_data = await return_msg(user_id)
    if msg_data != '':
        return_to_message = Message(**json.loads(msg_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_msg(user_id)


@ch_router.message(Command(commands='slide_show'), ~StateFilter(FSM_ST.waiting))
async def process_command_slide_show(message: Message, state:FSMContext):
    user_id = message.from_user.id
    await state.set_state(FSM_ST.show)
    await message.delete()
    att = await message.answer('Um zurückzukehren, klicken Sie auf die Menüschaltfläche',
                               reply_markup=menu_clava)
    js_att = att.model_dump_json(exclude_none=True)
    base_data = await return_base(user_id)
    if base_data != '':
        return_to_message = Message(**json.loads(base_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_base(user_id)
    msg_data = await return_msg(user_id)
    if msg_data != '':
        return_to_message = Message(**json.loads(msg_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_msg(user_id)

    await insert_text_in_msg(user_id, js_att)
    kadr_data = await return_kadr(user_id)
    if kadr_data != '':
        return_to_message = Message(**json.loads(kadr_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_kadr(user_id)

    first_foto_atw = await message.answer_photo(pagin_dict[1])
    json_att = first_foto_atw.model_dump_json(exclude_none=True)
    await insert_data_in_kadr(user_id, json_att)
    await show_slide_show(first_foto_atw)


@ch_router.message(Command(commands='kontakt'), StateFilter(FSM_ST.general, FSM_ST.slide))
async def go_to_kontakt(message:Message):
    user_id = message.from_user.id
    await message.delete()
    kadr_data = await return_kadr(user_id)
    if kadr_data != '':
        return_to_message = Message(**json.loads(kadr_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_kadr(user_id)

    msg_data = await return_msg(user_id)
    if msg_data != '':
        return_to_message = Message(**json.loads(msg_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()
        await reset_msg(user_id)

    base_data = await return_base(user_id)
    if base_data != '':
        return_to_message = Message(**json.loads(base_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        await msg.delete()

    try:
        await message.edit_media(
            media=InputMediaPhoto(
                media='AgACAgIAAxkBAAIC-WaNVEr7BJjtbZ4FRZ4szxLPT3qJAAJd3zEb3B5xSOVGm3eFQvajAQADAgADeQADNQQ',
            caption=kontakt_capture),
            reply_markup=None)
    except TelegramBadRequest:
        print('go to Kontact into Exeption')
        contact_foto_atw = await message.answer_photo(
            'AgACAgIAAxkBAAIC-WaNVEr7BJjtbZ4FRZ4szxLPT3qJAAJd3zEb3B5xSOVGm3eFQvajAQADAgADeQADNQQ',
            caption=kontakt_capture,
            reply_markup=None)
        js_contact_foto_atw = contact_foto_atw.model_dump_json(exclude_none=True)
        await insert_data_in_base(user_id, js_contact_foto_atw)

@ch_router.message(Command(commands='kontaktiere'), StateFilter(FSM_ST.general))
async def process_send_massage_to_bot(message: Message):
    print('process_send_massage_to_bot\n ')
    att = await message.answer(text=text_for_kontakt)
    await asyncio.sleep(10)
    await message.delete()
    await att.delete()



@ch_router.message(StateFilter(FSM_ST.general))
async def process_send_otzyv(message: Message, state: FSMContext):
    print('feed_back sending\n ')
    await state.set_state(FSM_ST.waiting)
    sending_data = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    join_text = f'User_id {user_id}, user_name  {user_name} \n\nsend MESSAGE \n\n{sending_data}'
    await message.bot.send_message(chat_id=-4263539640, text=join_text)
    await asyncio.sleep(1)
    await message.delete()
    att = await message.answer(success_send)
    await asyncio.sleep(3)
    await att.delete()
    wait_att = await message.answer(waiting_15)
    await asyncio.sleep(3)
    await asyncio.sleep(150)
    await wait_att.delete()
    await state.set_state(FSM_ST.general)

@ch_router.message(StateFilter(FSM_ST.waiting))
async def process_waiting(message: Message):
    att = await message.answer(just_waitng)
    await asyncio.sleep(3)
    await message.delete()
    await att.delete()


@ch_router.message(Command(commands='bookmarks'), StateFilter(FSM_ST.slide))
async def process_bookmarks_command(message: Message):
    user_id = message.from_user.id
    print('process_bookmarks_command works')
    msg_data = await return_msg(user_id)
    if msg_data != '':
        return_to_message = Message(**json.loads(msg_data))
        msg = Message.model_validate(return_to_message).as_(bot)
        try :
            await msg.delete()
            await reset_msg(user_id)
        except TelegramBadRequest:
            pass

    bm_data = await return_bookmarks(user_id)
    if bm_data:
        await message.answer(
            text=bookmark_list,
            reply_markup=create_bookmarks_keyboard(*bm_data))
        js_bm_atw = bm_data.model_dump_json(exclude_none=True)
        await insert_text_in_msg(user_id, js_bm_atw)
    else:
        no_bookmark = await message.answer(text=no_bookmarks)
        await asyncio.sleep(4)
        await no_bookmark.delete()
    await message.delete()

