from bot_base import session_marker, User
from sqlalchemy import select

async def insert_new_user_in_table(user_tg_id: int, name: str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        if not needed_data:
            print('Now we are into first function')
            new_us = User(tg_us_id=user_tg_id, user_name=name)
            session.add(new_us)
            await session.commit()

async def check_user_in_table(user_tg_id:int):
    """Функция проверяет есть ли юзер в БД"""
    async with session_marker() as session:
        print("Work check_user Function")
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        data = query.one_or_none()
        return data

async def insert_text_in_msg(user_id:int, text_msg:str):
    '''Функция вставляет текстовое сообщение в БД'''
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('insert_text_in_msg')
        needed_data.msg = text_msg
        await session.commit()


async def insert_data_in_kadr(user_id:int, kadr_data:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('insert_data_in_kadr')
        needed_data.kadr = kadr_data
        await session.commit()

async def insert_data_in_base(user_id:int, base_data:str):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('insert_data_in_kadr')
        needed_data.base = base_data
        await session.commit()

async def return_msg(user_id):
    async with session_marker() as session:
        print("Works return_msg Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        text_msg = needed_data.msg
        return text_msg

async def reset_msg(user_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('reset_msg works')
        needed_data.msg = ''
        await session.commit()

async def reset_kadr(user_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('reset_kadr works')
        needed_data.kadr = ''
        await session.commit()

async def reset_base(user_id:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('reset_base works')
        needed_data.base = ''
        await session.commit()

async def return_base(user_id):
    async with session_marker() as session:
        print("Works return_base Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        base_msg = needed_data.base
        return base_msg

async def return_kadr(user_id):
    async with session_marker() as session:
        print("Works return_kadr Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        kadr_msg = needed_data.kadr
        return kadr_msg

async def return_bookmarks(user_id):
    async with session_marker() as session:
        print("Works return_base Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        bookmarks = needed_data.bookmarks
        return bookmarks

async def set_pages(user_id:int, page_index:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('insert_data_in_kadr')
        needed_data.page = page_index
        await session.commit()

async def page_listai(user_id:int, schift:int):
    async with session_marker() as session:
        print("Work page_moving Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        print('data = ', needed_data)
        needed_data.page +=schift
        await session.commit()

async def return_page_index(user_id:int):
    async with session_marker() as session:
        print("Works return_base Func")
        query = await session.execute(select(User).filter(User.tg_us_id == user_id))
        needed_data = query.scalar()
        page_index = needed_data.page
        return page_index


async def add_new_bookmark(user_tg_id: int, adding_page:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('add_new_bookmarks works')
        bookmark_list = needed_data.bookmarks
        new_list = bookmark_list+[adding_page]
        needed_data.bookmarks = new_list
        await session.commit()

async def del_bookmarck(user_tg_id: int, delete_page:int):
    async with session_marker() as session:
        query = await session.execute(select(User).filter(User.tg_us_id == user_tg_id))
        needed_data = query.scalar()
        print('del_bookmarks works')
        bookmark_list = needed_data.bookmarks
        temp_arr = []
        for x in bookmark_list:
            if x != delete_page:
                temp_arr.append(x)
        needed_data.bookmarks = temp_arr
        await session.commit()


