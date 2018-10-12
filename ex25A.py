def break_words(words):
	word = words.split(' ')
	return word
	
def sort_words(words):
	word= sorted(words)
	return word
	
sort_words("Hello world")

def first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print(word)
	
def last_word(words):
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	words = break_words(sentence)
	sort = sort_words(words)
	return sort
sort_sentence("Hello world")

def first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	first_word(words)
	last_word(words)
first_and_last("who is he")

def first_and_last_sort_sentence(sentence):
	sen = sort_sentence(sentence)
	first_word(sen)
	last_word(sen)
first_and_last_sort_sentence("Hello World! How are you?")