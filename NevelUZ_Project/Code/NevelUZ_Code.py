from NevelUZ_Keyboard import (language, home_ru, home_uz, home_en, catalog_ru, catalog_uz, catalog_en, tool_ru, tool_uz,
                              tool_en, prass1_product_ru, prass2_product_ru, prass_product_uz, prass_product_en,
                              product1_keyboard,
                              product2_keyboard, product3_keyboard, product4_keyboard, product5_keyboard,
                              product6_keyboard, product7_keyboard, mexanik_prass_ru, product8_keyboard,
                              product9_keyboard, gidrav_press_ru, product10_keyboard, product11_keyboard,
                              pneumatic_equipment_ru, hydraulic_distributor_ru, air_gun_ru, air_pressure_regulators_ru,
                              product12_keyboard, product13_keyboard, product14_keyboard, product15_keyboard,
                              product16_keyboard, product17_keyboard, product18_keyboard, product19_keyboard,
                              product20_keyboard, product21_keyboard, product22_keyboard, product23_keyboard,
                              product24_keyboard, product25_keyboard, product26_keyboard, product27_keyboard,
                              product28_keyboard, product29_keyboard, product30_keyboard, product31_keyboard,
                              product32_keyboard, settings_ru, delivery_ru, payment_ru, click_ru, payme_ru, cash_ru,
                              location_ru, webapp, electrical_goods_ru, chint_1p, chint_2p, chint_3p,
                              chint_and_cnc, cnc_2p, cnc_1p, cnc_3p, avr, electro_clapn, cooling_fans, fans_coolers,
                              cooler_grilles, product33_keyboard, product34_keyboard, product35_keyboard,
                              product36_keyboard, product37_keyboard, product38_keyboard, product39_keyboard,
                              product40_keyboard, product41_keyboard, product42_keyboard, product43_keyboard,
                              product44_keyboard, product45_keyboard, product46_keyboard, product47_keyboard,
                              product48_keyboard, product49_keyboard, product50_keyboard, product51_keyboard,
                              product52_keyboard, product53_keyboard, product54_keyboard, product55_keyboard,
                              product56_keyboard, product57_keyboard, product58_keyboard, product59_keyboard,
                              product60_keyboard, product61_keyboard, product62_keyboard, product63_keyboard,
                              product64_keyboard, product65_keyboard, product66_keyboard, product67_keyboard,
                              product68_keyboard, product69_keyboard)

from aiogram.filters import CommandStart

from NevelUZ_Project.Code.NevelUZ_Commands import commands
from NevelUZ_Project.Code.NevelUZ_Data import db_cursor, db_connect
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import FSInputFile
from NevelUZ_Product import Product1, Product2, Product3, Product4, Product5, Product6, Product7, Product8, Product9, \
    Product10, Product11, Product12, Product13, Product14, Product15, Product16, Product17, Product18, Product19, \
    Product20, Product21, Product22, Product23, Product24, Product25, Product26, Product27, Product28, Product29, \
    Product30, Product31, Product32, Product33, Product34, Product35, Product36, Product37, Product38, Product39, \
    Product40, Product41, Product42, Product43, Product44, Product45, Product46, Product47, Product48, Product49, \
    Product50, Product51, Product52, Product53, Product54, Product55, Product56, Product57, Product58, Product59, \
    Product60, Product61, Product62, Product63, Product64, Product65, Product66, Product67, Product68, Product69
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def starting_bot(message: types.Message):
    await message.answer("Здравствуйте! Давайте для начала выберем язык обслуживания!\n\n"
                         "Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.\n\n"
                         "Hi! Let's first we choose language of serving!\n\n", reply_markup=language)


@dp.message(F.text == "🚪 Выйти")
async def starting_bot(message: types.Message):
    await message.answer("Здравствуйте! Давайте для начала выберем язык обслуживания!\n\n"
                         "Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.\n\n"
                         "Hi! Let's first we choose language of serving!\n\n", reply_markup=language)


@dp.message(F.text == "Добавить продукт")
async def starting_bot(message: types.Message):
    await message.answer("Вы не можете добавить продукт так как вы не админ 🙅‍♂️", reply_markup=home_ru)


# Русский
@dp.message(F.text.in_(["⬅️ Назад", "Отменить ❌", "/menu"]))
async def ru_back(message: types.Message):
    await message.answer(
        "Нажмите на Каталог товаров 🗂, чтобы увидеть разнообразие товаров и добавить их в корзинку или в"
        " список избранных.\n\n"
        "Нажмите на Корзину 🛍, чтобы заказать товары или просмотреть их.\n\n"
        "Нажмите на Избранные ❤, чтобы легко просмотреть все ваши любимые товары.\n\n"
        "Нажмите на Настройки ⚙️, чтобы изменить язык или выполнить другие настройки.", reply_markup=home_ru)


@dp.message(F.text == "🇷🇺 Русский")
async def ru_greetings(message: types.Message):
    await message.answer_photo(photo=FSInputFile("../Images/Bot_img/Start_img.jpg"),
                               caption="Добро пожаловать в Nevel.UZ. Здесь вы можете приобрести электротовары.\n\n"
                                       "Мы готовы предложить вам обширную номенклатуру кабельной продукции,"
                                       " электроаксессуаров, распределительных устройств, осветительных приборов,"
                                       " систем жизнеобеспечения и комфорта для дома, а также любое другое "
                                       "электрооборудование.",
                               reply_markup=home_ru)


@dp.message(F.text.in_(["Каталог товаров 🗂", "/catalog"]))
async def ru_catalog(message: types.Message):
    await message.answer("Новый удобный каталог товаров", reply_markup=webapp)
    await message.answer("Выберите раздел", reply_markup=catalog_ru)


@dp.message(F.text.in_(["Избранные ❤️", "/favorites"]))
async def show_basket(message: types.Message):
    db_cursor.execute("SELECT * FROM favorites")
    favorites_items = db_cursor.fetchall()

    if favorites_items:
        response = "Ваши избранные товары:\n"
        total_price = 0
        for item in favorites_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title}\n"
    else:
        response = "У вас пока нет избранных товаров."

    await message.answer(response)


@dp.message(F.text.in_(["Корзина 🛍", "/basket"]))
async def show_basket(message: types.Message):
    db_cursor.execute("SELECT * FROM basket")
    basket_items = db_cursor.fetchall()

    if basket_items:
        response = "Товары в вашей корзине:\n"
        total_price = 0
        for item in basket_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title} : {quantity} шт, {price}00 сум\n\n"
        response += f"Общая стоимость: {round(total_price, 00)}00 сум"
    else:
        response = "Ваша корзина пока пуста."

    await message.answer(response, reply_markup=delivery_ru)


@dp.message(F.text == "Доставка 🚚")
async def ru_delivery(message: types.Message):
    await message.answer("Дайте локацию 📍", reply_markup=location_ru)


@dp.message(lambda message: message.location is not None)
async def ru_location(message: types.Message):
    await message.answer("Выберите способ оплаты 💵💳", reply_markup=payment_ru)


@dp.message(lambda message: message.text == "Наличные 💵")
async def ru_cash(message: types.Message):
    db_cursor.execute("SELECT * FROM basket")
    basket_items = db_cursor.fetchall()

    if basket_items:
        response = ""
        total_price = 0
        for item in basket_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title} : {quantity} шт, {price}00 сум\n\n"
        response += f"\nОбщая стоимость:  {round(total_price, 2)} сум"
    else:
        response = "Корзина пуста."

    await message.answer(response, reply_markup=cash_ru)


@dp.message(F.text == "Подтвердить ✅")
async def ru_payme(message: types.Message):
    await message.answer("К сожалению доставка временно не работает.Обратите по этой "
                         "Рекомендуем обратиться по этой номере : +998 (97) 181-40-00;"
                         "Наша локация ⬇️", reply_markup=payme_ru)
    await message.answer_location(41.355931, 69.246039)


@dp.message(F.text == "Изменить 🔄")
async def ru_payme(message: types.Message):
    await message.answer("Выберите способ оплаты 💵💳", reply_markup=payment_ru)


@dp.message(F.text == "Payme 💳")
async def ru_payme(message: types.Message):
    db_cursor.execute("SELECT * FROM basket")
    basket_items = db_cursor.fetchall()

    if basket_items:
        response = ""
        total_price = 0
        for item in basket_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title} : {quantity} шт, {price}00 сум\n\n"
        response += f"\nОбщая стоимость:  {round(total_price, 2)} сум"
    else:
        response = "Корзина пуста."
    await message.answer(response, reply_markup=payme_ru)


