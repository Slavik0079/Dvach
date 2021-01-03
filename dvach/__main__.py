def main():

	import re, random, platform, os, sys,codecs, site, webbrowser
	from pathlib import Path

	

	try:	
		from Modules.Logo import Welcome
		from Modules.Color import color

	except ModuleNotFoundError:

		from dvach.Modules.Logo import Welcome
		from dvach.Modules.Color import color

	

	welcome = Welcome()

	print(welcome.Logo)

	print('\nДля выхода: \033[38;5;196mCtrl + C\033[0m\n')

	while True:

		try:

			Dict={}

			try:

				f1 = codecs.open('Толковый_словарь_Даля.txt','r',"utf8")

			except FileNotFoundError:

				txt = str(Path(__file__).parent)+'/Толковый_словарь_Даля.txt'

				f1 = codecs.open(txt,'r','utf8')


			for i in f1:
				list = re.findall(r'(.*):(.*)',str(re.sub('\\r\\n','',i)))

				Dict[list[0][0]]=list[0][1]

			f1.close()



			words=[word for word in Dict]

			counter=0

			

			print(f'\n\n\033[38;5;231mДля составления предложений, используй следующие\033[0m \033[38;5;208mслова\033[0m/\033[38;5;226mсловосочетания\033[0m:\n\n')

			for i in words:

				counter+=1

				if words.index(i) == 0:

					print(f'[\033[38;5;231m{i}\033[0m',end=', ')

				if (counter-1) % 5 != 0:

					print(f'\033[38;5;231m{i}\033[0m',end=', ')

				if (counter-1) % 5 == 0 and words.index(i) != 0 and words.index(i)!=-2:

					print(f'\n\n\033[38;5;231m{i}\033[0m',end=', ')

				if (counter) == len(words):

					print(f'\033[38;5;231m\b\b]\033[0m')

					break

			

			Input=str(input('\n\n\033[38;5;208mВведи предложение:\033[38;5;231m ')).lower()



			for key in Dict:

				number = str(random.randint(0,4))

				col = color(number)

				random_finish= col[0]+col[1]
				
				closure="\033[0m"

				Input=re.sub(key,random_finish+Dict[key]+closure,Input)

			print(f'\n\033[38;5;46mСкопируй данное предложение:\033[0m {Input}\n')

		except KeyboardInterrupt:

			print('\033[0m')

			print('\n\n\033[38;5;226mС Новым Годом, Анон ;)\033[0m\n\n')

			bud_dobree = None

			try:

				file = codecs.open('Надо_быть_добрее.txt','r',"utf8")

				bud_dobree = file.read()

				file.close()

			except FileNotFoundError:

				txt = str(Path(__file__).parent)+'/Надо_быть_добрее.txt'

				f1 = codecs.open(txt,'r','utf8')


			

			if bud_dobree != 'Надо_быть_добрее':
				
				try:

					file = codecs.open('Надо_быть_добрее.txt','w',"utf8")

				except FileNotFoundError:

					txt = str(Path(__file__).parent)+'/Надо_быть_добрее.txt'

					f1 = codecs.open(txt,'r','utf8')


				file.write('Надо_быть_добрее')

				webbrowser.open('https://youtu.be/vEN0qUfZk4c', new=2, autoraise=True)

				file.close()

				break

				sys.exit(0)

			else:

				break

				sys.exit(0)

if __name__ == '__main__':


	main()