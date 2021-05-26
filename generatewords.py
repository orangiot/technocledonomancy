import json
import numpy as np
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "-memory", type=int, default=2)
parser.add_argument("-l", "-maxlength", type=int, default=19)
parser.add_argument("-w", "-words", type=int, default=10)
parser.add_argument("-r", "-random", default='True')
parser.add_argument("-i1","-seed", default='seeds/portal.jpg')
parser.add_argument("-i2", "-matrix")
args = parser.parse_args()

if args.i2 == None:
	matrixfile = 'markov/markovmatrix'+str(args.m)+'.json'
else:
	matrixfile = args.i2
	
if args.r == 'False':
	rnd = False
else:
	rnd = True

def removedup(a):
	if a == []:
		return a
	a = sorted(a)
	b = []
	last = '-2'
	for i in a:
		if i != last:
			b.append(i)
		last = i
	return b

def permrip(letters,number):
	if number == 0:
		return ['']
	a = []
	b = permrip(letters,number-1)
	for p in b:
		for l in letters:
			a += [p+l,l+p]
	return removedup(a)

# a = chr(97), z = chr(122)
letters = []
for i in range(97,123):
	letters.append(chr(i))
letters += ['','-1']
column = {}
matrix = {}
for i in letters:
	column[i] = 0
for combination in permrip(letters,args.m):
	matrix[combination] = column

f = open(matrixfile,'r')
matrix = json.load(f)
f.close()

def state(word,mem):
	return word[-mem:]

def randomfromhash(s):
	a = ''
	for c in s:
		a += str(ord(c)%10)
	l = len(a)
	return int(a)/10**l

if rnd == False:
	g = open(args.i1,'rb')
	lines = g.readlines()
	seed = ''
	for l in lines:
		seed += str(l)
	h = hashlib.new('ripemd160')
	h.update(seed.encode('UTF-8'))

for counter in range(args.w):
	word = ''
	while (len(word)<3):
		word = ''
		a = ''
		while (a != '-1'):
			last = state(word,args.m)
			if rnd == False:
				seed = h.hexdigest()
				h.update(seed.encode('UTF-8'))
				r = randomfromhash(seed)
			else:
				r = np.random.random()
			s = 0
			for l in letters:
				s += matrix[last][l]
				if (r <= s):
					a = l
					if a != '-1':
						word += a
					break
			if len(word) > args.l:
				word = ''
	print(word)
