paragraph_text = '''
For a minute or two she stood looking at the house, and wondering what to do next, when suddenly a footman in livery came running out of the wood—(she considered him to be a footman because he was in livery: otherwise, judging by his face only, she would have called him a fish)—and rapped loudly at the door with his knuckles. It was opened by another footman in livery, with a round face, and large eyes like a frog; and both footmen, Alice noticed, had powdered hair that curled all over their heads. She felt very curious to know what it was all about, and crept a little way out of the wood to listen.
The Fish-Footman began by producing from under his arm a great letter, nearly as large as himself, and this he handed over to the other, saying, in a solemn tone, ‘For the Duchess. An invitation from the Queen to play croquet.’ The Frog-Footman repeated, in the same solemn tone, only changing the order of the words a little, ‘From the Queen. An invitation for the Duchess to play croquet.’
Then they both bowed low, and their curls got entangled together.
Alice laughed so much at this, that she had to run back into the wood for fear of their hearing her; and when she next peeped out the Fish-Footman was gone, and the other was sitting on the ground near the door, staring stupidly up into the sky.
Alice went timidly up to the door, and knocked.
‘There’s no sort of use in knocking,’ said the Footman, ‘and that for two reasons. First, because I’m on the same side of the door as you are; secondly, because they’re making such a noise inside, no one could possibly hear you.’ And certainly there was a most extraordinary noise going on within—a constant howling and sneezing, and every now and then a great crash, as if a dish or kettle had been broken to pieces.
‘Please, then,’ said Alice, ‘how am I to get in?’
‘There might be some sense in your knocking,’ the Footman went on without attending to her, ‘if we had the door between us. For instance, if you were inside, you might knock, and I could let you out, you know.’ He was looking up into the sky all the time he was speaking, and this Alice thought decidedly uncivil. ‘But perhaps he can’t help it,’ she said to herself; ‘his eyes are so very nearly at the top of his head. But at any rate he might answer questions.—How am I to get in?’ she repeated, aloud.
‘I shall sit here,’ the Footman remarked, ‘till tomorrow—’
At this moment the door of the house opened, and a large plate came skimming out, straight at the Footman’s head: it just grazed his nose, and broke to pieces against one of the trees behind him.'''

def counts(my_list):
    counts = dict()
    for item in my_list:
        counts.setdefault(item,0)
        counts[item] += 1
    return max(counts.items(), key=lambda x: x[1])

punc = [',','.',"’","‘","—",'?',':','(',')','\n']
for pun in punc:
    paragraph_text = paragraph_text.replace(pun,'')

print(counts(paragraph_text.split(' ')))