@dp.message(F.text == "Click 💳")
async def ru_click(message: types.Message):
    db_cursor.execute("SELECT * FROM basket")
    basket_items = db_cursor.fetchall()

    if basket_items:
        response = ""
        total_price = 0
        for item in basket_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title} : {quantity} шт, {price}00 сум\n\n"
        response += f"\nОбщая стоимость:  {round(total_price, 2)} сум"
    else:
        response = "Корзина пуста."
    await message.answer(response, reply_markup=click_ru)


@dp.message(F.text.in_(["Настройки ⚙️", "/settings"]))
async def ru_tool(message: types.Message):
    await message.answer("Выберите настройку", reply_markup=settings_ru)


@dp.message(F.text == "🇷🇺🇸🇱 Изменить язык")
async def ru_tool(message: types.Message):
    await message.answer("Выберите настройку", reply_markup=language)


@dp.message(F.text == "Инструменты")
async def ru_tool(message: types.Message):
    await message.answer("Выберите категорию инструментов", reply_markup=tool_ru)


@dp.message(F.text == "Пневмооборудование")
async def ru_pneumatic_equipment(message: types.Message):
    await message.answer("Выберите категорию пневмооборудование", reply_markup=pneumatic_equipment_ru)


@dp.message(F.text == "Электротовары")
async def ru_electrical_goods(message: types.Message):
    await message.answer("Выберите категорию электротоваров", reply_markup=electrical_goods_ru)


@dp.message(F.text == "Автоматические выключатели модульные")
async def ru_chint(message: types.Message):
    await message.answer("Выберите фазу 1-3 автоматического включателя", reply_markup=chint_and_cnc)


@dp.message(F.text == "1P-CHINT")
async def ru_chint(message: types.Message):
    await message.answer("Выберите автоматические включатель", reply_markup=chint_1p)


@dp.message(F.text == "2P-CHINT")
async def ru_chint(message: types.Message):
    await message.answer("Выберите автоматические включатель", reply_markup=chint_2p)


@dp.message(F.text == "3P-CHINT")
async def ru_chint(message: types.Message):
    await message.answer("Выберите автоматические включатель", reply_markup=chint_3p)


@dp.message(F.text == "1P-CNC")
async def ru_cnc(message: types.Message):
    await message.answer("Выберите автоматические включатель", reply_markup=cnc_1p)


@dp.message(F.text == "2P-CNC")
async def ru_cnc(message: types.Message):
    await message.answer("Выберите автоматические включатель", reply_markup=cnc_2p)


@dp.message(F.text == "3P-CNC")
async def ru_cnc(message: types.Message):
    await message.answer("Выберите автоматические включатель", reply_markup=cnc_3p)


@dp.message(F.text == "Автоматический ввод резерва (АВР)")
async def ru_cnc(message: types.Message):
    await message.answer("Выберите автоматические ввод резерва (АВР)", reply_markup=avr)


@dp.message(F.text == "Электромагнитный клапан")
async def ru_cnc(message: types.Message):
    await message.answer("Выберите электромагнитный клапан", reply_markup=electro_clapn)


@dp.message(F.text == "Вентиляторы охлаждения")
async def ru_cnc(message: types.Message):
    await message.answer("Выберите вентиляторы охлаждения", reply_markup=cooling_fans)


@dp.message(F.text == "Вентиляторы и кулеры")
async def ru_fans_coolers(message: types.Message):
    await message.answer("Выберите вентиляторы и кулеры", reply_markup=fans_coolers)


@dp.message(F.text == "Решетки для кулера")
async def ru_cooler_grilles(message: types.Message):
    await message.answer("Выберите решетки для кулера", reply_markup=cooler_grilles)


@dp.message(F.text == "Гидрораспределитель")
async def ru_hydraulic_distributor_product(message: types.Message):
    await message.answer("Выберите гидрораспределитель", reply_markup=hydraulic_distributor_ru)


@dp.message(F.text == "Пневматический Пистолет")
async def ru_hydraulic_distributor_product(message: types.Message):
    await message.answer("Выберите пневматический пистолет", reply_markup=air_gun_ru)


@dp.message(F.text == "Регуляторы давления воздуха")
async def ru_hydraulic_distributor_product(message: types.Message):
    await message.answer("Выберите регуляторы давления воздуха", reply_markup=air_pressure_regulators_ru)


@dp.message(F.text == "Пресс-клещи для втулочных наконечников")
async def ru_prass1_product(message: types.Message):
    await message.answer("Выберите инструмент", reply_markup=prass1_product_ru)


@dp.message(F.text == "Пресс-клещи для изолированных наконечников")
async def ru_prass2_product(message: types.Message):
    await message.answer("Выберите инструмент", reply_markup=prass2_product_ru)


@dp.message(F.text == "Прессы механические")
async def ru_prass_mexanik_product(message: types.Message):
    await message.answer("Выберите инструмент", reply_markup=mexanik_prass_ru)


@dp.message(F.text == "Прессы гидравлические")
async def ru_prass_gidrav_product(message: types.Message):
    await message.answer("Выберите инструмент", reply_markup=gidrav_press_ru)


@dp.message(F.text == "Пресс-клещи VSC9 10-6A")
async def send_product_info(message: types.Message):
    msg, photo = Product1.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product1_keyboard)


@dp.message(F.text == "Пресс-клещи VSC9 16-4A")
async def send_product_info(message: types.Message):
    msg, photo = Product2.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product2_keyboard)


@dp.message(F.text == "Пресс-клещи VSC8 6-6A")
async def send_product_info(message: types.Message):
    msg, photo = Product3.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product3_keyboard)


@dp.message(F.text == "Пресс-клещи VSC8 6-4A")
async def send_product_info(message: types.Message):
    msg, photo = Product4.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product4_keyboard)


@dp.message(F.text == "Пресс-клещи VSB-30J")
async def send_product_info(message: types.Message):
    msg, photo = Product5.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product5_keyboard)


@dp.message(F.text == "Пресс-клещи VSA-02C")
async def send_product_info(message: types.Message):
    msg, photo = Product6.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product6_keyboard)


@dp.message(F.text == "Пресс-клещи VSA-06WF")
async def send_product_info(message: types.Message):
    msg, photo = Product7.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product7_keyboard)


@dp.message(F.text == "Пресс механический HX-50B (6-50mm)")
async def send_product_info(message: types.Message):
    msg, photo = Product8.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product8_keyboard)


@dp.message(F.text == "Инструмент HT-2008R (обжим коннекторов RJ-45, RJ-11 / 12 с фикс.)")
async def send_product_info(message: types.Message):
    msg, photo = Product9.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product9_keyboard)


@dp.message(F.text == "Пресс гидравлический ручной YQK-300A (16-300mm)")
async def send_product_info(message: types.Message):
    msg, photo = Product10.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product10_keyboard)


@dp.message(F.text == "Пресс гидравлический ручной YQK-240A (16-240mm)")
async def send_product_info(message: types.Message):
    msg, photo = Product11.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product11_keyboard)


@dp.message(F.text == "Гидрораспределитель DSG-3C2-02")
async def send_product_info(message: types.Message):
    msg, photo = Product12.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product12_keyboard)


@dp.message(F.text == "Гидрораспределитель DSG-03-3C2-AC220V")
async def send_product_info(message: types.Message):
    msg, photo = Product13.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product13_keyboard)


@dp.message(F.text == "Гидрораспределитель DSG-02-3C4-DL-D24")
async def send_product_info(message: types.Message):
    msg, photo = Product14.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product14_keyboard)


@dp.message(F.text == "Гидрораспределитель 4W6D-50/AW220NZ5L")
async def send_product_info(message: types.Message):
    msg, photo = Product15.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product15_keyboard)


@dp.message(F.text == "Гидрораспределитель DSG-02-2B60B 24VDC")
async def send_product_info(message: types.Message):
    msg, photo = Product16.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product16_keyboard)


@dp.message(F.text == "Пневматический пистолет (мет) DG-10")
async def send_product_info(message: types.Message):
    msg, photo = Product17.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product17_keyboard)


@dp.message(F.text == "Пневматический пистолет PAG-07")
async def send_product_info(message: types.Message):
    msg, photo = Product18.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product18_keyboard)


