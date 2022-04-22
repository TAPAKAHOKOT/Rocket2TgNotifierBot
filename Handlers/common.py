from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types

from Settings import settings
from Configs import translations
from States import WriteToDevForm
from Services import WriteToDevService

# <<<<<<<<<<<<<<<<<< Write to dev handler >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.write-to-dev')))
async def write_to_dev_message(message: types.Message):
    await WriteToDevForm.white_to_dev.set()
    await message.answer(translations.get('keyboards.answers.write-to-dev'))


# <<<<<<<<<<<<<<<<<< Write to dev handler >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(state=WriteToDevForm.white_to_dev)
async def write_to_dev_message(message: types.Message, state: FSMContext):
    await WriteToDevService.write_to_dev(message['from']['username'], message.text)
    await state.finish()
    await message.answer(translations.get('keyboards.answers.writed-to-dev'))

    
# <<<<<<<<<<<<<<<<<< Any message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message(message: types.Message):
    await message.answer(translations.get('answers.dont-understand'))
