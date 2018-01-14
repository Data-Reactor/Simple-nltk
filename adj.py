
# -*- coding: utf-8 -*-
import nltk
#from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.tag import pos_tag
import collections


book = open('input.txt')

readl = book.readline()
#english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '!', '@', '#', '%', '$', '*']
ADJ = []
#PRP = []

while readl:

	ff = word_tokenize(readl)
	for a,b in pos_tag(ff):
		if b =='JJ' or b == 'ADJ':
			ADJ.append(a)



	readl = book.readline()


	
book.close()


adj_count = open('adj count','w')
word_file = open('word_file','w')
count_file = open('count_file','w')

for i in collections.Counter(ADJ).most_common():


		adj_count.write(i[0])
		word_file.write(i[0])
		adj_count.write(' ')
		adj_count.write(str(i[1]))
		count_file.write(str(i[1]))
		adj_count.write('\n')
		word_file.write('\n')
		count_file.write('\n')


adj_count.close()
word_file.close()
count_file.close()





write_file = open('write','w')




for i in ADJ:
	write_file.write(i)
	write_file.write('\n')



write_file.close()



#make WordCloud
from wordcloud import WordCloud
file = open("write","r").read()
wordcloud = WordCloud(background_color="white",width=800, height=800, margin=2).generate(file)

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('wordcloud.png')

file.close()
