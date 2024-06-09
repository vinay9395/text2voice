import requests
import telebot 
bot = telebot.TeleBot("7236081501:AAHyQmRW45_VKsl_Rglo42p63CmwIEMxfHw")
def generate(word):
	cookies = {
	    '_ga': 'GA1.1.1473852622.1717532969',
	    '__gsas': 'ID=d70a29d7e759d6d0:T=1717532990:RT=1717532990:S=ALNI_MaBfaAHd_duSDQplR8-1XQ4RgPBWA',
	    '__gads': 'ID=3f9b506e926994f5:T=1717532975:RT=1717617419:S=ALNI_MbnUdHiE4dVGpTv8SGADSZF3NhC3w',
	    '__gpi': 'UID=00000e4b35a32d75:T=1717532975:RT=1717617419:S=ALNI_MaNIMdj2F6erTknLzjV0cup8jEP_A',
	    '__eoi': 'ID=1c1d5e6fa07aeed4:T=1717532975:RT=1717617419:S=AA-AfjbCZaMR1tNjRVC6r3Ple_Dx',
	    '_ga_H0XGBVF70F': 'GS1.1.1717617407.2.1.1717617464.3.0.1430855070',
	    'FCNEC': '%5B%5B%22AKsRol-5WIn5humdz8ivky_16_E1d5llV4K7TNB2POeZAMdErZJjv0qJjHnISOZH9dbeNHq_14JvlNdI9XbLtaVz_MOMOjkKbovI37ySRyKFf56ucp6UBb0FuJdKQnvidtskhUsm8YdtmmqL-Sz7zAQsd19N87qfZA%3D%3D%22%5D%2Cnull%2C%5B%5B2%2C%22%5Bnull%2C%5Bnull%2C3%2C%5B1717532971%2C858389000%5D%5D%5D%22%5D%5D%5D',
	}
	
	headers = {
	    'authority': 'ttsmp3.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7,ku;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': '_ga=GA1.1.1473852622.1717532969; __gsas=ID=d70a29d7e759d6d0:T=1717532990:RT=1717532990:S=ALNI_MaBfaAHd_duSDQplR8-1XQ4RgPBWA; __gads=ID=3f9b506e926994f5:T=1717532975:RT=1717617419:S=ALNI_MbnUdHiE4dVGpTv8SGADSZF3NhC3w; __gpi=UID=00000e4b35a32d75:T=1717532975:RT=1717617419:S=ALNI_MaNIMdj2F6erTknLzjV0cup8jEP_A; __eoi=ID=1c1d5e6fa07aeed4:T=1717532975:RT=1717617419:S=AA-AfjbCZaMR1tNjRVC6r3Ple_Dx; _ga_H0XGBVF70F=GS1.1.1717617407.2.1.1717617464.3.0.1430855070; FCNEC=%5B%5B%22AKsRol-5WIn5humdz8ivky_16_E1d5llV4K7TNB2POeZAMdErZJjv0qJjHnISOZH9dbeNHq_14JvlNdI9XbLtaVz_MOMOjkKbovI37ySRyKFf56ucp6UBb0FuJdKQnvidtskhUsm8YdtmmqL-Sz7zAQsd19N87qfZA%3D%3D%22%5D%2Cnull%2C%5B%5B2%2C%22%5Bnull%2C%5Bnull%2C3%2C%5B1717532971%2C858389000%5D%5D%5D%22%5D%5D%5D',
	    'origin': 'https://ttsmp3.com',
	    'referer': 'https://ttsmp3.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'msg': word,
	    'lang': 'Salli',
	    'source': 'ttsmp3',
	}
	
	response = requests.post('https://ttsmp3.com/makemp3_new.php', cookies=cookies, headers=headers, data=data).json()
	audio = response["URL"]
	return audio
@bot.message_handler(commands=["start"])
def startt(message):
	bot.reply_to(message ,"اهلًا بك في بوت تحويل النص الى صوت\n ارسل النص الذي تريد تحويله لصوت وانتظر قليلًا")
@bot.message_handler(func=lambda message:True)
def coo(message):
	mess = str(message.text)
	get = generate(mess)
	bot.send_audio(message.chat.id ,get,caption=f"النص : {mess}",reply_to_message_id=message.message_id)
bot.infinity_polling(none_stop=True)