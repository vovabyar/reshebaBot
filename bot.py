import telebot
from telebot import types

bot = telebot.TeleBot('740277784:AAGLaVvzQ0LXDZoZP7K2MeBMB5k3_MRcIrg')
glava = ''
number = ''

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == '/start':
		keyboard = telebot.types.InlineKeyboardMarkup()
		key_help = telebot.types.InlineKeyboardButton(text="\ud83c\udd70\ufe0f Алгебра \ud83c\udd70\ufe0f",
													  callback_data="algebra")
		keyboard.add(key_help)
		key_search = telebot.types.InlineKeyboardButton(text="\ud83c\udd71\ufe0f Геометрия \ud83c\udd71\ufe0f",
														callback_data="geometry")
		keyboard.add(key_search)
		bot.send_message(message.chat.id,'''Выбери предмет!''',reply_markup=keyboard)
	else:
		bot.send_message(message.from_user.id, 'Напиши /start!')
		
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		global glava
		if call.data == "geometry":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо! Теберь выбери номер (1-448)',parse_mode='Markdown')
			geomHandler(call.message)
		elif call.data == "algebra":
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='\u23ec \u23ec \u23ec \u23ec \u23ec',parse_mode='Markdown')
			alg_glava(call.message)
		elif call.data == "1":
			glava = '1'
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='\u23ec \u23ec \u23ec \u23ec \u23ec',parse_mode='Markdown')
			algHandler(call.message)
		elif call.data == "2":
			glava = '2'
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='\u23ec \u23ec \u23ec \u23ec \u23ec',parse_mode='Markdown')
			algHandler(call.message)
		elif call.data == "3":
			glava = '3'
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='\u23ec \u23ec \u23ec \u23ec \u23ec',parse_mode='Markdown')
			algHandler(call.message)

def geomHandler(message):
   bot.register_next_step_handler(message, get_num_geom)
   
def algHandler(message):
	bot.send_message(message.chat.id, 'Хорошо! Теберь выбери номер!')
	bot.register_next_step_handler(message, get_num_alg)

def alg_glava(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	key_one = telebot.types.InlineKeyboardButton(text="\u2611\ufe0f 1",#1
													  callback_data="1")
	key_two = telebot.types.InlineKeyboardButton(text="\u2611\ufe0f 2",#2
														callback_data="2")
	key_three = telebot.types.InlineKeyboardButton(text="\u2611\ufe0f 3",#3
														callback_data="3")
	keyboard.add(key_one)
	keyboard.add(key_two)
	keyboard.add(key_three)
	bot.send_message(message.chat.id,'''Выбери главу (1-3)!''',reply_markup=keyboard)
	
   
def get_num_geom(message):
	global number
	number = message.text;
	if message.text.isdigit():
		if (int(message.text) > 0 and int(number) <= 165):
			glava = '1'
			bot.send_photo(chat_id=message.chat.id, photo=open('geom' + '/'+ glava +'/' + str(int(number) + 45516) + '.jpg', 'rb'))
		elif (int(message.text) > 165 and int(message.text) <= 321):
			glava = '2'
			bot.send_photo(chat_id=message.chat.id, photo=open('geom' + '/'+ glava +'/' + str(int(number) + 45516) + '.jpg', 'rb'))
		elif (int(message.text) > 321 and int(message.text) <= 448):
			glava = '3'
			bot.send_photo(chat_id=message.chat.id, photo=open('geom' + '/'+ glava +'/' + str(int(number) + 45516) + '.jpg', 'rb'))
		else:
			bot.send_message(message.from_user.id, 'Ты должен ввести  номер от 1 до 448! Что бы начать, напиши /start!')
	else:
		bot.send_message(message.from_user.id, 'Ты должен ввести цифру от 1 до 448! Что бы начать, напиши /start!')

	
def get_num_alg(message):
	global number
	number = message.text;
	if message.text.isdigit():
		if (glava == '1' and int(message.text) > 0 and int(number) <= 140):
			bot.send_photo(chat_id=message.chat.id, photo=open('alg' + '/'+ glava +'/' + number + '.png', 'rb'))
		elif (glava == '2' and int(message.text) > 0 and int(message.text) <= 199):
			bot.send_photo(chat_id=message.chat.id, photo=open('alg' + '/'+ glava +'/' + number + '.png', 'rb'))
		elif (glava == '3' and int(message.text) > 0 and int(message.text) <= 164):
			bot.send_photo(chat_id=message.chat.id, photo=open('alg' + '/'+ glava +'/' + number + '.png', 'rb'))
		else:
			bot.send_message(message.from_user.id, 'Ты должен ввести существующий номер! Что бы начать, напиши /start!')
	else:
		bot.send_message(message.from_user.id, 'Ты должен ввести цифру! Что бы начать, напиши /start!')
bot.polling()
