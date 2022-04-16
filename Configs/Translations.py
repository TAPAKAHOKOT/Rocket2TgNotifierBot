from .languages.english import translations as english
from .languages.russian import translations as russian
import logging

class Translations:
    def __init__(self, language: str, get_user_language: callable):
        self.get_user_language = get_user_language

        self.language = language
        self.all_translations = {
            'english': english,
            'russian': russian
        }
        self.set_locale_translations()
    
    def set_locale_translations(self):
        try: self.locale_translations = self.all_translations[self.language]
        except KeyError:
            logging.error(f'key {self.language} not found in Translations.all_translations')
            raise KeyError
    
    def get_recoursive(self, keys: list, translations: dict, default: any = '') -> str:
        if keys[0] in translations.keys():
            if (len(keys) == 1):
                return translations[keys[0]]
            return self.get_recoursive(keys[1:], translations[keys[0]], default)
        return default
    
    def get(self, key: str, default: any = ''):
        self.update_locale_translations()
        return self.get_recoursive(
            key.split('.'),
            self.locale_translations
        )
    
    def get_in_all_languages(self, key: str) -> list:
        values = []
        keys = key.split('.')
        for translations in self.all_translations.values():
            value = self.get_recoursive(
                keys,
                translations
            )
            if value: values.append(value)
        return values

    
    def load_language(self) -> str:
        return self.get_user_language()
    
    def update_locale_translations(self):
        language = self.load_language()
        if self.language != language:
            self.language = language
            self.set_locale_translations()