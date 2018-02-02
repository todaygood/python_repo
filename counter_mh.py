#!/usr/bin/env python
import collections
from string import punctuation

sentence = "one ,two,three, China,two, one I come from China."

words_count= collections.Counter(sentence.translate(None,punctuation).lower().split())

print(words_count)



