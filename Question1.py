import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.tag import UnigramTagger
from collections import Counter
import sys
import string
from io import StringIO
file = open('1865-Lincoln.txt','r') # openning a 1865-Lincoln Text file
a=file.read() # reading the content from the text file
words = 0
sentences = 0
print("The Number of sentences and words in  text file 1865-Lincoln.txt are:")
tokenized_sentences = sent_tokenize(a) # here we are performing the sentence tokenization
for i in tokenized_sentences:
    sentences = sentences + 1 # here we are keeping a count on the number of sentences in a text file
print("Sentences = "+str(sentences))
tokenized_words = word_tokenize(a) # here we are performing the word tokenization
for i in tokenized_words:
    words = words + 1 # here we are keeping a count on the number of words in a text file 
print("Words = "+str(words))
stop_words = set(stopwords.words("english")) # Here we are choosing the stopwords of English language
d=[]
word = word_tokenize(a)
for i in word:
    if i not in stop_words:
        d.append(i) # here we are storing all the non stopwords in a list named 'd'
print("The number of non-stop words (including punctuations) in 1865-Lincoln text file = " +str(len(d)))
final_text=[]
# now we are adding some puncutuation symbols to the pre defined function i.e punctuationSet
punctuationSet = set(string.punctuation)
punctuationSet.add("--")
punctuationSet.add("``")
punctuationSet.add("''")
punctuationSet.add("Fellow-Countrymen")
punctuationSet.add("One-eighth")
for i in d:
    if i not in punctuationSet: # here we are eliminating the punctuations and words which contains punctuations in middle 
        final_text.append(i)
print("The number of non-stop words (with no punctuations) in 1865-Lincoln text file  = " +str(len(final_text)))
print("\nThe frequency distribution of unique words in 1865-Lincoln text file is given below :")
print('\n')
LFD = nltk.FreqDist(final_text) # we are trying to find out the unique words number
print(LFD)
print('\n')
frequency_counting = Counter(final_text) # here we are calculating the frequency distribution of unique words 
print(frequency_counting)
print("\n")
for i in string.punctuation:
    a = a.replace(i,"")
s = stopwords.words('english')
w = nltk.word_tokenize(a)
filtered_words = [] 
filtered_words = [i for i in w if i not in s]
fdist = nltk.FreqDist(filtered_words)#this function is used to count the frequency distribution of the most commonly used words
print("The top 20 unique words in the 1865-Lincoln.txt file are: ")
list1=[]
for (ww, frequency) in fdist.most_common(20):
    list1.append(ww)
print(list1)

# the following part of code is taken reference from http://www.nltk.org/_modules/nltk/tag/sequential.html#UnigramTagger

# The following code is mainly used for conducting parts of speech for 1865-Lincoln Text file using unigram tegger 
print("\nConducting part-of-speech tagging for 1865-Lincoln text file, this may take few minutes")
unigram_tagger = UnigramTagger(brown.tagged_sents(categories='news'))
tokenized_sentences = sent_tokenize(a) # here we are performing the sentence tokenization
llist1=[]
for i in tokenized_sentences:
    tokenized_words = word_tokenize(i)
    tagged_words = unigram_tagger.tag(tokenized_words)
    llist1.append(tagged_words)
tagged_file=" ".join(str(i) for i in llist1)
files=open("Unigram_tagged_1865-Lincoln.txt","w")
files.write(tagged_file)
print("\nUnigram_tagged_1865-lincoln.txt file finished you can view in the folder")


    
# From here we are performing actions on 1945-Roosevelt text file

file = open('1945-Roosevelt.txt','r') # openning a 1865-Lincoln Text file
b=file.read() # reading the content from the text file
words = 0
sentences = 0
print("\nThe Number of sentences and words in text file 1945-Roosevelt.txt are:")
tokenized_sentences = sent_tokenize(b) # here we are performing the sentence tokenization
for i in tokenized_sentences:
    sentences = sentences + 1 # here we are keeping a count on the number of sentences in a text file
print("Sentences = "+str(sentences))
tokenized_words = word_tokenize(b) # here we are performing the word tokenization
for i in tokenized_words:
    words = words + 1 # here we are keeping a count on the number of words in a text file
print("Words = "+str(words))
stop_words = set(stopwords.words("english")) # Here we are choosing the stopwords of English language
c=[]
word = word_tokenize(b)
for i in word:
    if i not in stop_words:
        c.append(i) # here we are storing all the non stopwords in a list named 'c'
print("The number of non-stop words (including punctuations) in 1945-Roosevelt text file  = " +str(len(c)))
final_text1=[]
# now we are adding some puncutuation symbols to the pre defined function i.e punctuationSet
punctuationSet = set(string.punctuation)
punctuationSet.add("--")
punctuationSet.add("``")
punctuationSet.add("''")
for i in c:
    if i not in punctuationSet: 
        final_text1.append(i) # here we are eliminating the punctuations and storing the words in a list 
print("The number of non-stop words (with no punctuations) in 1945-Roosevelt text file  = " +str(len(final_text1)))
print("\nThe frequency distribution of unique words in 1945-Roosevelt text file is given below :")
print('\n')
RFD = nltk.FreqDist(final_text1) # we are trying to find out the unique words number
print(RFD)
print('\n')
frequency_counting = Counter(final_text1) # here we are calculating the frequency distribution of unique words)
print(frequency_counting)
print("\n")
for i in string.punctuation:
    b = b.replace(i,"")
s = stopwords.words('english')
w = nltk.word_tokenize(b)
filtered_words = [] 
filtered_words = [i for i in w if i not in s]
fdist = nltk.FreqDist(filtered_words)#this function is used to count the frequency distribution of the most commonly used words
print("\nThe top 20 unique words in the 1945-Roosevelt.txt file are: ")
list2=[]
for (ww, frequency) in fdist.most_common(20):
    list2.append(ww)
print(list2)

# the following part of code is taken reference from http://www.nltk.org/_modules/nltk/tag/sequential.html#UnigramTagger

# The following code is mainly used for conducting parts of speech for 1945-Roosevelt Text file using unigram tagger 
print("\nConducting part-of-speech tagging for 1945-Roosevelt text file, this may take few minutes")
unigram_tagger = UnigramTagger(brown.tagged_sents(categories='news'))
tokenized_sentences = sent_tokenize(b) # here we are performing the sentence tokenization
llist1=[]
for i in tokenized_sentences:
    tokenized_words = word_tokenize(i)
    tagged_words = unigram_tagger.tag(tokenized_words)
    llist1.append(tagged_words)
tagged_file=" ".join(str(i) for i in llist1)
files=open("Unigram_tagged_1945-Roosevelt.txt","w")
files.write(tagged_file)
print("\nUnigram_tagged_1945-Roosevelt.txt file finished you can view in the folder")

