import nltk
import math
from operator import sub
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
nonstopwords=[];
# Here wear eopening the file 
file1 = open('A5Q6.txt').read()
a= sent_tokenize(file1)
b=[]
for i in a:
    b.append(len(i.split()))
stopwords = stopwords.words("english")
# here we are eliminating the stopwords from each sentence 
for i in file1.lower().split():
    if i not in stopwords:
        nonstopwords.append(i)
# here we are trying to join all the sentences and forming text
text=" ".join(str(i) for i in nonstopwords)
#again we are performing the sentence tokenization for text
tokenize=sent_tokenize(text)
# performing the sentence tokenization
tokenized_sentences=sent_tokenize(text);
numofwords_list=[]
entrophy_list=[]
# reference from the Class Notes in lesson 10
# defining the entropy function
def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])

# calculating the number of non stop words in each sentences and storing it in a list
for i in tokenized_sentences:
    numofwords_list.append(len(i.split()))
#calculating the entropy of each sentences and storing it in a list
for i in tokenize:
    entrophy_list.append(entropy(i))
print("Sentences in Short"+"                    "+"#ofwords"+"              "+"Entropy")

# here printing the number of non stop words in each sentence, and its entropy
for i in range(len(tokenized_sentences)):
    x=tokenized_sentences[i]
    wl=numofwords_list[i]
    el=entrophy_list[i]
    print(x[:30],"\t\t",wl,"\t\t",el)
# reference http://stackoverflow.com/questions/32541659/plotting-histogram-with-given-x-and-y-values
# Drawing the histogram diagram 
plt.bar(numofwords_list,entrophy_list,align='center') # A bar chart
plt.xlabel('Number of words')
plt.ylabel('Entropy')
for i in range(len(entrophy_list)):
    plt.hlines(entrophy_list[i],0,numofwords_list[i]) # Here you are drawing the horizontal lines
plt.show()
    
    




    

    
