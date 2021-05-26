import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "-memory", type=int, default=2)
parser.add_argument("-i", "-dictionary", default='dict/italian.txt')
parser.add_argument("-o", "-matrix")
args = parser.parse_args()

if args.o == None:
	if not os.path.isdir('markov'):
		os.mkdir('markov')
	outputfile = 'markov/markovmatrix'+str(args.m)+'.json'
else:
	outputfile = args.o

def removedup(a,number):
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
	return removedup(a,number)

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

f = open(args.i, 'r')
lines = f.readlines()
for l in lines:
	for i in range(len(l)):
		if i == 0:
			matrix[''][l[0]] += 1
		else:
			a = l[i-1]
			b = l[i]
			if not b in letters:
				matrix[a]['-1'] += 1
				break
			else:
				matrix[a][b] += 1
f.close()

for i in matrix:
	s = sum(matrix[i].values())
	for j in matrix[i]:
		if s != 0:
			matrix[i][j] /= s

g = open(outputfile,'w')
print(json.dumps(matrix), file=g)
g.close()
