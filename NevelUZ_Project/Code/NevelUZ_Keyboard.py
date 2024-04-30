from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇺🇸 English")]
], resize_keyboard=True)
webapp = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Nнтерактивного меню", web_app=WebAppInfo(url="https://nevel.uz/elektrotovary-2"))]
])

product1_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product1"),
     InlineKeyboardButton(text="-", callback_data="remove_Product1")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product1"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product1")]
], resize_keyboard=True)

product2_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product2"),
     InlineKeyboardButton(text="-", callback_data="remove_Product2")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product2"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product2")]
], resize_keyboard=True)

product3_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product3"),
     InlineKeyboardButton(text="-", callback_data="remove_Product3")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product3"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product3")]
], resize_keyboard=True)

product4_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product4"),
     InlineKeyboardButton(text="-", callback_data="remove_Product4")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product4"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product4")]
], resize_keyboard=True)

product5_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product5"),
     InlineKeyboardButton(text="-", callback_data="remove_Product5")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product5"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product5")]
], resize_keyboard=True)

product6_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product6"),
     InlineKeyboardButton(text="-", callback_data="remove_Product6")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product6"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product6")]
], resize_keyboard=True)

product7_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product7"),
     InlineKeyboardButton(text="-", callback_data="remove_Product7")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product7"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product7")]
], resize_keyboard=True)

product8_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product8"),
     InlineKeyboardButton(text="-", callback_data="remove_Product8")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product8"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product8")]
], resize_keyboard=True)

product9_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product9"),
     InlineKeyboardButton(text="-", callback_data="remove_Product9")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product9"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product9")]
], resize_keyboard=True)

product10_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product10"),
     InlineKeyboardButton(text="-", callback_data="remove_Product10")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product10"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product10")]
], resize_keyboard=True)

product11_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product11"),
     InlineKeyboardButton(text="-", callback_data="remove_Product11")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product11"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product11")]
], resize_keyboard=True)

product12_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product12"),
     InlineKeyboardButton(text="-", callback_data="remove_Product12")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product12"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product12")]
], resize_keyboard=True)

product13_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product13"),
     InlineKeyboardButton(text="-", callback_data="remove_Product13")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product13"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product13")]
], resize_keyboard=True)

product14_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product14"),
     InlineKeyboardButton(text="-", callback_data="remove_Product14")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product14"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product14")]
], resize_keyboard=True)

product15_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product15"),
     InlineKeyboardButton(text="-", callback_data="remove_Product15")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product15"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product15")]
], resize_keyboard=True)

product16_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product16"),
     InlineKeyboardButton(text="-", callback_data="remove_Product16")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product16"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product16")]
], resize_keyboard=True)

product17_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product17"),
     InlineKeyboardButton(text="-", callback_data="remove_Product17")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product17"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product17")]
], resize_keyboard=True)

product18_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product18"),
     InlineKeyboardButton(text="-", callback_data="remove_Product18")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product18"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product18")]
], resize_keyboard=True)

product19_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product19"),
     InlineKeyboardButton(text="-", callback_data="remove_Product19")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product19"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product19")]
], resize_keyboard=True)

product20_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product20"),
     InlineKeyboardButton(text="-", callback_data="remove_Product20")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product20"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product20")]
], resize_keyboard=True)

product21_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product21"),
     InlineKeyboardButton(text="-", callback_data="remove_Product21")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product21"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product21")]
], resize_keyboard=True)

product22_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product22"),
     InlineKeyboardButton(text="-", callback_data="remove_Product22")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product22"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product22")]
], resize_keyboard=True)

product23_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product23"),
     InlineKeyboardButton(text="-", callback_data="remove_Product23")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product23"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product23")]
], resize_keyboard=True)

product24_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product24"),
     InlineKeyboardButton(text="-", callback_data="remove_Product24")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product24"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product24")]
], resize_keyboard=True)

product25_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product25"),
     InlineKeyboardButton(text="-", callback_data="remove_Product25")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product25"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product25")]
], resize_keyboard=True)

product26_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product26"),
     InlineKeyboardButton(text="-", callback_data="remove_Product26")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product26"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product26")]
], resize_keyboard=True)

product27_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product27"),
     InlineKeyboardButton(text="-", callback_data="remove_Product27")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product27"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product27")]
], resize_keyboard=True)

product28_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product28"),
     InlineKeyboardButton(text="-", callback_data="remove_Product28")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product28"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product28")]
], resize_keyboard=True)

product29_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product29"),
     InlineKeyboardButton(text="-", callback_data="remove_Product29")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product29"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product29")]
], resize_keyboard=True)

