from telebot.types import InlineKeyboardMarkup as ik
from telebot.types import InlineKeyboardButton as ib
from telebot import types
from const import b
from functools import wraps

users = dict()

to = lambda message: message.chat.id
current = ''

def log(user_id, state, users):
	if user_id not in users.keys(): users.update({user_id:''})
	print(users)
	users[user_id] = state

@b.message_handler(commands=['start'])
def start(message):
	t = to(message)
	k = ik()
	k.add(ib(text="x^3 - 2*x^2 + x + 1 = 0", callback_data='equ'))
	md = """*Рівняння для знаходження коренів:*"""
	b.send_message(t, text=md, reply_markup=k, parse_mode="Markdown")

@b.message_handler(content_types=['text'])
def resp(message):
	t = to(message)
	if current == 'equ':
		try:
			params = [float(d) for d in message.text.split(' ')]
			import lab4 as l
			res, k, iv = l.solve(*params)
			if type(k) == str: b.send_message(t, text=k)
			else:
				md = """*x* : _{}_\n""".format(res)
				md1 = """*Iterations* - _{}_""".format(k)
				md2 = """*Iter values* - _{}_""".format("\n".join([str(i) for i in iv]))
				b.send_message(t, text=md, parse_mode='Markdown')
				b.send_message(t, text=md1, parse_mode='Markdown')
				b.send_message(t, text=md2, parse_mode='Markdown')
		except ValueError: b.send_message(t, text="Wrong input")

@b.callback_query_handler(func=lambda call: True)
def cb(call):
	t = to(call.message); global current 
	if call.data == "equ":
		current = 'equ'
		md = """
		*Введіть межі проміжку :*
		*a* - _нижня межа_
		*b* - _верхня межа_
		*eps* - _допустима похибка_
		"""
		b.send_message(t, text=md, parse_mode="Markdown")

b.polling(none_stop=True)