@dp.message(F.text == "Пневматический пистолет PAG-02")
async def send_product_info(message: types.Message):
    msg, photo = Product19.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product19_keyboard)


@dp.message(F.text == "Реле давления HEP110")
async def send_product_info(message: types.Message):
    msg, photo = Product20.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product20_keyboard)


@dp.message(F.text == "Регулятор давления QTYH-15 40 бар 1/2")
async def send_product_info(message: types.Message):
    msg, photo = Product21.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product21_keyboard)


@dp.message(F.text == "Регулятор давления FRC-D/AOU-1/4-MINI с фильтром")
async def send_product_info(message: types.Message):
    msg, photo = Product22.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product22_keyboard)


@dp.message(F.text == "Регулятор давления LFR-D/AOFR- 1/4-MINI")
async def send_product_info(message: types.Message):
    msg, photo = Product23.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product23_keyboard)


@dp.message(F.text == "Регулятор давления LR-D/AOR -1/2-MIDI Без фильтра")
async def send_product_info(message: types.Message):
    msg, photo = Product24.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product24_keyboard)


@dp.message(F.text == "Регулятор давления LR-D/AOR - 1/4-MINI Без фильтра")
async def send_product_info(message: types.Message):
    msg, photo = Product25.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product25_keyboard)


@dp.message(F.text == "Регулятор давления AC 2010-02")
async def send_product_info(message: types.Message):
    msg, photo = Product26.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product26_keyboard)


@dp.message(F.text == "Блок подготовки воздуха с регулятором давления BFC-4000")
async def send_product_info(message: types.Message):
    msg, photo = Product27.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product27_keyboard)


@dp.message(F.text == "Блок подготовки воздуха с регулятором давления AFC-2000")
async def send_product_info(message: types.Message):
    msg, photo = Product28.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product28_keyboard)


@dp.message(F.text == "Фильтр влаготделитель с регулятором давления BFR-4000")
async def send_product_info(message: types.Message):
    msg, photo = Product29.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product29_keyboard)


@dp.message(F.text == "Фильтр влаготделитель с регулятором давления AFR-2000")
async def send_product_info(message: types.Message):
    msg, photo = Product30.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product30_keyboard)


@dp.message(F.text == "Регулятор давления с манометром BR-4000")
async def send_product_info(message: types.Message):
    msg, photo = Product31.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product31_keyboard)


@dp.message(F.text == "Регулятор давления с манометром AR-2000")
async def send_product_info(message: types.Message):
    msg, photo = Product32.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product32_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 1A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product33.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product33_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 2A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product34.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product34_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 3A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product35.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product35_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 4A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product36.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product36_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 6A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product37.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product37_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 10A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product38.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product38_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 16A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product39.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product39_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 25A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product40.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product40_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 32A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product41.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product41_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 40A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product42.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product42_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 50A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product43.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product43_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 1P 63A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product44.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product44_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 2A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product45.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product45_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 4A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product46.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product46_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 6A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product47.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product47_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 10A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product48.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product48_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 16A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product49.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product49_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 25A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product50.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product50_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 32A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product51.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product51_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 40A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product52.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product52_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 50A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product53.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product53_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 2P 63A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product54.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product54_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 2A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product55.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product55_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 4A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product56.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product56_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 6A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product57.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product57_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 10A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product58.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product58_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 16A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product59.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product59_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 25A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product60.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product60_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 32A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product61.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product61_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 40A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product62.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product62_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 50A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product63.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product63_keyboard)


@dp.message(F.text == "Автоматический выключатель NXB-63 3P 63A 6кА х-ка С")
async def send_product_info(message: types.Message):
    msg, photo = Product64.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product64_keyboard)


@dp.message(F.text == "Автоматический ввод резерва АВР XLDS-630/4P 630A")
async def send_product_info(message: types.Message):
    msg, photo = Product65.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product65_keyboard)


@dp.message(F.text == "Автоматический ввод резерва АВР XLDS-250/4P 250A")
async def send_product_info(message: types.Message):
    msg, photo = Product66.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product66_keyboard)


@dp.message(F.text == "Автоматический ввод резерва АВР XLDS-125/4P 100A")
async def send_product_info(message: types.Message):
    msg, photo = Product67.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product67_keyboard)


@dp.message(F.text == "Автоматический ввод резерва АВР XLDS-1000/4P 1000A")
async def send_product_info(message: types.Message):
    msg, photo = Product68.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product68_keyboard)


@dp.message(F.text == "Автоматический ввод резерва АВР XLDS-1600/4P 1600A")
async def send_product_info(message: types.Message):
    msg, photo = Product69.send_product_info()
    await message.answer_photo(photo=FSInputFile(photo), caption=msg, reply_markup=product69_keyboard)


# O'zbekcha
@dp.message(F.text == "⬅️ Orqaga")
async def uz_back(message: types.Message):
    await message.answer(
        "Turli xil mahsulotlarni ko'rish va ularni savatga yoki sevimlilar ro'yxatiga qo'shish "
        "uchun Mahsulotlar katalogi 🗂 ustiga bosing.\n\n"
        "Mahsulotlarni buyurtma qilish yoki ko'rish uchun Savatga 🛍 bosing.\n\n"
        "Barcha sevimli mahsulotlaringizni osongina ko'rish uchun Sevimlilar ❤ tugmasini bosing.\n\n"
        "Tilni oʻzgartirish yoki boshqa sozlamalarni oʻrnatish uchun “Sozlamalar ⚙️” tugmasini bosing.",
        reply_markup=home_uz)


@dp.message(F.text == "🇺🇿 O'zbekcha")
async def uz_greetings(message: types.Message):
    await message.answer("Oʻzbek tili vaqtincha ishlamayapti")
    # await message.answer_photo(photo=FSInputFile("../Images/Bot_img/Start_img.jpg"),
    #                            caption="Nevel.UZ saytiga xush kelibsiz. Bu yerda siz elektrotexnika mahsulotlarini "
    #                                    "xarid qilishingiz mumkin.\n\n"
    #                                    "Biz sizga kabel mahsulotlarining keng assortimentini taklif qilishga tayyormiz,"
    #                                    " elektr jihozlari, tarqatish moslamalari, yoritish moslamalari,"
    #                                    " hayotni qo'llab-quvvatlash va uydagi qulaylik tizimlari,"
    #                                    " shuningdek, boshqa har qanday elektr jihozlari.", reply_markup=home_uz)


@dp.message(F.text == "Katalog 🗂")
async def uz_catalog(message: types.Message):
    await message.answer("Bo'limni tanlang", reply_markup=catalog_uz)


@dp.message(F.text == "Asboblar")
async def uz_tool(message: types.Message):
    await message.answer("Asboblar toifasini tanlang", reply_markup=tool_uz)


@dp.message(F.text == "Press-klesh vtulochniy nakonechniklar uchun")
async def uz_prass_product(message: types.Message):
    await message.answer("Asbobni tanlang", reply_markup=prass_product_uz)


# English
@dp.message(F.text == "⬅️ Back")
async def en_back(message: types.Message):
    await message.answer(
        "Click on Product Catalog 🗂 to see a variety of products and add them to your cart or favorites list.\n\n"
        "Click on Cart 🛍 to order or view products.\n\n"
        "Click on Favorites ❤ to easily view all your favorite products.\n\n"
        "Tap Settings ⚙️ to change the language or make other settings.", reply_markup=home_en)


@dp.message(F.text == "🇺🇸 English")
async def ru_greetings(message: types.Message):
    await message.answer("English language is temporarily unavailable")
    # await message.answer_photo(photo=FSInputFile("../Images/Bot_img/Start_img.jpg"),
    #                            caption="Welcome to Nevel.UZ. Here you can buy electrical goods.\n\n"
    #                                    "We are ready to offer you wide range of cable products "
    #                                    "electrical accessories, switchgear, lighting fixtures"
    #                                    "Life support and home comfort systems as well as any other electrical "
    #                                    "equipments.",
    #                            reply_markup=home_en)


@dp.message(F.text == "Catalog 🗂")
async def en_catalog(message: types.Message):
    await message.answer("Choose a section", reply_markup=catalog_en)


@dp.message(F.text == "Tools")
async def uz_tool(message: types.Message):
    await message.answer("Select the Tools category", reply_markup=tool_en)