product30_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product30"),
     InlineKeyboardButton(text="-", callback_data="remove_Product30")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product30"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product30")]
], resize_keyboard=True)

product31_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product31"),
     InlineKeyboardButton(text="-", callback_data="remove_Product31")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product31"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product31")]
], resize_keyboard=True)

product32_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product32"),
     InlineKeyboardButton(text="-", callback_data="remove_Product32")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product32"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product32")]
], resize_keyboard=True)

product33_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product33"),
     InlineKeyboardButton(text="-", callback_data="remove_Product33")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product33"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product33")]
], resize_keyboard=True)

product34_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product34"),
     InlineKeyboardButton(text="-", callback_data="remove_Product34")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product34"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product34")]
], resize_keyboard=True)

product35_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product35"),
     InlineKeyboardButton(text="-", callback_data="remove_Product35")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product35"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product35")]
], resize_keyboard=True)

product36_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product36"),
     InlineKeyboardButton(text="-", callback_data="remove_Product36")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product36"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product36")]
], resize_keyboard=True)

product37_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product37"),
     InlineKeyboardButton(text="-", callback_data="remove_Product37")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product37"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product37")]
], resize_keyboard=True)

product38_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product38"),
     InlineKeyboardButton(text="-", callback_data="remove_Product38")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product38"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product38")]
], resize_keyboard=True)

product39_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product39"),
     InlineKeyboardButton(text="-", callback_data="remove_Product39")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product39"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product39")]
], resize_keyboard=True)

product40_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product40"),
     InlineKeyboardButton(text="-", callback_data="remove_Product40")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product40"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product40")]
], resize_keyboard=True)

product41_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product41"),
     InlineKeyboardButton(text="-", callback_data="remove_Product41")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product41"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product41")]
], resize_keyboard=True)

product42_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product42"),
     InlineKeyboardButton(text="-", callback_data="remove_Product42")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product42"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product42")]
], resize_keyboard=True)

product43_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product43"),
     InlineKeyboardButton(text="-", callback_data="remove_Product43")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product43"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product43")]
], resize_keyboard=True)

product44_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product44"),
     InlineKeyboardButton(text="-", callback_data="remove_Product44")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product44"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product44")]
], resize_keyboard=True)

product45_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product45"),
     InlineKeyboardButton(text="-", callback_data="remove_Product45")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product45"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product45")]
], resize_keyboard=True)

product46_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product46"),
     InlineKeyboardButton(text="-", callback_data="remove_Product46")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product46"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product46")]
], resize_keyboard=True)

product47_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product47"),
     InlineKeyboardButton(text="-", callback_data="remove_Product47")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product47"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product47")]
], resize_keyboard=True)

product48_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product48"),
     InlineKeyboardButton(text="-", callback_data="remove_Product48")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product48"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product48")]
], resize_keyboard=True)

product49_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product49"),
     InlineKeyboardButton(text="-", callback_data="remove_Product49")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product49"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product49")]
], resize_keyboard=True)

product50_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product50"),
     InlineKeyboardButton(text="-", callback_data="remove_Product50")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product50"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product50")]
], resize_keyboard=True)

product51_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product51"),
     InlineKeyboardButton(text="-", callback_data="remove_Product51")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product51"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product51")]
], resize_keyboard=True)

product52_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product52"),
     InlineKeyboardButton(text="-", callback_data="remove_Product52")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product52"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product52")]
], resize_keyboard=True)

product53_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product53"),
     InlineKeyboardButton(text="-", callback_data="remove_Product53")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product53"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product53")]
], resize_keyboard=True)

product54_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product54"),
     InlineKeyboardButton(text="-", callback_data="remove_Product54")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product54"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product54")]
], resize_keyboard=True)

product55_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product55"),
     InlineKeyboardButton(text="-", callback_data="remove_Product55")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product55"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product55")]
], resize_keyboard=True)

product56_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product56"),
     InlineKeyboardButton(text="-", callback_data="remove_Product56")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product56"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product56")]
], resize_keyboard=True)

product57_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product57"),
     InlineKeyboardButton(text="-", callback_data="remove_Product57")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product57"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product57")]
], resize_keyboard=True)

product58_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product58"),
     InlineKeyboardButton(text="-", callback_data="remove_Product58")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product58"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product58")]
], resize_keyboard=True)

product59_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product59"),
     InlineKeyboardButton(text="-", callback_data="remove_Product59")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product59"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product59")]
], resize_keyboard=True)

