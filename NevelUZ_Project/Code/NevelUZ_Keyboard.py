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
],resize_keyboard=True)

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
    [KeyboardButton(text="Реле давления HEP110"), KeyboardButton(text="Регулятор давления QTYH-15 40 бар 1/2")],
    [KeyboardButton(text="Регулятор давления FRC-D/AOU-1/4-MINI с фильтром"),
     KeyboardButton(text="Регулятор давления LFR-D/AOFR- 1/4-MINI")],
    [KeyboardButton(text="Регулятор давления LR-D/AOR -1/2-MIDI Без фильтра"),
     KeyboardButton(text="Регулятор давления LR-D/AOR - 1/4-MINI Без фильтра")],
    [KeyboardButton(text="Регулятор давления AC 2010-02"),
     KeyboardButton(text="Блок подготовки воздуха с регулятором давления BFC-4000")],
    [KeyboardButton(text="Блок подготовки воздуха с регулятором давления AFC-2000"),
     KeyboardButton(text="Фильтр влаготделитель с регулятором давления BFR-4000")],
    [KeyboardButton(text="Фильтр влаготделитель с регулятором давления AFR-2000"),
     KeyboardButton(text="Регулятор давления с манометром BR-4000")],
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
