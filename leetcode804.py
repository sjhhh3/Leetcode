
mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
dic = {}
list = ["gin", "zen", "gig", "msg"]
moslist = []


for index, letter in enumerate(range(97,123)):
    dic[chr(letter)] = mos[index]

for word in list:
    mosword = ""
    for letter in word:
        mosword += dic[letter]

    moslist.append(mosword)

print(len(set(moslist)))