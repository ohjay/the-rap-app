rap_list = open("mobypron.txt", 'r+')

target = open('rap_vocab_list.txt', 'a')

print('step 1')

for line in rap_list:
	if (line.split(":")[0]).upper() in open("websters-dictionary.txt").read():
		target.write(str(line) + '\n')
		print(line)
		print('step 2')
	open("websters-dictionary.txt").close()


target.write('step 3')

rap_list.close()
target.close()