product60_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product60"),
     InlineKeyboardButton(text="-", callback_data="remove_Product60")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product60"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product60")]
], resize_keyboard=True)

product61_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product61"),
     InlineKeyboardButton(text="-", callback_data="remove_Product61")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product61"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product61")]
], resize_keyboard=True)

product62_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product62"),
     InlineKeyboardButton(text="-", callback_data="remove_Product62")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product62"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product62")]
], resize_keyboard=True)

product63_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product63"),
     InlineKeyboardButton(text="-", callback_data="remove_Product63")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product63"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product63")]
], resize_keyboard=True)

product64_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product64"),
     InlineKeyboardButton(text="-", callback_data="remove_Product64")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product64"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product64")]
], resize_keyboard=True)

product65_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product65"),
     InlineKeyboardButton(text="-", callback_data="remove_Product65")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product65"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product65")]
], resize_keyboard=True)

product66_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product66"),
     InlineKeyboardButton(text="-", callback_data="remove_Product66")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product66"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product66")]
], resize_keyboard=True)

product67_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product67"),
     InlineKeyboardButton(text="-", callback_data="remove_Product67")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product67"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product67")]
], resize_keyboard=True)

product68_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product68"),
     InlineKeyboardButton(text="-", callback_data="remove_Product68")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product68"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product68")]
], resize_keyboard=True)

product69_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="add_Product69"),
     InlineKeyboardButton(text="-", callback_data="remove_Product69")],
    [InlineKeyboardButton(text="Избранные ❤️", callback_data="add_Favorites_Product69"),
     InlineKeyboardButton(text="Корзина 🛍", callback_data="add_Basket_Product69")]
], resize_keyboard=True)

# Русский
home_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог товаров 🗂"), KeyboardButton(text="Корзина 🛍")],
    [KeyboardButton(text="Избранные ❤️")],
    [KeyboardButton(text="Настройки ⚙️")]
], resize_keyboard=True)

delivery_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Доставка 🚚")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

payment_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Наличные 💵"), KeyboardButton(text="Payme 💳")],
    [KeyboardButton(text="Click 💳")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

location_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Мой локация 📍", request_location=True)]
], resize_keyboard=True)

cash_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Отменить ❌"), KeyboardButton(text="Подтвердить ✅")],
    [KeyboardButton(text="Изменить 🔄")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

payme_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Отменить ❌"), KeyboardButton(text="Подтвердить ✅")],
    [KeyboardButton(text="Изменить 🔄")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

click_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Отменить ❌"), KeyboardButton(text="Подтвердить ✅")],
    [KeyboardButton(text="Изменить 🔄")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

settings_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🇷🇺🇸🇱 Изменить язык"), KeyboardButton(text="🚪 Выйти")],
    [KeyboardButton(text="Добавить продукт")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

catalog_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Инструменты"), KeyboardButton(text="Электротовары")],
    [KeyboardButton(text="Пневмооборудование")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

electrical_goods_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматические выключатели модульные")],
    [KeyboardButton(text="Автоматический ввод резерва (АВР)")],
    #  KeyboardButton(text="Электромагнитный клапан")],
    # [KeyboardButton(text="Вентиляторы охлаждения")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

cooling_fans = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Вентиляторы и кулеры"), KeyboardButton(text="Решетки для кулера")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

fans_coolers = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Вентилятор охлаждения FP20060 AC220/240V")],
    [KeyboardButton(text="Вентилятор охлаждения FP-108 AC220/240V")],
    [KeyboardButton(text="Вентилятор охлаждения DS1751ABNL AC220/240V")],
    [KeyboardButton(text="Вентилятор охлаждения JQH 2123HSL AC220/240V")],
    [KeyboardButton(text="Вентилятор охлаждения SF8025AT AC220/240V")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

cooler_grilles = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Решетка для вентиляции XT-807 420х180")],
    [KeyboardButton(text="Решетка для вентиляции XT-804 204х204")],
    [KeyboardButton(text="Решетка для вентиляции XT-803 148х148")],
    [KeyboardButton(text="Решетка для вентиляции XT-801 116x116")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

avr = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический ввод резерва АВР XLDS-125/4P 100A")],
    [KeyboardButton(text="Автоматический ввод резерва АВР XLDS-250/4P 250A")],
    [KeyboardButton(text="Автоматический ввод резерва АВР XLDS-630/4P 630A")],
    [KeyboardButton(text="Автоматический ввод резерва АВР XLDS-1000/4P 1000A")],
    [KeyboardButton(text="Автоматический ввод резерва АВР XLDS-1600/4P 1600A")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

electro_clapn = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Электрический клапан US-15E2 220VAС")],
    [KeyboardButton(text="Электромагнитный клапан 50мм 220V.")],
    [KeyboardButton(text="Электрический клапан SLG5404-15E2 220VAC")],
    [KeyboardButton(text="Электромагнитный клапан 40мм 220V.")],
    [KeyboardButton(text="Электромагнитный клапан 32мм 220V")],
    [KeyboardButton(text="Электромагнитный клапан 25мм 220V")],
    [KeyboardButton(text="Катушка на электромагнитный клапан 220VAC/24VDC")],
    [KeyboardButton(text="Электромагнитный клапан 20мм 220V")],
    [KeyboardButton(text="Электромагнитный клапан 15мм 220V.")],
    [KeyboardButton(text="Электромагнитный клапан 10мм 220V")],
    [KeyboardButton(text="Электромагнитный клапан 8мм 220V.")],
    [KeyboardButton(text="Электромагнитный клапан 6мм 220V.")],
    [KeyboardButton(text="Катушка на электромагнитный клапан 220VAC/24VDC")],
    [KeyboardButton(text='⬅️ Назад')]
], reply_markup=True)

firma = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="CHINT"), KeyboardButton(text="CNC")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

chint_and_cnc = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1P-CHINT"), KeyboardButton(text="2P-CHINT"), KeyboardButton(text="3P-CHINT")],
    # [KeyboardButton(text="1P-CNC"), KeyboardButton(text="2P-CNC"), KeyboardButton(text="3P-CNC")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

chint_1p = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 1A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 2A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 3A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 4A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 6A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 10A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 16A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 25A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 32A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 40A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 50A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 1P 63A 6кА х-ка С")],
    [KeyboardButton(text='⬅️ Назад')]
], reply_markup=True)

chint_2p = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 2A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 4A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 6A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 10A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 16A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 25A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 32A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 40A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 50A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 2P 63A 6кА х-ка С")],
    [KeyboardButton(text='⬅️ Назад')]
], reply_markup=True)

chint_3p = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 2A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 4A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 6A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 10A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 16A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 25A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 32A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 40A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 50A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель NXB-63 3P 63A 6кА х-ка С")],
    [KeyboardButton(text='⬅️ Назад')]
], reply_markup=True)

