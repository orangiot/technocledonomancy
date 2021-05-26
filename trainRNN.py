import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-hid", "-hidden", type=int, default=1)
parser.add_argument("-e", "-epochs", type=int, default=10)
parser.add_argument("-i", "-dictionary", default='dict/italian.txt')
parser.add_argument("-o", "-weights")
args = parser.parse_args()

if args.o == None:
	if not os.path.isdir('rnn'):
		os.mkdir('rnn')
	weightsfile = 'rnn/rnnweights'+str(args.hid)+'.h5'
else:
	weightsfile = args.o

def string2numbers(s):
	s = s.replace('\n','')
	a = [0]*len(s)
	for i in range(len(s)):
		a[i] = ord(s[i]) - ord('a')
	return a
	
def finddist(a):
	b = [0]*len(a)
	for i in range(len(a)):
		b[i] = len(a[i])
	return np.average(b), np.std(b), max(b)
	
def generaterandomstring(mu,sigma,maxlength):
	k = min(maxlength,max(2,int(np.random.normal(mu,sigma))))
	return np.random.randint(ord('a'), ord('z')+1, k)

#defines the model
model = keras.Sequential()
model.add(layers.LSTM(units=args.hid, input_shape=(None,1)))
model.add(layers.Dense(1))

#loads the real words
f = open(args.i,'r')
realwords = f.readlines()
f.close()
for i in range(len(realwords)):
	realwords[i] = np.asarray(string2numbers(realwords[i]))
fakewords = [0]*len(realwords)
mu, sigma, maxlength = finddist(realwords)
for i in range(len(fakewords)):
	fakewords[i] = np.asarray(generaterandomstring(mu,sigma, maxlength))

examples = len(realwords)
x = np.zeros((examples*2,maxlength,1))
for i in range(examples):
	for j in range(maxlength):
		if len(realwords[i]) <= j:
			x[i,j,0] = -1
		else:
			x[i,j,0] = realwords[i][j]
		if len(fakewords[i]) <= j:
			x[i + examples,j,0] = -1
		else:
			x[i + examples,j,0] = fakewords[i][j]
y = np.asarray([1]*examples + [0]*examples)

#trains the model 
batchsize = 256
model.compile(loss = 'mse', optimizer = 'adam')
model.fit(x, y, batch_size = batchsize, epochs = args.e, shuffle = True,  validation_split = 0.2)
model.save_weights(weightsfile)
