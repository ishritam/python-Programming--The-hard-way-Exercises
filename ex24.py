print("let's do somme practice")
print("let me know \' :what does it do.")  #\' is use to print a '
print("tab or 4 spaces \t i am tab")
print("i am the next line \n next line")

poem = """What if i told you \n i am in love with you \n what if i told you \t i am in love with python and what is \' it"""

print("i want to write a poem: {}".format(poem))
print("same as f\"\"")
print(f"i want to write a poem {poem}")

def secreat_formula(started):
	cock = started *2
	sprite = started * 3
	maza = started * 4
	return cock,sprite,maza
started=1000

print(secreat_formula(started))
cock,sprite,maza = secreat_formula(started)

print(f"we would have {cock}->cocacola, {sprite}->sprite and {maza}->maza")

started =started + 1000 #the started value will be 2000
print(f"we would have {cock}->cocacola, {sprite}->sprite and {maza}->maza")