cnc_1p = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 1A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 2A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 4A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 6A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 10A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 16A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 20A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 25A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 32A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 40A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 50A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 1P 63A 6кА х-ка С")],
    [KeyboardButton(text='⬅️ Назад')]
])

cnc_2p = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 2A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 6A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 10A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 16A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 25A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 32A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 40A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 50A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 2P 63A 6кА х-ка С")],
    [KeyboardButton(text='⬅️ Назад')]
])

cnc_3p = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 2A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 6A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 10A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 16A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 25A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 32A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 40A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 50A 6кА х-ка С")],
    [KeyboardButton(text="Автоматический выключатель YCB6-63H 3P 63A 6кА х-ка С")],
    [KeyboardButton(text='⬅️ Назад')]
])

tool_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пресс-клещи для втулочных наконечников"),
     KeyboardButton(text="Пресс-клещи для изолированных наконечников")],
    [KeyboardButton(text='Прессы механические'), KeyboardButton(text="Прессы гидравлические")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

pneumatic_equipment_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Гидрораспределитель"), KeyboardButton(text="Пневматический Пистолет")],
    [KeyboardButton(text="Регуляторы давления воздуха")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

hydraulic_distributor_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Гидрораспределитель DSG-3C2-02"),
     KeyboardButton(text="Гидрораспределитель DSG-03-3C2-AC220V")],
    [KeyboardButton(text="Гидрораспределитель DSG-02-3C4-DL-D24"),
     KeyboardButton(text="Гидрораспределитель 4W6D-50/AW220NZ5L")],
    [KeyboardButton(text="Гидрораспределитель DSG-02-2B60B 24VDC")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

air_gun_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пневматический пистолет (мет) DG-10"),
     KeyboardButton(text="Пневматический пистолет PAG-07")],
    [KeyboardButton(text="Пневматический пистолет PAG-02")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)
air_pressure_regulators_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Реле давления HEP110")],
    [KeyboardButton(text="Регулятор давления QTYH-15 40 бар 1/2")],
    [KeyboardButton(text="Регулятор давления FRC-D/AOU-1/4-MINI с фильтром")],
    [KeyboardButton(text="Регулятор давления LFR-D/AOFR- 1/4-MINI")],
    [KeyboardButton(text="Регулятор давления LR-D/AOR -1/2-MIDI Без фильтра")],
    [KeyboardButton(text="Регулятор давления LR-D/AOR - 1/4-MINI Без фильтра")],
    [KeyboardButton(text="Регулятор давления AC 2010-02")],
    [KeyboardButton(text="Блок подготовки воздуха с регулятором давления BFC-4000")],
    [KeyboardButton(text="Блок подготовки воздуха с регулятором давления AFC-2000")],
    [KeyboardButton(text="Фильтр влаготделитель с регулятором давления BFR-4000")],
    [KeyboardButton(text="Фильтр влаготделитель с регулятором давления AFR-2000")],
    [KeyboardButton(text="Регулятор давления с манометром BR-4000")],
    [KeyboardButton(text="Регулятор давления с манометром AR-2000")],
    [KeyboardButton(text='⬅️ Назад')]
])
mexanik_prass_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пресс механический HX-50B (6-50mm)"),
     KeyboardButton(text="Инструмент HT-2008R (обжим коннекторов RJ-45, RJ-11 / 12 с фикс.)")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

