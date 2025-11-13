def get_password_variants(password):
	pass_variants = []
	substitutions = {
		'a': ['@', '4', 'A'],
		'e': ['3', 'E'],
		'i': ['1', '!', 'I'],
		'o': ['0', 'O'],
		's': ['$', '5', 'S'],
		't': ['7', 'T'],
		'z': ['2', 'Z'],
	}

for i in range (len(password)):
	if password[1] in substitions:
		for sub in substitions[password[i]]:
			pass_variant = password[:i] + sub + passwpord[i+1:]
			pass_variantes.append(pass_variant)

pass_variants.append(password + '!')
pass_variants.append(password + '123')
pass_variants.append(password + '@')
pass_variants.append(password + '#')
pass_variants.append(password + '$')
pass_variants.append(password + '%')
pass_variants.append(password + '&')
pass_varients.append(password + '*')
pass_varients.append(password + '-')
pass_varrients



