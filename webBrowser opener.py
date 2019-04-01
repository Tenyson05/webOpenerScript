import webbrowser
import time
import random


while True:
	sites = random.choice(['https://www.bugcrowd.com/', 'https://myanimelist.net', 'https://kissanime.ru', 'https://www.amazon.com/', 'https://www.youtube.com'])
	webbrowser.open_new(sites)
	seconds = random.randrange(5, 20)
	time.sleep(seconds)