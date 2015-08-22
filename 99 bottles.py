song = '''{whole} bottles of beer on the wall, {whole} of beer...
If one of those bottles should happen to fall, {broken} bottles of beer on the wall
'''

for bottles in range(99,0,-1):
	print song.format(whole=bottles, broken=bottles-1)
