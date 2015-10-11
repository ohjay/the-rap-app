rap_list = open("mobypron_new.txt", 'r')
target = open('rap_vocab_list.txt', 'a')

with open ("websters-dictionary.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

with open("mobypron_new.txt") as myfile2:
	content = myfile2.readlines()

print(len(content))


rap_list.close()
target.close()