Cledonomancy (sometimes called cledonism) is a divination practice which consists in listening to the words of passersby or other people and interpreting them as oracles. Practised both in ancient Greece and in the hebraic-christian culture and in Persia (with the name of [falgus](https://iranicaonline.org/articles/divination); I have no info about this practice as all the sources I found are in Persian). In Greece it was practised in some temples consecrated to Apollo (like in Thebes and Smyrna, see Pausanias 9.11.5, but the Dizionario Mitologico by Giovanni Pozzoli et al. vol. 1 pg. 435 says that it was previously attributed to Ceres) and to Hermes (like in Pharae, see Pausanias 7.22.2). Also Ulysses (Odyssey 20.145+) uses cledonomancy invoking Zeus. The original Pharae ritual is the following:

1. during the evening, burn some incense on the fire near the statue of Hermes;
2. fill and light the lamps near the fire;
3. place a local coin at the right of the statue;
4. ask to the ears of Hermes your question;
5. plug your ears with your hands and exit the temple;
6. when suitable, unplug your ears and listen to what people are saying.

Pausanias, in the same section, implies that such divination form originates in temples dedicated to Apis (and here, maybe, there is the "mysteric" correspondence Apis-(Serapis-Mitra-)Ceres). The practice I propose follows the same principle: a suitable invocation and then "listening to what people are saying", but on the internet, inspired by recent practices like infoscaping. There are several suitable traditional invocations (Apollo, Hermes, Ceres, Zeus, Apis), but also Homer (the poet as a divinized hero) or Uranus (to produce barbaric words) might be interesting. I use Hermes as he seems the more logical for a contemporary divination practice:

1. (in case) banishing ritual;
2. suitable invocation;
3. (optional) preparation of an input file for the artificial intelligence (AI); it is possible to prepare such file before the ritual;
4. run the AI script which will output several words;
5. select a word and search on a search engine;
6. navigate in a website which catches the eye, search a new word or phrase to search;
7. repeat the step 6 until you find a response;
8. (in case) banishing ritual.

The invocation might be a simple request or a more complete assumption of godform, following the details of Liber O vel Manus et Sagittae. I use the Orphic Hymn to Mercury.
response
The input file can be any file which gives a magical link, like a photo of a sigil or a meaningful song. It is possible to not have an input file and use "the present moment". The internal structure of the AI is the following:

1. transformation of the input file in a seed for the random number generator;
2. generation of a word with a Markov chain from the seed;
3. quality control of the word with a RNN.

While the steps 2 and 3 of the AI are actually based on data (the corpus of words in a given language) and so are "intelligent", step 1 is arbitrary and then the magician should intervene to give meaning to the operation, similarly to what happens with sigil (that might be, but aren't, arbitrary squiggles). In a following version I will try to make also this step intelligent, maybe through a GAN, but restraining the input file on a specific class (like an image). Moreover, if one has a suitable corpus of texts, it is possible to convert this practice to a bibliomancy of sorts, doing the steps 5-6-7 on such corpus and not on a search engine.
