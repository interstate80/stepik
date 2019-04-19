
spaces = {
	'global': {
		'parent': None,
		'vars': set(),
		}
	}

def add_v(sp, vr):
	spaces[sp]['vars'].add(vr)

def create_n(sp, par):
	spaces[sp] = {
		'parent': par,
		'vars': set(),
		}

def get_var(sp, var):
	if sp == "global":
		if var in spaces[sp]['vars']:
			print('global')
		else:
			print('None')
	elif sp in spaces.keys():
		spar = spaces[sp]['parent']
		if var in spaces[sp]['vars']:
			print(sp)
		elif var in spaces[spar]['vars']:
			print(spar)
		else:
			print('None')
	elif var in spaces['global']['vars']:
		print('global')
	else:
		print('None')

def main_loop():
	n = int(input())
	while n != 0:
		cmd, namesp, var = input().split()
		if cmd == "add":
			add_v(namesp, var)
		if cmd == "create":
			create_n(namesp, var)
		if cmd == "get":
			get_var(namesp, var)
		n -= 1

if __name__ == "__main__":
	main_loop()
