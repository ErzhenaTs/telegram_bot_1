# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='5751134174:AAHaUTgUL05mKMyzi7Vnpl_NrGQEUPN-W9Q', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'дбо': 'дистанционное банковское обслуживание',
    'умбо':'Управление мониторинга банковских операций',
    'дккифм':'Департамент комплаенс контроля и финансового мониторинга',
    'сдо':'Система документационного обеспечения',
    'пси':'Приёмо-сдаточные испытания',
    'хотфикс':'Контур К5 - там, где проводятся срочные исправления для ПРОДа',
    'препрод':'Контур К4 - там, где проходят ПСИ',
    'рко':'Расчётно-кассовое обслуживание',
    'егрюл':'Единый государственный реестр юридических лиц. Федеральный ресурс, содержащий общие сведения о юридических лицах, осуществляющих предпринимательскую деятельность на территории России',
    'рпп':'Рублевое Платежное Получение',
    'оро':'Отдел расходных операций',
    'утоюл':'Управление транзакционных операций юридических лиц',
    'утофл':'Управление транзакционных операций физических лиц',
    'рцоп':'Региональный центр операционной поддержки',
    'фоив':'Федеральные органы исполнительной власти',
    'оснор':'Система электронного обмена сообщениями с налоговыми органами',
    'фкр':'Факторы кредитного риска',
    'тп':'Точка Продаж',
    'бик':'Банковский идентификационный код',
    'гоз':'ГосОборонЗаказ',
    'ип':'Индивидуальный предприниматель',
    'соид':'Система обработки исполнительных документов',
    'ид':'исполнительный документ',
    'фссп':'Федеральная служба судебных приставов',
    'фсс':'Фонд Социального Страхования',
    'цспп':'Центральная Служба Поддержки Пользователей',
    'абс':'Автоматизированная банковская система',
    'уфк':'Управление федерального казначейства',
    'вк':'Валютный контроль',
    'рцк':'Расчётный Центр Клиента',
    'рц':'Расчетный центр',
    'уфэбс':'Унифицированный формат электронных банковских сообщений',
    'инн':'Индивидуальный номер налогоплательщика',
    'арм':'Автоматизированное Рабочее Место',
    'урм':'Удалённое рабочее место',
    'врм':'Виртуальное Рабочее место',
    'фркк':'Фронтальное решение корпоративного клиента',
    'допб':'Департамент операционной поддержки бизнеса',
    'сро':'Саморегулируемая организация'

}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры 🤓\nВведи интересующую, например, ДОПБ', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='🤓 Я пока не знаю такой аббревиатуры',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующую',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
