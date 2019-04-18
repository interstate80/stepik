#!/bin/python

areas = {
	'global': {
		'parent': None,
		'vars': None,
		},
	}

def add(var, area):
	areas[area]['vars'] = set(var)
	
def create(area, parent):
	addset = {
		'parent': parent,
		'vars': None,
	}
	areas[area] = addset
	
def get(var, area):
	if area in areas.keys():
		if var in areas[area]['vars']:
			print(areas[area]['parent'])
		else:
			print('None')