@dp.message(F.text == "Press pliers for ferrules")
async def ru_prass_product(message: types.Message):
    await message.answer("Select a tool", reply_markup=prass_product_en)


@dp.callback_query(F.data == "add_Product1")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product1.quantity += 1
    Product1.price += 468.900

    await callback.message.answer_photo(photo=FSInputFile(Product1.photo),
                                        caption=f"{Product1.title}\n\n{Product1.description}\n\n{round(Product1.price,
                                                                                                       2)}00 сум"
                                                f"\n\nКоличество - {Product1.quantity}",
                                        reply_markup=product1_keyboard)


@dp.callback_query(F.data == "remove_Product1")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product1.quantity -= 1
    Product1.price -= 468.900

    await callback.message.answer_photo(photo=FSInputFile(Product1.photo),
                                        caption=f"{Product1.title}\n\n{Product1.description}\n\n{round(Product1.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product1.quantity} \n",
                                        reply_markup=product1_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product1')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC9 10-6A", f"{Product1.price}00", Product1.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product1')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC9 10-6A", f"{Product1.price}00", Product1.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product2")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product2.quantity += 1
    Product2.price += 393.200

    await callback.message.answer_photo(photo=FSInputFile(Product2.photo),
                                        caption=f"{Product2.title}\n\n{Product2.description}\n\n{round(Product2.price, 2
                                                                                                       )}00 сум"
                                                f"\n\nКоличество - {Product2.quantity}",
                                        reply_markup=product2_keyboard)


@dp.callback_query(F.data == "remove_Product2")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product2.quantity -= 1
    Product2.price -= 393.200

    await callback.message.answer_photo(photo=FSInputFile(Product2.photo),
                                        caption=f"{Product2.title}\n\n{Product2.description}\n\n{round(Product2.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product2.quantity} \n",
                                        reply_markup=product2_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product2')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC9 16-4A", f"{Product2.price}00", Product2.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product2')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC9 16-4A", f"{Product2.price}00", Product2.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product3")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product3.quantity += 1
    Product3.price += 247.700

    await callback.message.answer_photo(photo=FSInputFile(Product3.photo),
                                        caption=f"{Product3.title}\n\n{Product3.description}\n\n{round(Product3.price, 2
                                                                                                       )}00 сум"
                                                f"\n\nКоличество - {Product3.quantity}",
                                        reply_markup=product3_keyboard)


@dp.callback_query(F.data == "remove_Product3")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product3.quantity -= 1
    Product3.price -= 247.700

    await callback.message.answer_photo(photo=FSInputFile(Product3.photo),
                                        caption=f"{Product3.title}\n\n{Product3.description}\n\n{round(Product3.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product3.quantity} \n",
                                        reply_markup=product3_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product3')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC8 6-6A", f"{Product3.price}00", Product3.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product3')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC8 6-6A", f"{Product3.price}00", Product3.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product4")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product4.quantity += 1
    Product4.price += 209.900

    await callback.message.answer_photo(photo=FSInputFile(Product4.photo),
                                        caption=f"{Product4.title}\n\n{Product4.description}\n\n{round(Product4.price, 2
                                                                                                       )}00 сум"
                                                f"\n\nКоличество - {Product4.quantity}",
                                        reply_markup=product4_keyboard)


@dp.callback_query(F.data == "remove_Product4")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product4.quantity -= 1
    Product4.price -= 209.900

    await callback.message.answer_photo(photo=FSInputFile(Product4.photo),
                                        caption=f"{Product4.title}\n\n{Product4.description}\n\n{round(Product4.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product4.quantity} \n",
                                        reply_markup=product4_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product4')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC8 6-4A", f"{Product4.price}00", Product4.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product4')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSC8 6-4A", f"{Product4.price}00", Product4.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product5")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product5.quantity += 1
    Product5.price += 249.500

    await callback.message.answer_photo(photo=FSInputFile(Product5.photo),
                                        caption=f"{Product5.title}\n\n{Product5.description}\n\n{round(Product5.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product5.quantity} \n",
                                        reply_markup=product5_keyboard)


@dp.callback_query(F.data == "remove_Product5")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product5.quantity -= 1
    Product5.price -= 249.500

    await callback.message.answer_photo(photo=FSInputFile(Product5.photo),
                                        caption=f"{Product5.title}\n\n{Product5.description}\n\n{round(Product5.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product5.quantity} \n",
                                        reply_markup=product5_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product5')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSB-30J", f"{Product5.price}00", Product5.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product5')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSB-30J", f"{Product5.price}00", Product5.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product6")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product6.quantity += 1
    Product6.price += 231.400

    await callback.message.answer_photo(photo=FSInputFile(Product6.photo),
                                        caption=f"{Product6.title}\n\n{Product6.description}\n\n{round(Product6.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product6.quantity} \n",
                                        reply_markup=product6_keyboard)


@dp.callback_query(F.data == "remove_Product6")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product6.quantity -= 1
    Product6.price -= 231.400

    await callback.message.answer_photo(photo=FSInputFile(Product6.photo),
                                        caption=f"{Product6.title}\n\n{Product6.description}\n\n{round(Product6.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product6.quantity} \n",
                                        reply_markup=product6_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product6')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSA-02C", f"{Product6.price}00", Product6.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product6')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSA-02C", f"{Product6.price}00", Product6.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product7")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product7.quantity += 1
    Product7.price += 231.400

    await callback.message.answer_photo(photo=FSInputFile(Product7.photo),
                                        caption=f"{Product7.title}\n\n{Product7.description}\n\n{round(Product7.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product7.quantity} \n",
                                        reply_markup=product7_keyboard)


@dp.callback_query(F.data == "remove_Product7")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product7.quantity -= 1
    Product7.price -= 231.400

    await callback.message.answer_photo(photo=FSInputFile(Product7.photo),
                                        caption=f"{Product7.title}\n\n{Product7.description}\n\n{round(Product7.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product7.quantity} \n",
                                        reply_markup=product7_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product7')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс-клещи VSA-06WF", f"{Product7.price}00", Product7.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product7')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс-клещи VSA-06WF", f"{Product7.price}00", Product7.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product8")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product8.quantity += 1
    Product8.price += 238.400

    await callback.message.answer_photo(photo=FSInputFile(Product8.photo),
                                        caption=f"{Product8.title}\n\n{Product8.description}\n\n{round(Product8.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product8.quantity} \n",
                                        reply_markup=product8_keyboard)


@dp.callback_query(F.data == "remove_Product8")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product8.quantity -= 1
    Product8.price -= 238.400

    await callback.message.answer_photo(photo=FSInputFile(Product8.photo),
                                        caption=f"{Product8.title}\n\n{Product8.description}\n\n{round(Product8.price, 2
                                                                                                       )}00 "
                                                f"сум\n\nКоличество - {Product8.quantity} \n",
                                        reply_markup=product8_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product8')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс механический HX-50B (6-50mm)", f"{Product8.price}00", Product8.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product8')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс механический HX-50B (6-50mm)", f"{Product8.price}00", Product8.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product9")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product9.quantity += 1
    Product9.price += 142.300

    await callback.message.answer_photo(photo=FSInputFile(Product9.photo),
                                        caption=f"{Product9.title}\n\n{Product9.description}\n\n{round(Product9.price,
                                                                                                       2)}00 "
                                                f"сум\n\nКоличество - {Product9.quantity} \n",
                                        reply_markup=product9_keyboard)


@dp.callback_query(F.data == "remove_Product9")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product9.quantity -= 1
    Product9.price -= 142.300

    await callback.message.answer_photo(photo=FSInputFile(Product9.photo),
                                        caption=f"{Product9.title}\n\n{Product9.description}\n\n{round(Product9.price,
                                                                                                       2)}00 "
                                                f"сум\n\nКоличество - {Product9.quantity} \n",
                                        reply_markup=product9_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product9')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Инструмент HT-2008R (обжим коннекторов RJ-45, RJ-11 / 12 с фикс.)",
              f"{Product9.price}00", Product9.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product9')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Инструмент HT-2008R (обжим коннекторов RJ-45, RJ-11 / 12 с фикс.)",
              f"{Product9.price}00", Product9.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product10")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product10.quantity += 1
    Product10.price += 633.100

    await callback.message.answer_photo(photo=FSInputFile(Product10.photo),
                                        caption=f"{Product10.title}\n\n{Product10.description}\n\n{round(
                                            Product10.price, 2)}00 "
                                                f"сум\n\nКоличество - {Product10.quantity} \n",
                                        reply_markup=product10_keyboard)


