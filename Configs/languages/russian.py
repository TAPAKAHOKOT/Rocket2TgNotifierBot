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
            'check-settings': 'Проверить настройки',
            'instruction': 'Инструкция'
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
                'token': 'Token',
                'instruction': {
                    '1': 'Нажмите на иконку своего профиля в верхнем левом углу',
                    '2': 'Во всплывшем меню выберете "My account"',
                    '3': 'На открывшейся странице выберете пункт меню "Personal Access Tokens"',
                    '4': 'Введите любое название токена, поставьте галочку на "Ignore Two Factor Authentification" и нажмите "Add"',
                    '5': 'Во всплывшем popup-е скопируйте "Token" и "User id" в свои заметки, чтобы отправить их боту',
                    '6': 'В строке с адресом страницы скопируйте домен (выделен на фото)',
                    '7': 'Все скопированные данные нужны для настройки бота в меню /settings->rocket пункты domain, user id и token'
                }
            }
        }
    }
}