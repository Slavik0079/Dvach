def main():

	import re, random, platform, os, sys,codecs, site, webbrowser

	

	try:	
		from Modules.Logo import Welcome

	except ModuleNotFoundError:

		from dvach.Modules.Logo import Welcome

	

	welcome = Welcome()

	print(welcome.Logo)

	while True:

		try:

			Dict={}

			try:

				f1 = codecs.open('dvach/data/Толковый_словарь_Даля.txt','r',"utf8")

			except FileNotFoundError:

				f1 = codecs.open('data/Толковый_словарь_Даля.txt','r',"utf8")

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

			#

			Input=str(input('\n\n\033[38;5;208mВведи предложение:\033[0m ')).lower()



			for key in Dict:

				random_1 = random.randint(20,246)
				
				random_2 = int(random_1 - 7)

				random_finish="\033[38;5;"+str(random_1)+";48;5;"+str(random_2)+"m"
				
				closure="\033[0m"

				Input=re.sub(key,random_finish+Dict[key]+closure,Input)

			print(f'\n\033[38;5;46mСкопируй данное предложение:\033[0m {Input}\n')

		except KeyboardInterrupt:

			print('\n\n\033[38;5;226mС наступающим анон ;)\033[0m\n\n')

			try:

				file = codecs.open('dvach/data/Надо_быть_добрее.txt','r',"utf8")

			except FileNotFoundError:

				file = codecs.open('data/Надо_быть_добрее.txt','r',"utf8")

			bud_dobree = file.read()

			file.close()

			if bud_dobree != 'Надо_быть_добрее':
				try:

					file = codecs.open('dvach/data/Надо_быть_добрее.txt','w',"utf8")

					file.write('Надо_быть_добрее')

				except FileNotFoundError:

					file=codecs.open('data/Надо_быть_добрее.txt','w',"utf8")

					file.write('Надо_быть_добрее')

				webbrowser.open('https://youtu.be/vEN0qUfZk4c', new=2, autoraise=True)

				file.close()

				break

				sys.exit(0)

			else:

				file.close()

				break

				sys.exit(0)

if __name__ == '__main__':

	

	main()