@dp.callback_query(F.data == "remove_Product10")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product10.quantity -= 1
    Product10.price -= 633.100

    await callback.message.answer_photo(photo=FSInputFile(Product10.photo),
                                        caption=f"{Product10.title}\n\n{Product10.description}\n\n{round(Product10.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product10.quantity} \n",
                                        reply_markup=product10_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product10')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс гидравлический ручной YQK-300A (16-300mm)",
              f"{Product10.price}00", Product10.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product10')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс гидравлический ручной YQK-300A (16-300mm)",
              f"{Product10.price}00", Product10.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product11")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product11.quantity += 1
    Product11.price += 579.800

    await callback.message.answer_photo(photo=FSInputFile(Product11.photo),
                                        caption=f"{Product11.title}\n\n{Product11.description}\n\n{round(Product11.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product11.quantity} \n",
                                        reply_markup=product11_keyboard)


@dp.callback_query(F.data == "remove_Product11")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product11.quantity -= 1
    Product11.price -= 579.800

    await callback.message.answer_photo(photo=FSInputFile(Product11.photo),
                                        caption=f"{Product11.title}\n\n{Product11.description}\n\n{round(Product11.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product11.quantity} \n",
                                        reply_markup=product11_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product11')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пресс гидравлический ручной YQK-240A (16-240mm)",
              f"{Product11.price}00", Product11.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product11')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пресс гидравлический ручной YQK-240A (16-240mm)",
              f"{Product11.price}00", Product11.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product12")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product12.quantity += 1
    Product12.price += 543.400

    await callback.message.answer_photo(photo=FSInputFile(Product12.photo),
                                        caption=f"{Product12.title}\n\n{Product12.description}\n\n{round(Product12.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product12.quantity} \n",
                                        reply_markup=product12_keyboard)


@dp.callback_query(F.data == "remove_Product12")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product12.quantity -= 1
    Product12.price -= 543.400

    await callback.message.answer_photo(photo=FSInputFile(Product12.photo),
                                        caption=f"{Product12.title}\n\n{Product12.description}\n\n{round(Product12.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product12.quantity} \n",
                                        reply_markup=product12_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product12')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-3C2-02",
              f"{Product12.price}00", Product12.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product12')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-3C2-02",
              f"{Product12.price}00", Product12.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product13")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product13.quantity += 1
    Product13.price += 851.100

    await callback.message.answer_photo(photo=FSInputFile(Product13.photo),
                                        caption=f"{Product13.title}\n\n{Product13.description}\n\n{round(Product13.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product13.quantity} \n",
                                        reply_markup=product13_keyboard)


@dp.callback_query(F.data == "remove_Product13")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product13.quantity -= 1
    Product13.price -= 851.100

    await callback.message.answer_photo(photo=FSInputFile(Product13.photo),
                                        caption=f"{Product13.title}\n\n{Product13.description}\n\n{round(Product13.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product13.quantity} \n",
                                        reply_markup=product13_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product13')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-03-3C2-AC220V",
              f"{Product13.price}00", Product13.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product13')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-03-3C2-AC220V",
              f"{Product13.price}00", Product13.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product14")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product14.quantity += 1
    Product14.price += 472.000

    await callback.message.answer_photo(photo=FSInputFile(Product14.photo),
                                        caption=f"{Product14.title}\n\n{Product14.description}\n\n{round(Product14.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product14.quantity} \n",
                                        reply_markup=product14_keyboard)


@dp.callback_query(F.data == "remove_Product14")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product14.quantity -= 1
    Product14.price -= 472.000

    await callback.message.answer_photo(photo=FSInputFile(Product14.photo),
                                        caption=f"{Product14.title}\n\n{Product14.description}\n\n{round(Product14.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product14.quantity} \n",
                                        reply_markup=product14_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product14')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-02-3C4-DL-D24",
              f"{Product14.price}00", Product14.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product14')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-02-3C4-DL-D24",
              f"{Product14.price}00", Product14.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product15")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product15.quantity += 1
    Product15.price += 404.900

    await callback.message.answer_photo(photo=FSInputFile(Product15.photo),
                                        caption=f"{Product15.title}\n\n{Product15.description}\n\n{round(Product15.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product15.quantity} \n",
                                        reply_markup=product15_keyboard)


@dp.callback_query(F.data == "remove_Product15")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product15.quantity -= 1
    Product15.price -= 404.900

    await callback.message.answer_photo(photo=FSInputFile(Product15.photo),
                                        caption=f"{Product15.title}\n\n{Product15.description}\n\n{round(Product15.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product15.quantity} \n",
                                        reply_markup=product15_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product15')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Гидрораспределитель 4W6D-50/AW220NZ5L",
              f"{Product15.price}00", Product15.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product15')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Гидрораспределитель 4W6D-50/AW220NZ5L",
              f"{Product15.price}00", Product15.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product16")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product16.quantity += 1
    Product16.price += 459.400

    await callback.message.answer_photo(photo=FSInputFile(Product16.photo),
                                        caption=f"{Product16.title}\n\n{Product16.description}\n\n{round(Product16.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product16.quantity} \n",
                                        reply_markup=product16_keyboard)


@dp.callback_query(F.data == "remove_Product16")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product16.quantity -= 1
    Product16.price -= 459.400

    await callback.message.answer_photo(photo=FSInputFile(Product16.photo),
                                        caption=f"{Product16.title}\n\n{Product16.description}\n\n{round(Product16.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product16.quantity} \n",
                                        reply_markup=product16_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product16')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-02-2B60B 24VDC",
              f"{Product16.price}00", Product16.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product16')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Гидрораспределитель DSG-02-2B60B 24VDC",
              f"{Product16.price}00", Product16.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product17")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product17.quantity += 1
    Product17.price += 157.400

    await callback.message.answer_photo(photo=FSInputFile(Product17.photo),
                                        caption=f"{Product17.title}\n\n{Product17.description}\n\n{round(Product17.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product17.quantity} \n",
                                        reply_markup=product17_keyboard)


@dp.callback_query(F.data == "remove_Product17")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product17.quantity -= 1
    Product17.price -= 157.400

    await callback.message.answer_photo(photo=FSInputFile(Product17.photo),
                                        caption=f"{Product17.title}\n\n{Product17.description}\n\n{round(Product17.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product17.quantity} \n",
                                        reply_markup=product17_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product17')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пневматический пистолет (мет) DG-10",
              f"{Product17.price}00", Product17.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product17')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пневматический пистолет (мет) DG-10",
              f"{Product17.price}00", Product17.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product18")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product18.quantity += 1
    Product18.price += 39.400

    await callback.message.answer_photo(photo=FSInputFile(Product18.photo),
                                        caption=f"{Product18.title}\n\n{Product18.description}\n\n{round(Product18.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product18.quantity} \n",
                                        reply_markup=product18_keyboard)


@dp.callback_query(F.data == "remove_Product18")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product18.quantity -= 1
    Product18.price -= 39.400

    await callback.message.answer_photo(photo=FSInputFile(Product18.photo),
                                        caption=f"{Product18.title}\n\n{Product18.description}\n\n{round(Product18.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product18.quantity} \n",
                                        reply_markup=product18_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product18')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пневматический пистолет PAG-07",
              f"{Product18.price}00", Product18.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product18')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пневматический пистолет PAG-07",
              f"{Product18.price}00", Product18.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product19")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product19.quantity += 1
    Product19.price += 39.400

    await callback.message.answer_photo(photo=FSInputFile(Product19.photo),
                                        caption=f"{Product19.title}\n\n{Product19.description}\n\n{round(Product19.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product19.quantity} \n",
                                        reply_markup=product19_keyboard)


@dp.callback_query(F.data == "remove_Product19")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product19.quantity -= 1
    Product19.price -= 39.400

    await callback.message.answer_photo(photo=FSInputFile(Product19.photo),
                                        caption=f"{Product19.title}\n\n{Product19.description}\n\n{round(Product19.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product19.quantity} \n",
                                        reply_markup=product19_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product19')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Пневматический пистолет PAG-02",
              f"{Product19.price}00", Product19.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product19')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Пневматический пистолет PAG-02",
              f"{Product19.price}00", Product19.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product20")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product20.quantity += 1
    Product20.price += 153.000

    await callback.message.answer_photo(photo=FSInputFile(Product20.photo),
                                        caption=f"{Product20.title}\n\n{Product20.description}\n\n{round(Product20.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product20.quantity} \n",
                                        reply_markup=product20_keyboard)


@dp.callback_query(F.data == "remove_Product20")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product20.quantity -= 1
    Product20.price -= 153.000

    await callback.message.answer_photo(photo=FSInputFile(Product20.photo),
                                        caption=f"{Product20.title}\n\n{Product20.description}\n\n{round(Product20.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product20.quantity} \n",
                                        reply_markup=product20_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product20')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Реле давления HEP110",
              f"{Product20.price}00", Product20.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product20')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Реле давления HEP110",
              f"{Product20.price}00", Product20.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product21")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product21.quantity += 1
    Product21.price += 173.000

    await callback.message.answer_photo(photo=FSInputFile(Product21.photo),
                                        caption=f"{Product21.title}\n\n{Product21.description}\n\n{round(Product21.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product21.quantity} \n",
                                        reply_markup=product21_keyboard)


@dp.callback_query(F.data == "remove_Product21")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product21.quantity -= 1
    Product21.price -= 173.000

    await callback.message.answer_photo(photo=FSInputFile(Product21.photo),
                                        caption=f"{Product21.title}\n\n{Product21.description}\n\n{round(Product21.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product21.quantity} \n",
                                        reply_markup=product21_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product21')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления QTYH-15 40 бар 1/2",
              f"{Product21.price}00", Product21.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product21')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления QTYH-15 40 бар 1/2",
              f"{Product21.price}00", Product21.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product22")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product22.quantity += 1
    Product22.price += 433.400

    await callback.message.answer_photo(photo=FSInputFile(Product22.photo),
                                        caption=f"{Product22.title}\n\n{Product22.description}\n\n{round(Product22.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product22.quantity} \n",
                                        reply_markup=product22_keyboard)


@dp.callback_query(F.data == "remove_Product22")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product22.quantity -= 1
    Product22.price -= 433.400

    await callback.message.answer_photo(photo=FSInputFile(Product22.photo),
                                        caption=f"{Product22.title}\n\n{Product22.description}\n\n{round(Product22.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product22.quantity} \n",
                                        reply_markup=product22_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product22')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления FRC-D/AOU-1/4-MINI с фильтром",
              f"{Product22.price}00", Product22.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product22')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления FRC-D/AOU-1/4-MINI с фильтром",
              f"{Product22.price}00", Product22.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product23")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product23.quantity += 1
    Product23.price += 269.500

    await callback.message.answer_photo(photo=FSInputFile(Product23.photo),
                                        caption=f"{Product23.title}\n\n{Product23.description}\n\n{round(Product23.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product23.quantity} \n",
                                        reply_markup=product23_keyboard)


@dp.callback_query(F.data == "remove_Product23")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product23.quantity -= 1
    Product23.price -= 269.500

    await callback.message.answer_photo(photo=FSInputFile(Product23.photo),
                                        caption=f"{Product23.title}\n\n{Product23.description}\n\n{round(Product23.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product23.quantity} \n",
                                        reply_markup=product23_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product23')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления LFR-D/AOFR- 1/4-MINI",
              f"{Product23.price}00", Product23.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product23')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления LFR-D/AOFR- 1/4-MINI",
              f"{Product23.price}00", Product23.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product24")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product24.quantity += 1
    Product24.price += 338.600

    await callback.message.answer_photo(photo=FSInputFile(Product24.photo),
                                        caption=f"{Product24.title}\n\n{Product24.description}\n\n{round(Product24.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product24.quantity} \n",
                                        reply_markup=product24_keyboard)


@dp.callback_query(F.data == "remove_Product24")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product24.quantity -= 1
    Product24.price -= 338.600

    await callback.message.answer_photo(photo=FSInputFile(Product24.photo),
                                        caption=f"{Product24.title}\n\n{Product24.description}\n\n{round(Product24.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product24.quantity} \n",
                                        reply_markup=product24_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product24')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления LR-D/AOR -1/2-MIDI Без фильтра",
              f"{Product24.price}00", Product24.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product24')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления LR-D/AOR -1/2-MIDI Без фильтра",
              f"{Product24.price}00", Product24.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product25")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product25.quantity += 1
    Product25.price += 201.100

    await callback.message.answer_photo(photo=FSInputFile(Product25.photo),
                                        caption=f"{Product25.title}\n\n{Product25.description}\n\n{round(Product25.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product25.quantity} \n",
                                        reply_markup=product25_keyboard)


@dp.callback_query(F.data == "remove_Product25")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product25.quantity -= 1
    Product25.price -= 201.100

    await callback.message.answer_photo(photo=FSInputFile(Product25.photo),
                                        caption=f"{Product25.title}\n\n{Product25.description}\n\n{round(Product25.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product25.quantity} \n",
                                        reply_markup=product25_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product25')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления LR-D/AOR - 1/4-MINI Без фильтра",
              f"{Product25.price}00", Product25.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product25')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления LR-D/AOR - 1/4-MINI Без фильтра",
              f"{Product25.price}00", Product25.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product26")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product26.quantity += 1
    Product26.price += 162.100

    await callback.message.answer_photo(photo=FSInputFile(Product26.photo),
                                        caption=f"{Product26.title}\n\n{Product26.description}\n\n{round(Product26.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product26.quantity} \n",
                                        reply_markup=product26_keyboard)


@dp.callback_query(F.data == "remove_Product26")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product26.quantity -= 1
    Product26.price -= 162.100

    await callback.message.answer_photo(photo=FSInputFile(Product26.photo),
                                        caption=f"{Product26.title}\n\n{Product26.description}\n\n{round(Product26.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product26.quantity} \n",
                                        reply_markup=product26_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product26')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления AC 2010-02",
              f"{Product26.price}00", Product26.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product26')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления AC 2010-02",
              f"{Product26.price}00", Product26.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product27")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product27.quantity += 1
    Product27.price += 206.100

    await callback.message.answer_photo(photo=FSInputFile(Product27.photo),
                                        caption=f"{Product27.title}\n\n{Product27.description}\n\n{round(Product27.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product27.quantity} \n",
                                        reply_markup=product27_keyboard)


@dp.callback_query(F.data == "remove_Product27")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product27.quantity -= 1
    Product27.price -= 206.100

    await callback.message.answer_photo(photo=FSInputFile(Product27.photo),
                                        caption=f"{Product27.title}\n\n{Product27.description}\n\n{round(Product27.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product27.quantity} \n",
                                        reply_markup=product27_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product27')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Блок подготовки воздуха с регулятором давления BFC-4000",
              f"{Product27.price}00", Product27.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product27')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Блок подготовки воздуха с регулятором давления BFC-4000",
              f"{Product27.price}00", Product27.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product28")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product28.quantity += 1
    Product28.price += 102.800

    await callback.message.answer_photo(photo=FSInputFile(Product28.photo),
                                        caption=f"{Product28.title}\n\n{Product28.description}\n\n{round(Product28.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product28.quantity} \n",
                                        reply_markup=product28_keyboard)


@dp.callback_query(F.data == "remove_Product28")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product28.quantity -= 1
    Product28.price -= 102.800

    await callback.message.answer_photo(photo=FSInputFile(Product28.photo),
                                        caption=f"{Product28.title}\n\n{Product28.description}\n\n{round(Product28.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product28.quantity} \n",
                                        reply_markup=product28_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product28')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Блок подготовки воздуха с регулятором давления AFC-2000",
              f"{Product28.price}00", Product28.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product28')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Блок подготовки воздуха с регулятором давления AFC-2000",
              f"{Product28.price}00", Product28.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product29")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product29.quantity += 1
    Product29.price += 121.100

    await callback.message.answer_photo(photo=FSInputFile(Product29.photo),
                                        caption=f"{Product29.title}\n\n{Product29.description}\n\n{round(Product29.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product29.quantity} \n",
                                        reply_markup=product29_keyboard)


@dp.callback_query(F.data == "remove_Product29")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product29.quantity -= 1
    Product29.price -= 121.100

    await callback.message.answer_photo(photo=FSInputFile(Product29.photo),
                                        caption=f"{Product29.title}\n\n{Product29.description}\n\n{round(Product29.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product29.quantity} \n",
                                        reply_markup=product29_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product29')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Фильтр влаготделитель с регулятором давления BFR-4000",
              f"{Product29.price}00", Product29.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product29')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Фильтр влаготделитель с регулятором давления BFR-4000",
              f"{Product29.price}00", Product29.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product30")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product30.quantity += 1
    Product30.price += 80.100

    await callback.message.answer_photo(photo=FSInputFile(Product30.photo),
                                        caption=f"{Product30.title}\n\n{Product30.description}\n\n{round(Product30.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product30.quantity} \n",
                                        reply_markup=product30_keyboard)


@dp.callback_query(F.data == "remove_Product30")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product30.quantity -= 1
    Product30.price -= 80.100

    await callback.message.answer_photo(photo=FSInputFile(Product30.photo),
                                        caption=f"{Product30.title}\n\n{Product30.description}\n\n{round(Product30.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product30.quantity} \n",
                                        reply_markup=product30_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product30')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Фильтр влаготделитель с регулятором давления AFR-2000",
              f"{Product30.price}00", Product30.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product30')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Фильтр влаготделитель с регулятором давления AFR-2000",
              f"{Product30.price}00", Product30.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product31")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product31.quantity += 1
    Product31.price += 80.100

    await callback.message.answer_photo(photo=FSInputFile(Product31.photo),
                                        caption=f"{Product31.title}\n\n{Product31.description}\n\n{round(Product31.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product31.quantity} \n",
                                        reply_markup=product31_keyboard)


@dp.callback_query(F.data == "remove_Product31")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product31.quantity -= 1
    Product31.price -= 80.100

    await callback.message.answer_photo(photo=FSInputFile(Product31.photo),
                                        caption=f"{Product31.title}\n\n{Product31.description}\n\n{round(Product31.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product31.quantity} \n",
                                        reply_markup=product31_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product31')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Фильтр влаготделитель с регулятором давления AFR-2000",
              f"{Product31.price}00", Product31.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product31')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления с манометром BR-4000",
              f"{Product31.price}00", Product31.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product32")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product32.quantity += 1
    Product32.price += 70.500

    await callback.message.answer_photo(photo=FSInputFile(Product32.photo),
                                        caption=f"{Product32.title}\n\n{Product32.description}\n\n{round(Product32.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product32.quantity} \n",
                                        reply_markup=product32_keyboard)


@dp.callback_query(F.data == "remove_Product32")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product32.quantity -= 1
    Product32.price -= 70.500

    await callback.message.answer_photo(photo=FSInputFile(Product32.photo),
                                        caption=f"{Product32.title}\n\n{Product32.description}\n\n{round(Product32.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product32.quantity} \n",
                                        reply_markup=product32_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product32')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Регулятор давления с манометром AR-2000",
              f"{Product32.price}00", Product32.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product32')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Регулятор давления с манометром AR-2000",
              f"{Product32.price}00", Product32.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product33")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product33.quantity += 1
    Product33.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product33.photo),
                                        caption=f"{Product33.title}\n\n{Product33.description}\n\n{round(Product33.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product33.quantity} \n",
                                        reply_markup=product33_keyboard)


@dp.callback_query(F.data == "remove_Product33")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product33.quantity -= 1
    Product33.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product33.photo),
                                        caption=f"{Product33.title}\n\n{Product33.description}\n\n{round(Product33.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product33.quantity} \n",
                                        reply_markup=product33_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product33')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 1A 6кА х-ка С",
              f"{Product33.price}00", Product33.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product33')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 1A 6кА х-ка С",
              f"{Product33.price}00", Product33.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product34")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product34.quantity += 1
    Product34.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product34.photo),
                                        caption=f"{Product34.title}\n\n{Product34.description}\n\n{round(Product34.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product34.quantity} \n",
                                        reply_markup=product34_keyboard)


@dp.callback_query(F.data == "remove_Product34")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product34.quantity -= 1
    Product34.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product34.photo),
                                        caption=f"{Product34.title}\n\n{Product34.description}\n\n{round(Product34.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product34.quantity} \n",
                                        reply_markup=product34_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product34')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 2A 6кА х-ка С",
              f"{Product34.price}00", Product34.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product34')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 2A 6кА х-ка С",
              f"{Product34.price}00", Product34.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product35")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product35.quantity += 1
    Product35.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product35.photo),
                                        caption=f"{Product35.title}\n\n{Product35.description}\n\n{round(Product35.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product35.quantity} \n",
                                        reply_markup=product35_keyboard)


@dp.callback_query(F.data == "remove_Product35")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product35.quantity -= 1
    Product35.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product35.photo),
                                        caption=f"{Product35.title}\n\n{Product35.description}\n\n{round(Product35.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product35.quantity} \n",
                                        reply_markup=product35_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product35')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 3A 6кА х-ка С",
              f"{Product35.price}00", Product35.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product35')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 3A 6кА х-ка С",
              f"{Product35.price}00", Product35.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product36")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product36.quantity += 1
    Product36.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product36.photo),
                                        caption=f"{Product36.title}\n\n{Product36.description}\n\n{round(Product36.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product36.quantity} \n",
                                        reply_markup=product36_keyboard)


@dp.callback_query(F.data == "remove_Product36")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product36.quantity -= 1
    Product36.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product36.photo),
                                        caption=f"{Product36.title}\n\n{Product36.description}\n\n{round(Product36.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product36.quantity} \n",
                                        reply_markup=product36_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product36')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 4A 6кА х-ка С",
              f"{Product36.price}00", Product36.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product36')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 4A 6кА х-ка С",
              f"{Product36.price}00", Product36.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product37")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product37.quantity += 1
    Product37.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product37.photo),
                                        caption=f"{Product37.title}\n\n{Product37.description}\n\n{round(Product37.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product37.quantity} \n",
                                        reply_markup=product37_keyboard)


@dp.callback_query(F.data == "remove_Product37")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product37.quantity -= 1
    Product37.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product37.photo),
                                        caption=f"{Product37.title}\n\n{Product37.description}\n\n{round(Product37.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product37.quantity} \n",
                                        reply_markup=product37_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product37')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 6A 6кА х-ка С",
              f"{Product37.price}00", Product37.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product37')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 6A 6кА х-ка С",
              f"{Product37.price}00", Product37.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product38")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product38.quantity += 1
    Product38.price += 14.300

    await callback.message.answer_photo(photo=FSInputFile(Product38.photo),
                                        caption=f"{Product38.title}\n\n{Product38.description}\n\n{round(Product38.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product38.quantity} \n",
                                        reply_markup=product38_keyboard)


@dp.callback_query(F.data == "remove_Product38")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product38.quantity -= 1
    Product38.price -= 14.300

    await callback.message.answer_photo(photo=FSInputFile(Product38.photo),
                                        caption=f"{Product38.title}\n\n{Product38.description}\n\n{round(Product38.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product38.quantity} \n",
                                        reply_markup=product38_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product38')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 10A 6кА х-ка С",
              f"{Product38.price}00", Product38.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product38')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 10A 6кА х-ка С",
              f"{Product38.price}00", Product38.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product39")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product39.quantity += 1
    Product39.price += 14.300

    await callback.message.answer_photo(photo=FSInputFile(Product39.photo),
                                        caption=f"{Product39.title}\n\n{Product39.description}\n\n{round(Product39.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product39.quantity} \n",
                                        reply_markup=product39_keyboard)


@dp.callback_query(F.data == "remove_Product39")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product39.quantity -= 1
    Product39.price -= 14.300

    await callback.message.answer_photo(photo=FSInputFile(Product39.photo),
                                        caption=f"{Product39.title}\n\n{Product39.description}\n\n{round(Product39.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product39.quantity} \n",
                                        reply_markup=product39_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product39')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 10A 6кА х-ка С",
              f"{Product39.price}00", Product39.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product39')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 16A 6кА х-ка С",
              f"{Product39.price}00", Product39.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product40")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product40.quantity += 1
    Product40.price += 14.300

    await callback.message.answer_photo(photo=FSInputFile(Product40.photo),
                                        caption=f"{Product40.title}\n\n{Product40.description}\n\n{round(Product40.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product40.quantity} \n",
                                        reply_markup=product40_keyboard)


@dp.callback_query(F.data == "remove_Product40")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product40.quantity -= 1
    Product40.price -= 14.300

    await callback.message.answer_photo(photo=FSInputFile(Product40.photo),
                                        caption=f"{Product40.title}\n\n{Product40.description}\n\n{round(Product40.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product40.quantity} \n",
                                        reply_markup=product40_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product40')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 25A 6кА х-ка С",
              f"{Product40.price}00", Product40.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product40')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 25A 6кА х-ка С",
              f"{Product40.price}00", Product40.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product41")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product41.quantity += 1
    Product41.price += 15.300

    await callback.message.answer_photo(photo=FSInputFile(Product41.photo),
                                        caption=f"{Product41.title}\n\n{Product41.description}\n\n{round(Product41.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product41.quantity} \n",
                                        reply_markup=product41_keyboard)


@dp.callback_query(F.data == "remove_Product41")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product41.quantity -= 1
    Product41.price -= 15.300

    await callback.message.answer_photo(photo=FSInputFile(Product41.photo),
                                        caption=f"{Product41.title}\n\n{Product41.description}\n\n{round(Product41.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product41.quantity} \n",
                                        reply_markup=product41_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product41')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 25A 6кА х-ка С",
              f"{Product41.price}00", Product41.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product41')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 25A 6кА х-ка С",
              f"{Product41.price}00", Product41.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product42")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product42.quantity += 1
    Product42.price += 15.300

    await callback.message.answer_photo(photo=FSInputFile(Product42.photo),
                                        caption=f"{Product42.title}\n\n{Product42.description}\n\n{round(Product42.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product42.quantity} \n",
                                        reply_markup=product42_keyboard)


@dp.callback_query(F.data == "remove_Product42")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product42.quantity -= 1
    Product42.price -= 15.300

    await callback.message.answer_photo(photo=FSInputFile(Product42.photo),
                                        caption=f"{Product42.title}\n\n{Product42.description}\n\n{round(Product42.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product42.quantity} \n",
                                        reply_markup=product42_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product42')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 40A 6кА х-ка С",
              f"{Product42.price}00", Product42.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product42')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 40A 6кА х-ка С",
              f"{Product42.price}00", Product42.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product43")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product43.quantity += 1
    Product43.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product43.photo),
                                        caption=f"{Product43.title}\n\n{Product43.description}\n\n{round(Product43.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product43.quantity} \n",
                                        reply_markup=product43_keyboard)


@dp.callback_query(F.data == "remove_Product43")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product43.quantity -= 1
    Product43.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product43.photo),
                                        caption=f"{Product43.title}\n\n{Product43.description}\n\n{round(Product43.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product43.quantity} \n",
                                        reply_markup=product43_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product43')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 50A 6кА х-ка С",
              f"{Product43.price}00", Product43.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product43')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 50A 6кА х-ка С",
              f"{Product43.price}00", Product43.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product44")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product44.quantity += 1
    Product44.price += 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product44.photo),
                                        caption=f"{Product44.title}\n\n{Product44.description}\n\n{round(Product44.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product44.quantity} \n",
                                        reply_markup=product44_keyboard)


@dp.callback_query(F.data == "remove_Product44")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product44.quantity -= 1
    Product44.price -= 18.500

    await callback.message.answer_photo(photo=FSInputFile(Product44.photo),
                                        caption=f"{Product44.title}\n\n{Product44.description}\n\n{round(Product44.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product44.quantity} \n",
                                        reply_markup=product44_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product44')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 63A 6кА х-ка С",
              f"{Product44.price}00", Product44.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product44')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический выключатель NXB-63 1P 63A 6кА х-ка С",
              f"{Product44.price}00", Product44.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product65")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product65.quantity += 1
    Product65.price += 5080.000

    await callback.message.answer_photo(photo=FSInputFile(Product65.photo),
                                        caption=f"{Product65.title}\n\n{Product65.description}\n\n{round(Product65.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product65.quantity} \n",
                                        reply_markup=product65_keyboard)


@dp.callback_query(F.data == "remove_Product65")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product65.quantity -= 1
    Product65.price -= 5080.000

    await callback.message.answer_photo(photo=FSInputFile(Product65.photo),
                                        caption=f"{Product65.title}\n\n{Product65.description}\n\n{round(Product65.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product65.quantity} \n",
                                        reply_markup=product65_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product65')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-630/4P 630A",
              f"{Product65.price}00", Product65.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product65')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-630/4P 630A",
              f"{Product65.price}00", Product65.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product66")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product66.quantity += 1
    Product66.price += 2540.000

    await callback.message.answer_photo(photo=FSInputFile(Product66.photo),
                                        caption=f"{Product66.title}\n\n{Product66.description}\n\n{round(Product66.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product66.quantity} \n",
                                        reply_markup=product66_keyboard)


@dp.callback_query(F.data == "remove_Product66")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product66.quantity -= 1
    Product66.price -= 2540.000

    await callback.message.answer_photo(photo=FSInputFile(Product66.photo),
                                        caption=f"{Product66.title}\n\n{Product66.description}\n\n{round(Product66.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product66.quantity} \n",
                                        reply_markup=product66_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product66')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-250/4P 250A",
              f"{Product66.price}00", Product66.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product66')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-250/4P 250A",
              f"{Product66.price}00", Product66.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product67")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product67.quantity += 1
    Product67.price += 1270.000

    await callback.message.answer_photo(photo=FSInputFile(Product67.photo),
                                        caption=f"{Product67.title}\n\n{Product67.description}\n\n{round(Product67.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product67.quantity} \n",
                                        reply_markup=product67_keyboard)


@dp.callback_query(F.data == "remove_Product67")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product67.quantity -= 1
    Product67.price -= 1270.000

    await callback.message.answer_photo(photo=FSInputFile(Product67.photo),
                                        caption=f"{Product67.title}\n\n{Product67.description}\n\n{round(Product67.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product67.quantity} \n",
                                        reply_markup=product67_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product67')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-125/4P 100A",
              f"{Product67.price}00", Product67.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product67')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-125/4P 100A",
              f"{Product67.price}00", Product67.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product68")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product68.quantity += 1
    Product68.price += 15748.000

    await callback.message.answer_photo(photo=FSInputFile(Product68.photo),
                                        caption=f"{Product68.title}\n\n{Product68.description}\n\n{round(Product68.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product68.quantity} \n",
                                        reply_markup=product68_keyboard)


@dp.callback_query(F.data == "remove_Product68")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product68.quantity -= 1
    Product68.price -= 15748.000

    await callback.message.answer_photo(photo=FSInputFile(Product68.photo),
                                        caption=f"{Product68.title}\n\n{Product68.description}\n\n{round(Product68.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product68.quantity} \n",
                                        reply_markup=product68_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product68')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-1000/4P 1000A",
              f"{Product68.price}00", Product68.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product68')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-1000/4P 1000A",
              f"{Product68.price}00", Product68.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


@dp.callback_query(F.data == "add_Product69")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product69.quantity += 1
    Product69.price += 19050.000

    await callback.message.answer_photo(photo=FSInputFile(Product69.photo),
                                        caption=f"{Product69.title}\n\n{Product69.description}\n\n{round(Product69.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product69.quantity} \n",
                                        reply_markup=product69_keyboard)


@dp.callback_query(F.data == "remove_Product69")
async def add_quantity(callback: types.CallbackQuery):
    await callback.message.delete()
    Product69.quantity -= 1
    Product69.price -= 19050.000

    await callback.message.answer_photo(photo=FSInputFile(Product69.photo),
                                        caption=f"{Product69.title}\n\n{Product69.description}\n\n{round(Product69.price
                                                                                                         , 2)}00 "
                                                f"сум\n\nКоличество - {Product69.quantity} \n",
                                        reply_markup=product69_keyboard)


@dp.callback_query(F.data == 'add_Favorites_Product69')
async def add_product(message: types.Message):
    db_cursor.execute("""
        INSERT INTO favorites (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-1600/4P 1600A",
              f"{Product69.price}00", Product69.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Избранные ❤️")


@dp.callback_query(F.data == 'add_Basket_Product69')
async def add_basket(message: types.Message):
    db_cursor.execute("""
            INSERT INTO basket (title, price, quantity)
            VALUES (?, ?, ?)
        """, ("Автоматический ввод резерва АВР XLDS-1600/4P 1600A",
              f"{Product69.price}00", Product69.quantity))
    db_connect.commit()
    await message.answer("Продукт добавлен в Корзине 🛍")


async def main():
    print("Bot started")
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
