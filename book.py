import re  #import the re library for regular expressions
import collections #import the collections library, that allows us to count the occurrences of words.

text = open('book.txt').read().lower()  #open the book txt file, use the read method, have it all in lowercase. 
words = re.findall('\w+', text)   #we're going to use the regular expressions findall() method with the pattern here. 
print(collections.Counter(words).most_common(10))  #we're going to use the counter() method from our collections, and we're also going to find the ten most common words.
