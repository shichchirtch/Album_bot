from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

pre_start_button = KeyboardButton(text='/start')
menu_button = KeyboardButton(text='/menu')

pre_start_clava = ReplyKeyboardMarkup(
    keyboard=[[pre_start_button]],
    resize_keyboard=True,
    input_field_placeholder='Приятного чтения'
)

menu_clava = ReplyKeyboardMarkup(
    keyboard=[[menu_button]],
    resize_keyboard=True,
    input_field_placeholder='into menu')

portfolio = InlineKeyboardButton(text=f'Portfolio', callback_data='portfolio')
hochzeitreportagen = InlineKeyboardButton(text=f'Hochzeitreportagen', callback_data='reportagen')
info = InlineKeyboardButton(text=f'Info', callback_data='info')
kontakt = InlineKeyboardButton(text=f'Kontakt', callback_data='kontakt')
faq = InlineKeyboardButton(text=f'FAQ', callback_data='faq')
slide_show = InlineKeyboardButton(text=f'Sleiden', callback_data='sleiden')

inline_kb = InlineKeyboardMarkup(
            inline_keyboard= [[portfolio],[hochzeitreportagen],[info],[kontakt],[faq],[slide_show]])

forward_button = InlineKeyboardButton(text=f'>>', callback_data='forward')
backward_button = InlineKeyboardButton(text='<<', callback_data='backward')

pagination_keyboard = InlineKeyboardMarkup(
            inline_keyboard= [[backward_button,forward_button]])

#####################################################################################################

in_trier = InlineKeyboardButton(text=f'Hochzeit in Trier mit Jackie und Simon', callback_data='Trier')
in_bornheim = InlineKeyboardButton(text=f'Faschinghochzeit in Bornheim mit Carsten und Kerstin', callback_data='Bornheim')
in_bamberg = InlineKeyboardButton(text=f'Grosse Vietnamesche Hochzeit in Bamberg', callback_data='Bamberg')
in_kleeburg = InlineKeyboardButton(text=f'Hochzeit im Schloss Kleeburg mit Mark und Simone', callback_data='Kleeburg')
in_kastanienhof = InlineKeyboardButton(text=f'Hochzeit im Kastanienhof mit Sabrina und Thomas', callback_data='Kastanienhof')
in_juchen = InlineKeyboardButton(text=f'Hochzeit auf Schloss Dyck in Jüchen mit Anna und Kai', callback_data='Juchen')


reportagen_keyboard=InlineKeyboardMarkup(
            inline_keyboard= [[in_trier],[in_bornheim],[in_bamberg],[in_kleeburg],[in_kastanienhof],[in_juchen]])

##############################################################################################################

trier = InlineKeyboardButton(text=f'Hochzeit in Trier', url="https://telegra.ph/Hochzeit-in-Trier-mit-Jackie-und-Simon-07-08")

trier_kb = InlineKeyboardMarkup( inline_keyboard= [[trier]])

bornheim = InlineKeyboardButton(text=f'Faschinghochzeit in Bornheim', url="https://shugol.com/hochzeit-in-bornheim/")

bornheim_kb = InlineKeyboardMarkup( inline_keyboard= [[bornheim]])

bamberg = InlineKeyboardButton(text=f'Vietnamesische Hochzeit', url="https://shugol.com/vietnamesische-hochzeit-in-bamberg/")

bamberg_kb = InlineKeyboardMarkup( inline_keyboard= [[bamberg]])

kleeburg = InlineKeyboardButton(text=f'Hochzeit im Schloss', url="https://shugol.com/hochzeit-im-schloss-kleeburg-euskirchen/")

kleeburg_kb = InlineKeyboardMarkup( inline_keyboard= [[kleeburg]])

koeln = InlineKeyboardButton(text=f'Hochzeit im Kastanienhof', url="https://shugol.com/hochzeit-kastanienhof-koeln/")

koeln_kb = InlineKeyboardMarkup( inline_keyboard= [[koeln]])

juechen = InlineKeyboardButton(text=f'Hochzeit in Jüchen', url="https://shugol.com/hochzeit-auf-schloss-dyck-in-juechen-mit-anna-und-kai/")

juechen_kb = InlineKeyboardMarkup( inline_keyboard= [[juechen]])