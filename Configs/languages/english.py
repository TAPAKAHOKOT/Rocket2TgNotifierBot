translations = {
    'commands': {
        'answers': {
            'start': 'Welcome, {user_name}!\nI am - *{bot_name}*, i will help you to get notifications from rocket. Press /help to get more information.',
            'help': 'I will send you notifications from the rocket right here.\n\nBut for this you need to configure three fields in the /settings menu ("Rocket" button next): domain, user_id, token. To configure them, just click on the desired menu item and send the desired text value\n\nTo check the settings in /settings ("Rocket" button next), there is a "Check settings" button, and if it is not clear where to get the data for settings, you can see the "instruction"\n\nAfter successfully checking the settings, you can click "Notifications" to enable notifications',
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
            'write-to-dev': 'Enter below the message you want to send to the developers',
            'writed-to-dev': 'Message sent to developers',
            'write-to-all-users': 'Enter below the message you want to send to all users',
            'writed-to-all-users': 'Message sent to all users',
            'message-from-user': 'Message from user [ {username} ]:\n\n{message}',
            'message-from-admin-to-all-users': 'Message from admins:\n\n{message}',
        },
        'buttons': {
            'write-to-dev': 'Write to the developer📝',
            'write-to-all-users': 'Write to all users📝',
            'black-list': 'Black list'
        }
    },
    'callbacks': {
        'default': {
            'back': 'Back',
            'cancel': 'Cansel',
            'check-settings': 'Check settings',
            'check-settings-status': 'Settings checking status: {status}',
            'instruction': 'Instruction',
            'black-list': 'Your black list'
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
                    '7': 'All copied data is needed to configure bot in /settings->rocket menu to reject domain, userid and token',
                    '8': 'Data sample:\n\ndomain: [ rocket.mgts.ru ]\n\nuser id: [ 6iuKa4igFYuqQoPNl ]\n\ntoken: [ 8l_RyU0hJFilfFru-oBG3T8mT92v7T_SPVrSEW9mpGq ]'
                }
            }
        }
    }
}