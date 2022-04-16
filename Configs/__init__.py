from configparser import ConfigParser
from .Translations import Translations


app_config = ConfigParser()
app_config.read("Configs/app.ini")


def update_user_language(language: str):
    app_config.set('USER', 'language', language)

    with open("Configs/app.ini", 'w') as fp:
        app_config.write(fp, False)


def get_available_languages():
    languages = app_config.get('DEFAULT', 'available-languages').split(',')
    return map(lambda l: l.title(), languages)


def get_user_language() -> str:
    user_language = app_config.get('USER', 'language')
    return user_language if user_language else app_config.get('DEFAULT', 'language')
    

user_language = app_config.get('USER', 'language')
translations = Translations(
    user_language if user_language else app_config.get('DEFAULT', 'language'),
    get_user_language
)