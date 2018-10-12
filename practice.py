def break_word(f):
	word= f.split()
	return word
def sort(word):
	words= sorted(word)
	return words
def first_word(words):
	word= words.pop(0)
	print(word)
def last_word(words):
	word = words.pop(-1)
	print(word)
def sort_sentence(sentence):
	break_sen= break_word(sentence)
	sort_sen = sort(break_sen)
	return sort_sen                         
def first_last_sentence(sentence):
	sen = sort_sentence(sentence)
	first_word(sen)
	last_word(sen)
	
