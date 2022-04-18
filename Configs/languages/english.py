translations = {
    'commands': {
        'answers': {
            'start': 'Welcome, {user_name}!\nI am - *{bot_name}*, i will help you to get notifications from rocket. Press /help to get an instruction',
            'help': '/help command',
            'settings': 'Choose a setting',
            'role': {
                'root': "You'r a boss!",
                'admin': "You'r an admin!",
                'user': "You'r an usual user, access denied((("
            }
        }
    },
    'answers': {
        'dont-understand': "Sorry, i don't understand, type /start or /help"
    },
    'keyboards': {
        'answers': {
            'hello': 'Hi Hello',
            'joke': '<<Funny Joke>>',
            'another-keyboard': 'Open another keyboard'
        },
        'buttons': {
            'hi': 'Hi',
            'joke': 'Joke',
            'another-keyboard': 'Another keyboard'
        }
    },
    'callbacks': {
        'default': {
            'back': 'Back',
            'cancel': 'Cansel',
            'check-settings': 'Check settings',
            'check-settings-status': 'Settings checking status: {status}'
        },
        'answers': {
            'number-value': "Number value: {value}",
            'letter-value': "Letter value: {value}",
            'choose-language': 'Choose language',
            'choose-rocket-setting': 'Choose rocket setting\ndomain={domain}\nuser_id={user_id}\ntoken={token}',
            'language-updated-to': 'Language updated to {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Language',
                'rocket': 'Rocket'
            },
            'example': {
                '1': '1',
                '2': '2',
                '3': '3',
                'a': 'A',
                'b': 'B',
                'c': 'C'
            }
        },
        'state-back': {
            'rocket-form': "Past {value} or press 'Cancel'"
        },
        'settings': {
            'rocket': {
                'domain': 'Domain',
                'user-id': 'User id',
                'token': 'Token'
            }
        }
    }
}