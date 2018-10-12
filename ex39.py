states= {"Odisha": "OD","Maharastra":"MH","Utterpradesh":"UP"}
capital = {"OD":"BHUBANESWER","MH":"MUMBAI","UP":"BHOPAL"}
for state,abbrevation in list(states.items()):
	print(f"{state}'s abbrevation is {abbrevation}")
for capitals,abbrevation in list(capital.items()):
	print(f"{abbrevation}'s capital is {capitals}")  #Never ever use the same variable or names in the FOR LOOP for decl.
#print the both
for state,abbrevation in list(states.items()):
	print(f"{state}'s abbrevation is {abbrevation} and capital is {capital[abbrevation]}")
