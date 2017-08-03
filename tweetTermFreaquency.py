import operator 
import json
from collections import Counter
from preProcessTweets import *
from nltk.corpus import stopwords
import string

from nltk import bigrams 
 

 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['n','RT', 'via', 'Donald', 'Trump']

listOfTokensList = tokenizeTweetDump()
count_all = Counter()
terms_only = []
for tokenList in listOfTokensList:
	terms_all = [term for term in tokenList]
	terms_stop = [term for term in tokenList if term not in stop]
	# Count terms only once, equivalent to Document Frequency
	terms_single = set(terms_all)
	# Count hashtags only
	terms_hash = [term for term in tokenList if term.startswith('#')]
	#Count terms only (no hashtags, no mentions)
	terms_only = [term for term in tokenList if term not in stop and not term.startswith(('#', '@', 'u'))] 
	# mind the ((double brackets))
	# startswith() takes a tuple (not a list) if 
	# we pass a list of inputs
	terms_bigram = bigrams(terms_only)
	count_all.update(terms_bigram)

print(count_all.most_common(10))