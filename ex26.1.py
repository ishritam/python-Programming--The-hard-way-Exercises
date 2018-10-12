def secreat_formula(secreat):
	jelly_bean= secreat * 5
	bean = jelly_bean / 2
	cradit = bean - 20
	return jelly_bean,bean,cradit
secreat = 10

jelly,bean,cradit = secreat_formula(secreat)
formula =  secreat_formula(secreat)
print("There are {}jelly, {}bean, {}cradit are there:".format(*formula))