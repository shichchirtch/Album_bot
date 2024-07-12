from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
from config import settings

using_redis = Redis(host=settings.REDIS_HOST)
redis_storage = RedisStorage(redis=using_redis)



class FSM_ST(StatesGroup):
    general = State()
    waiting = State()
    slide = State()
    text_mess = State()
