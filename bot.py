import telebot


bot = telebot.TeleBot('740277784:AAGLaVvzQ0LXDZoZP7K2MeBMB5k3_MRcIrg')
glava = ''
number = ''

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == '/geometry':
		bot.send_message(message.from_user.id, "Хорошо! Теберь выбери номер (1-448)")
		bot.register_next_step_handler(message, get_num_geom) #следующий шаг – функция get_num_geom
	elif message.text == '/algebra':
		bot.send_message(message.from_user.id, "Хорошо! Теберь выбери главу (1-3)")
		bot.register_next_step_handler(message, get_glava_alg) #следующий шаг – функция get_glava_alg
	else:
		bot.send_message(message.from_user.id, 'Напиши /geometry или /algebra !')


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
			bot.send_message(message.from_user.id, 'Ты должен ввести  номер от 1 до 448! Что бы начать, напиши /geometry или /algebra !')
	else:
		bot.send_message(message.from_user.id, 'Ты должен ввести цифру от 1 до 448! Что бы начать, напиши /geometry или /algebra !')

def get_glava_alg(message):
	global glava
	glava = message.text;
	if glava.isdigit():
		if (int(glava) >= 1 and int(glava) <= 3):
			bot.send_message(message.from_user.id, 'Введи номер!')
			bot.register_next_step_handler(message, get_num_alg)
		else:
			bot.send_message(message.from_user.id, 'Ты должен ввести номер главы от 1 до 3! Что бы начать, напиши /geometry или /algebra !')
	else:
		bot.send_message(message.from_user.id, 'Ты должен ввести цифру от 1 до 3! Что бы начать, напиши /geometry или /algebra!')
	
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
			bot.send_message(message.from_user.id, 'Ты должен ввести существующий номер! Что бы начать, напиши /geometry или /algebra !')
	else:
		bot.send_message(message.from_user.id, 'Ты должен ввести цифру! Что бы начать, напиши /geometry или /algebra !')
bot.polling()
