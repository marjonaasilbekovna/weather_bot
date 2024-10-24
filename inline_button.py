from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_country = {
    "navoi": "Navoi",
    "tashkent": "Tashkent",
    "samarkand": "Samarkand",
    "jizzakh": "Jizzakh",
    "fergana": "Fergana",
    "bukhara": "Bukhara",
    "namangan": "Namangan",
    "andijan": "Andijan",
    "zarafshan": "Zarafshan",
    "urgench": "Urgench",
    "khiva": "Khiva",
    "sirdaryo": "Sirdaryo",
    "nukus": "Nukus",
    "termiz": "Termiz"
}

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Navoi", callback_data="navoi"), 
            InlineKeyboardButton(text="Tashkent", callback_data="tashkent")
        ],
        [
            InlineKeyboardButton(text="Samarkand", callback_data="samarkand"), 
            InlineKeyboardButton(text="Jizzakh", callback_data="jizzakh")
        ],
        [
            InlineKeyboardButton(text="Fergana", callback_data="fergana"),
            InlineKeyboardButton(text="Bukhara", callback_data="bukhara")           
        ],
        [
            InlineKeyboardButton(text="Namangan", callback_data="namangan"),
            InlineKeyboardButton(text="Andijan", callback_data="andijan")
        ],
        [
            InlineKeyboardButton(text="Zarafshan", callback_data="zarafshan"),
            InlineKeyboardButton(text="Urgench", callback_data="urgench")
        ],
        [
            InlineKeyboardButton(text="Khiva", callback_data="khiva"),
            InlineKeyboardButton(text="Sirdaryo", callback_data="sirdaryo")
        ],
        [
            InlineKeyboardButton(text="Termiz", callback_data="termiz"),
            InlineKeyboardButton(text="Nukus", callback_data="nukus")
        ]
    ]
)

surov = {
    "ha": "Ha ✅",
    "yoq": "Yo'q ❌"
}
surov_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha ✅", callback_data="ha"), 
            InlineKeyboardButton(text="Yo'q ❌", callback_data="yoq")
        ]
    ]
)

qayta = {
    "start": "Start"
}

qayta_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Start", callback_data="start")
        ]
    ]
)