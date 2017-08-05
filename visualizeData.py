import vincent
from tweetTermFreaquency import *

word_freq = getWordFreq()
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')

#bar.to_json('term_freq.json', html_out=True, html_path='chart.html')