prass1_product_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пресс-клещи VSC9 10-6A"), KeyboardButton(text="Пресс-клещи VSC9 16-4A")],
    [KeyboardButton(text="Пресс-клещи VSC8 6-6A"), KeyboardButton(text="Пресс-клещи VSC8 6-4A")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

prass2_product_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пресс-клещи VSB-30J"), KeyboardButton(text="Пресс-клещи VSA-02C")],
    [KeyboardButton(text="Пресс-клещи VSA-06WF")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

gidrav_press_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пресс гидравлический ручной YQK-300A (16-300mm)")],
    [KeyboardButton(text="Пресс гидравлический ручной YQK-240A (16-240mm)")],
    [KeyboardButton(text='⬅️ Назад')]
], resize_keyboard=True)

# O'zbekcha
home_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Katalog 🗂"), KeyboardButton(text="Savat 🛍")],
    [KeyboardButton(text="Sevimlilar ❤️")],
    [KeyboardButton(text="Sozlamalar ⚙️")]
], resize_keyboard=True)

catalog_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Asboblar"), KeyboardButton(text="Elektr buyumlari"),
     KeyboardButton(text="Pnevmatik uskunalar")],
    [KeyboardButton(text='⬅️ Orqaga')]
], resize_keyboard=True)

tool_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Press-klesh vtulochniy nakonechniklar uchun"),
     KeyboardButton(text="Press-klesh izolirovanniy nakonechniklar uchun")],
    [KeyboardButton(text='Mexanik presslar'), KeyboardButton(text="Gidravlik presslar")],
    [KeyboardButton(text='⬅️ Orqaga')]
], resize_keyboard=True)

prass_product_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="VSC9 10-6A press pensesi"), KeyboardButton(text="VSC9 16-4A press pensesi")],
    [KeyboardButton(text="VSC8 6-6A press pensesi"), KeyboardButton(text="VSC8 6-4A press pensesi")],
    [KeyboardButton(text='PZ 1,5-6 mm2'), KeyboardButton(text="PZ 0,25-2,5")],
    [KeyboardButton(text='⬅️ Orqaga')]
], resize_keyboard=True)

# English
home_en = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Catalog 🗂"), KeyboardButton(text="Basket 🛍")],
    [KeyboardButton(text="Favorites ❤️")],
    [KeyboardButton(text="Settings ⚙️")]
], resize_keyboard=True)

catalog_en = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Tools"), KeyboardButton(text="Electrical goods"),
     KeyboardButton(text="Pneumatic equipment")],
    [KeyboardButton(text='⬅️ Back')]
], resize_keyboard=True)

tool_en = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Press pliers for ferrules"), KeyboardButton(text="Press jaws for insulated tips")],
    [KeyboardButton(text='Mechanical presses'), KeyboardButton(text="Hydraulic presses")],
    [KeyboardButton(text='⬅️ Back')]
], resize_keyboard=True)

prass_product_en = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Press pliers VSC9 10-6A"), KeyboardButton(text="Press pliers VSC9 16-4A")],
    [KeyboardButton(text="Press pliers VSC8 6-6A"), KeyboardButton(text="Press pliers VSC8 6-4A")],
    [KeyboardButton(text='Press jaws PZ 1.5-6 mm2'), KeyboardButton(text="Press jaws PZ 0.25-2.5")],
    [KeyboardButton(text='⬅️ Back')]
], resize_keyboard=True)
