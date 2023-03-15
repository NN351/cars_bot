from aiogram import types



def get_menu_button():
    # markup - настройка кнопок
    markup = types.InlineKeyboardMarkup(row_width=1)
    # Кнопки:
    category = types.InlineKeyboardButton(
# Название кнопки - Categories       Уникальный код кнопки - category
        "Categories", callback_data="category")
    search_by_name = types.InlineKeyboardButton(
        "Search by name", callback_data="search_by_name"
    )
    search_by_price = types.InlineKeyboardButton(
        "Search by price", callback_data="search_by_price"
    )
    markup.add(category, search_by_name, search_by_price) # добавление кнопок
    return markup

def get_post_url_button(link):
    markup = types.InlineKeyboardMarkup()
    url = types.InlineKeyboardButton("Go to site", url=link)
    markup.add(url)
    return markup