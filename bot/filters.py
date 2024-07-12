from aiogram.types import CallbackQuery, Message
from aiogram.filters import BaseFilter
from postgres_functions import check_user_in_table


class MOVE_PAGE(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('forward', 'backward'):
            return True
        return False


class PORT_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'portfolio':
            return True
        return False


class REPORT_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'reportagen':
            return True
        return False


class SIX_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data in ('Trier', 'Bornheim', 'Bamberg', 'Kleeburg', 'Kastanienhof', 'Juchen'):
            return True
        return False


class KONTAKT_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'kontakt':
            return True
        return False


class FAQ_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'faq':
            return True
        return False


class PREISE_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'info':
            return True
        return False


class SLIDE_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'sleiden':
            return True
        return False


class PRE_START(BaseFilter):
    async def __call__(self, message: Message):
        print("PRE_START Filter works")
        user_tg_id = message.from_user.id
        if await check_user_in_table(user_tg_id):
            return False
        return True


class ADD_BM_FILTER(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data == 'mark':
            return True
        return False


class IS_DIGIT_CALLBACK_DATA(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()


class IS_DEL_BUCKMARK(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        print('Works IS_DEL_BUCKMARK')
        return callback.data.endswith('del') and callback.data[:-3].isdigit()
