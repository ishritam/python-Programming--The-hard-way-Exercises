def break_words(stuff):
	word= stuff.split(' ')
	return word

def sort_word(words):
	return sorted(words)
	
def first_word(words):
	word = words.pop(0)
	print (word)
	
def last_word(words):
	word = words.pop(-1)
	print(word)
	
def sorted_sentence(sentence):
	word = break_words(sentence)
	return sort_word(word)
	
	  #if you are getting a --> 'NoneType' object has no attribute 'pop' <-- eroor then Check for the Return and Print. There will be an error in it. Check it and correct it.
def first_and_last(sentence):
	word = sorted_sentence(sentence)
	first_word(word)
	last_word(word)