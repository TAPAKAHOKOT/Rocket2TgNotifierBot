translations = {
    'commands': {
        'answers': {
            'start': 'Добро пожаловать, {user_name}!\nЯ - *{bot_name}*, помогу тебе получать уведомления из rocket. Введи /help чтобы получить инструкцию',
            'help': '/help команда',
            'settings': 'Выбери настройку',
            'role': {
                'root': 'Ты босс',
                'admin': 'Ты админ',
                'user': 'Ты пользователь, доступ закрыт((('
            }
        }
    },
    'answers': {
        'dont-understand': "Извините, я не понимаю, нажмите /start или /help"
    },
    'keyboards': {
        'answers': {
            'hello': 'Прив Привет',
            'joke': '<<Смешная шутка>>',
            'another-keyboard': 'Открываю другую клавиатуру'
        },
        'buttons': {
            'hi': 'Приу',
            'joke': 'Шутка',
            'another-keyboard': 'Другая клавиатура'
        }
    },
    'callbacks': {
        'default': {
            'back': 'Назад',
            'cancel': 'Отменить',
            'check-settings': 'Проверить настройки'
        },
        'answers': {
            'number-value': "Значение номера: {value}",
            'letter-value': "Значение буквы: {value}",
            'choose-language': 'Выбери язык',
            'choose-rocket-setting': 'Выбери настройку рокета\nдомен={domain}\nuser_id={user_id}\ntoken={token}',
            'language-updated-to': 'Язык обновлен на {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Язык',
                'rocket': 'Rocket'
            },
            'example': {
                '1': '1',
                '2': '2',
                '3': '3',
                'a': 'А',
                'b': 'Б',
                'c': 'В'
            }
        },
        'state-back': {
            'rocket-form': "Вставьте {value} или нажмите 'Отменить'"
        },
        'settings': {
            'rocket': {
                'domain': 'Домен',
                'user-id': 'User id',
                'token': 'Token'
            }
        }
    }
}