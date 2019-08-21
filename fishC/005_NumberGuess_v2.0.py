import random
import os

while 1:
	print ('Welcome to the simplest game NumberGuess\n')
	#输入数值
	tempt = input('Could you guess my fortune number?(hint: from 1 to 10)\n')
	guess = int(tempt)

	#定义游戏规则
	answer = random.randint(1,10)
	times_limit = 5
	times = 1

	while guess != answer and times < times_limit:
		#猜错了
		if guess > answer:
				print('No, too large.')
		if guess < answer:
			print('No, too small.')
		
		#计数器加一
		times += 1
		if times == times_limit:
			print('You have no more chances.')
		print('you have ' + str(times_limit) + ' chances, now you have ' + str(times_limit-times) + ' more times.')
		
		#重新输入数值
		tempt = input('Try again please\n')
		guess = int(tempt)
		
		#猜对了
		if guess == answer:
			print('Yes, it is!\n')
			
	print('Game over, welcome back.')
	os.system("pause")
	os.system('cls')
