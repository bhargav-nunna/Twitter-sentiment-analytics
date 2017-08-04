import operator 
import json
from collections import Counter
from preProcessTweets import *
from nltk.corpus import stopwords
import string

from nltk import bigrams 
from collections import defaultdict
# remember to include the other import from the previous post

 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['n','RT', 'via', 'Donald', 'Trump']

listOfTokensList = tokenizeTweetDump()
count_all = Counter()
terms_only = []
com = defaultdict(lambda : defaultdict(int))

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
	# Build co-occurrence matrix
	for i in range(len(terms_only)-1):
		for j in range(i+1, len(terms_only)):
			w1, w2 = sorted([terms_only[i], terms_only[j]])
			if w1 != w2:
				com[w1][w2] += 1
	terms_bigram = bigrams(terms_only)
	count_all.update(terms_only)
print(count_all.most_common(10))
 
com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])
    
## co-occurence for a search word
#search_word = sys.argv[1] # pass a term as a command-line argument
#count_search = Counter()
#for line in f:
#    tweet = json.loads(line)
#    terms_only = [term for term in preprocess(tweet['text']) 
#                  if term not in stop 
#                  and not term.startswith(('#', '@'))]
#    if search_word in terms_only:
#        count_search.update(terms_only)
#print("Co-occurrence for %s:" % search_word)
#print(count_search.most_common(20))"""