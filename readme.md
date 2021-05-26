###Quickstart guide:

1. install python3 and (optional) tensorflow (tested with tf 2.4.1)
2. run buildmarkov.py
3. (optional, requires tensorflow) run trainRNN.py
4. run generatewords.py or (after trainRNN.py) nicergeneratewords.py

###Scripts:

***buildmarkov.py*** is a python3 script to produce a transition matrix for a Markov chain, given a dictionary of words. Such Markov chain is a model that describes the relationship between letters in a word and their preceding letters. It accepts the following arguments:

- -m, -memory (default: 2): the number of previous letters to remember in a relationship. For example, if memory is 1, from 'bottle' the chain will remember (start)->b, b->o, o->t, t->t, t->l, l->e, e->(end); if memory is 2, it will remember (start)->b, b->o, bo->t, ot->t, tt->l, tl->e, le->(end). A note of caution: increasing the memory will result in exponentially larger files: a 1-memory file is ~20 kB, a 2-memory is ~560 kB, a 3-memory is ~15 MB, a 4-memory is ~410 MB. *TODO*: better file format.
- -i, -dictionary (default: dict/italian.txt): path to the dictionary to use; the file should be a plaintext file with one word for line.
- -o, -matrix (default: markov/markovmatrix<memory>.json): path to the output file.

***trainRNN.py*** is a python3 script to train a RNN to distinguish between the words of a given dictionary and totally random words. It uses a small LSTM architecture and is really fast to train on modern hardware. The script requires tensorflow, so it might not work on older OS. It is better to use this script, but it is optional for the end result. It accepts the following arguments:

- -hid, -hidden (default: 1): the dimension of the hidden LSTM layer.
- -e, -epochs (default: 10): total epochs.
- -i, -dictionary (default: dict/italian.txt): path to the dictionary to use; the file should be a plaintext file with one word for line.
- -o, -weights (default: rnn/rnnweights<h>.h5): path to the output file.

**generatewords.py** is a python3 script to generate words and print them on terminal, without using the RNN for quality control. It accepts the following arguments:

- -m, -memory: like for buildmarkov.py
- -l, -maxlength (default: 19): maximum length of the generated words.
- -w, -words (default: 10): number of words to generate.
- -r, -random (default: False): if true, it will use a random seed for the RNG; if false and a seed file is given, such seed file will be converted (with RIPEMD-160) to a suitable seed.
- -i1, -seed (default: seeds/portal.jpg): any file to be converted to a seed.
- -i2, -matrix (default: markov/markovmatrix<memory>.json): the output of buildmarkov.py

**nicergeneratewords.py** is a python3 script to generate words and print them on terminal, without using the RNN for quality control. Like trainRNN, requires tensorflow. It accepts the following arguments:

- -m, -l, -w, -r, -i1, -i2: like for generatewords.py
- -hid: like for trainRNN.py
- -i3, -weights (default: rnn/rnnweights<h>.h5): the output of trainRNN.py
- -t, -tolerance (default: 0.5): a number between 0 and 1, the minimum quality of the generated words, where 0 is given to a totally random word and 1 is given to a word in the dictionary.

*TODO*: verbose mode for more "interaction"
*TODO*: enochian dictionary
