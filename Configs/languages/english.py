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
        },
        'buttons': {
        }
    },
    'callbacks': {
        'default': {
            'back': 'Back',
            'cancel': 'Cansel',
            'check-settings': 'Check settings',
            'check-settings-status': 'Settings checking status: {status}',
            'instruction': 'Instruction'
        },
        'answers': {
            'number-value': "Number value: {value}",
            'letter-value': "Letter value: {value}",
            'choose-language': 'Choose language',
            'choose-rocket-setting': 'Choose rocket setting\n\ndomain=[ {domain} ]\n\nuser_id=[ {user_id} ]\n\ntoken=[ {token} ]',
            'language-updated-to': 'Language updated to {language}'
        },
        'keyboards': {
            'settings': {
                'language': 'Language',
                'rocket': 'Rocket'
            },
        },
        'state-back': {
            'rocket-form': "Past {value} or press 'Cancel'"
        },
        'settings': {
            'rocket': {
                'domain': 'Domain',
                'user-id': 'User id',
                'token': 'Token',
                'send_notifications': 'Notifications {status}',
                'instruction': {
                    '1': 'Click on your profile icon in the left corner sphere',
                    '2': 'In the final menu select "My account"',
                    '3': 'On the page that opens, select the menu item "Personal access tokens"',
                    '4': 'Enter any token name, check "Ignore Two Factor authentication" and click "Add"',
                    '5': 'In the comprehensive popup, copy "Token" and "User id" into your notes to send to the bot',
                    '6': 'In the line with the page address, copy the domain (highlighted in the photo)',
                    '7': 'All copied data is needed to configure bot in /settings->rocket menu to reject domain, userid and token'
                }
            }
        }
    }
}