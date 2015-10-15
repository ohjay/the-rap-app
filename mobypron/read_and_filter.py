rap_list = open("mobypron_new.txt", 'r')
target = open('rap_vocab_list.txt', 'a')

with open ("websters-dictionary.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

with open("mobypron_new.txt") as myfile2:
    content = myfile2.readlines()

for line in content:
    if (line.split(":")[0][2:]).upper() in data:
        target.write(str(line) + '\n')
        print(line)

rap_list.close()
target.close()
