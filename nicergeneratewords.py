import json
import numpy as np
import hashlib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "-memory", type=int, default=2)
parser.add_argument("-l", "-maxlength", type=int, default=19)
parser.add_argument("-w", "-words", type=int, default=10)
parser.add_argument("-r", "-random", default='True')
parser.add_argument("-i1","-seed", default='seeds/portal.jpg')
parser.add_argument("-i2", "-matrix")
parser.add_argument("-hid", "-hidden", type=int, default=1)
parser.add_argument("-i3", "-weights")
parser.add_argument("-t", "-tolerance", type=float, default=0.5)
args = parser.parse_args()

if args.i2 == None:
	matrixfile = 'markov/markovmatrix'+str(args.m)+'.json'
else:
	matrix = args.i2
if args.i3 == None:
	weightsfile = 'rnn/rnnweights'+str(args.hid)+'.h5'
else:
	weightsfile = args.i3
if args.r == 'False':
	rnd = False
else:
	rnd = True

def string2numbers(s):
	s = s.replace('\n','')
	a = [0]*len(s)
	for i in range(len(s)):
		a[i] = ord(s[i]) - ord('a')
	return a

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

#defines the model
model = keras.Sequential()
model.add(layers.LSTM(units=args.hid, input_shape=(None,1)))
model.add(layers.Dense(1))
model.compile(loss = 'mse', optimizer = 'adam')
model.load_weights(weightsfile)

counter = 0
while counter < args.w:
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
	if len(word) <= args.l:
		numberarray = string2numbers(word)
		a = np.zeros((1,len(numberarray),1))
		for i in range(len(numberarray)):
			a[0,i,0] = numberarray[i]
		prediction = model.predict(a)
		if prediction[0] > args.t:
			counter += 1
			print(word,prediction)
