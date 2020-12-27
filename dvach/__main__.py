import re, random, platform, os, sys,codecs, site, webbrowser

def main():

	packages = os.listdir(site.getsitepackages()[1])

	if 'dvach' not in packages:
		
		from Modules.Logo import Welcome

	else:

		from dvach.Modules.Logo import Welcome


	welcome = Welcome()

	print(welcome.Logo)

	while True:

		try:

			Dict={}

			f1 = codecs.open('Толковый_словарь_Даля.txt','r',"utf8")

			for i in f1:
				list = re.findall(r'(.*):(.*)',str(re.sub('\\r\\n','',i)))

				Dict[list[0][0]]=list[0][1]

			f1.close()



			words=[word for word in Dict]

			#print(len(words))

			counter=0

			print(f'\n\nДля составления предложений, используй следующие \033[38;5;208mслова\033[0m/\033[38;5;226mсловосочетания\033[0m:\n\n')

			for i in words:

				counter+=1

				if words.index(i) == 0:

					print(f'[\033[38;5;231m{i}\033[0m',end=', ')

				if (counter -1) % 5 != 0:

					print(f'\033[38;5;231m{i}\033[0m',end=', ')

				if (counter-1) % 5 == 0 and words.index(i) !=  0:

					print(f'\n\n\033[38;5;231m{i}\033[0m',end=', ')

				if (counter) == len(words):

					print(f'{i}]')

					break

			#

			Input=str(input('\n\n\033[38;5;208mВведи предложение:\033[0m ')).lower()



			for key in Dict:

				random_1 = random.randint(20,246)
				
				random_2 = int(random_1 - 4)

				random_finish="\033[38;5;"+str(random_1)+";48;5;"+str(random_2)+"m"
				
				closure="\033[0m"

				Input=re.sub(key,random_finish+Dict[key]+closure,Input)

			print(f'\n\033[38;5;46mСкопируй данное предложение:\033[0m {Input}\n')

		except KeyboardInterrupt:

			print('\n\n\033[38;5;226mС наступающим анон ;)\033[0m\n\n')

			file = codecs.open('Надо_быть_добрее.txt','r',"utf8")

			bud_dobree = file.read()

			file.close()

			if bud_dobree != 'Надо_быть_добрее':

				file = codecs.open('Надо_быть_добрее.txt','w',"utf8")

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