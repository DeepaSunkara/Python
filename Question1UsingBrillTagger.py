import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string
from io import StringIO
from nltk.corpus import brown
file = open('1865-Lincoln.txt','r') # openning a 1865-Lincoln Text file
a=file.read() # reading the content from the text file
words = 0
sentences = 0
print("The Number of sentences and words in  text file 1865-Lincoln.txt are:")
Ltokenized_sentences = sent_tokenize(a) # here we are performing the sentence tokenization
for i in Ltokenized_sentences:
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
punctuationSet.add("-")
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



# From here we are performing actions on 1945-Roosevelt text file

file = open('1945-Roosevelt.txt','r') # openning a 1865-Lincoln Text file
b=file.read() # reading the content from the text file
words = 0
sentences = 0
print("\nThe Number of sentences and words in text file 1945-Roosevelt.txt are:")
Rtokenized_sentences = sent_tokenize(b) # here we are performing the sentence tokenization
for i in Rtokenized_sentences:
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


# The following part of code is taken as a reference from http://www.nltk.org/api/nltk.tag.html#nltk.tag.brill.brill24
# Preparing the brill tagger
def brill_tagger(tagged_sentences):
    wordings = [
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
        (r'(The|the|A|a|An|an)$', 'AT'),
        (r'.*able$', 'JJ'),
        (r'.*ness$', 'NN'),
        (r'.*ly$', 'NN'),
        (r'.*ing$', 'VBG'),
        (r'.*ed$', 'VBD'),
        (r'.*ould$', 'MD'),
        (r'.*ment$', 'NN'),
        (r'.*ful$', 'JJ'),
        (r'.*ious$', 'JJ'),
        (r'.*ble$', 'JJ'),
        (r'.*ic$', 'JJ'),
        (r'.*ive$', 'JJ'),
        (r'.*est$', 'JJ'),
        (r'.*ould$', 'MD'),
    ]

    # the part of code is taken as a reference from http://stackoverflow.com/questions/14802442/how-to-use-a-regex-backoff-tagger-in-python-nltk-to-override-nns
    # here we are using the unigram and regex taggers as backoffs for brill tagger 
    regex_tagger = nltk.tag.RegexpTagger(wordings)
    unigram_tagger = nltk.UnigramTagger(tagged_sentences, backoff=regex_tagger)
    model = nltk.tag.brill.brill24()
    brill_trainer = nltk.tag.brill_trainer.BrillTaggerTrainer(unigram_tagger, model)
    brill_tagger = brill_trainer.train(tagged_sentences)
    return brill_tagger

# here the following function takes a sentence and tags each word in the sentence using word/tag format
def tagged_sentences(tagger, sentences):
    tokenwords = nltk.word_tokenize(sentences)
    taggedword_tokens = tagger.tag(tokenwords)
    a = []
    for word,tag in taggedword_tokens:
        if word == tag: # when the word is equal to the tag or '.' then the tag wil become none
            tag = None
        elif word == '.':
            tag =None
        taggedword = word
        if tag != None: # Here the tag which is not equal to none then the word will be added to the list named 'a' along with it's tag 
            taggedword = word  + "\\" + tag + ',' # this part of code taken reference from http://nltk.sourceforge.net/doc/en/ch03.html 
        a.append(taggedword)
    return ' '.join(a)

# This function that takes all tokenized sentences and returns a list of tagged sentences
def gettagged_sentences(tagger, tokenizedsentences): 
    b = []
    for i in tokenizedsentences:
        taggedsentence = tagged_sentences(tagger, i)# here the process of tagging a tokenized sentence will take place 
        b.append(taggedsentence)
    return b

# this function is mainly used for accepting particular Text file and its tagged sentences and writing them into particular tagged text files.
def write_to_file(filename, taggedsentences):
    with open(filename, 'w') as file1:
        for i in taggedsentences:
            file1.write(i + '\n')

# the  following part of code for categories is taken as  a reference from http://web.mit.edu/6.863/python/nltk-0.9.7/nltk/test/corpus.doctest in Categorized Corpora section
brown_tagged_sentences = nltk.corpus.brown.tagged_sents(categories=['government', 'news'])
print("\nConducting parts of speech using Brill Tagger. This may take 2-3 minutes")
brilltagger = brill_tagger(brown_tagged_sentences)
lincoln_tagged_sentences = gettagged_sentences(brilltagger, Ltokenized_sentences)
roosevelt_tagged_sentences = gettagged_sentences(brilltagger, Rtokenized_sentences)
write_to_file('tagged_1865-Lincoln.txt', lincoln_tagged_sentences )
write_to_file('tagged_1945-Roosevelt.txt',roosevelt_tagged_sentences)
print("\nFinished, now the tagged 1865-Lincoln text file and tagged 1945-Roosevelt text file  can be viewed in the folder ")


