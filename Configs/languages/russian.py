translations = {
    'commands': {
        'answers': {
            'start': 'Добро пожаловать, {user_name}!\nЯ - *{bot_name}*, помогу тебе получать уведомления из rocket. Введи /help чтобы получить подробную информацию.',
            'help': 'Я буду отправлять тебе уведомления из рокета прямо сюда.\n\nНо для этого нужно в меню /settings (далее кнопка "Rocket") настроить три поля: домен, user_id, token. Для их настройки достаточно нажать на нужный пункт меню и отправить текстом нужное значение\n\nДля проверки настроек в /settings (далее кнопка "Rocket") есть кнопка "Проверить настройки", а если непонятно откуда брать данные для настройки то можно посмотреть "инструкцию"\n\nПосле удачной проверки настроек можешь нажать "Уведомления" чтобы включить уведомления',
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
            'write-to-dev': 'Введите ниже сообщение которое хотите отправить разработчикам',
            'writed-to-dev': 'Сообщение отправлено разработчикам',
            'message-from-user': 'Сообщение от пользователя [ {username} ]:\n\n{message}'
        },
        'buttons': {
            'write-to-dev': 'Написать разработчику📝'
        }
    },
    'callbacks': {
        'default': {
            'back': 'Назад',
            'cancel': 'Отменить',
            'check-settings': 'Проверить настройки',
            'check-settings-status': 'Статус проверки настроек: {status}',
            'instruction': 'Инструкция'
        },
        'answers': {
            'number-value': "Значение номера: {value}",
            'letter-value': "Значение буквы: {value}",
            'choose-language': 'Выбери язык',
            'choose-rocket-setting': 'Выбери настройку рокета\n\nдомен=[ {domain} ]\n\nuser_id=[ {user_id} ]\n\ntoken=[ {token} ]',
            'language-updated-to': 'Язык обновлен на {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Язык',
                'rocket': 'Rocket'
            },
        },
        'state-back': {
            'rocket-form': "Вставьте {value} или нажмите 'Отменить'"
        },
        'settings': {
            'rocket': {
                'domain': 'Домен',
                'user-id': 'User id',
                'token': 'Token',
                'send_notifications': 'Уведомления {status}',
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