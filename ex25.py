def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	print(words)
break_words("Hello world! I am Python.")

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	word= words.pop(0)
	print(word)

def last_word(words):
	word = words.pop(-1)
	print(word)
	
def sort_sentence(sentence):
	words = break_words(sentence)
	sentence = sort_words(words)
	return sentence
	
def first_and_last_word(sentence):
	words = break_words(sentence)
	first_word(words)
	last_word(words)
	return print_first_word
	return print_last_word
def first_last_sort(sentence):
	new= sort_sentence(sentence)
	first_word(words)
	last_word(words)
	