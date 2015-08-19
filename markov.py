import random
from wordbank import *

class Markov(object):
    
    def __init__(self, seed_words):
        self.W = Wordbank()
        self.cache = {}
        self.seed_cache = {}
        self.words = []
        self.word_size = len(self.words)
        self.seed_words = self.W.add(seed_words)
        self.seed_word_size = len(self.seed_words)

    def add_words(self, words):
        self.words = self.W.add(words)
        self.word_size = len(words)
        self.database()

    def triples(self):
        """ Generates triples from the given data string. So if our string were
        "What a lovely day", we'd generate (What, a, lovely) and then
        (a, lovely, day).
        """
        
        if len(self.words) < 3:
            return
        
        for i in xrange(len(self.words) - 1):
            if i+2 < self.word_size:
                yield (self.words[i], self.words[i+1], self.words[i+2])
            else:
                yield (self.words[i], self.words[i+1], -1)
    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]
        for i in xrange(self.word_size-1):
            if self.words[i] in self.seed_words:
                key = self.words[i]
                value = self.words[i+1]
                if key in self.seed_cache:
                    self.seed_cache[key].append(value)
                else:
                    self.seed_cache[key] = [value]
        self.words = []

    def generate_markov_text(self, size=25):
        seed = random.randint(0, self.seed_word_size-1)
        seed_word = self.seed_words[seed] 
        next_word = random.choice(self.seed_cache[seed_word])
        w1, w2 = seed_word, next_word
        gen_words = [self.W['tfw']]
        for i in xrange(size):
            if i != 0:
                gen_words.append(w1)
            if w2 < 0:
                if random.randint(0,3) == 1:
                    break
            if (w1, w2) not in self.cache:
                break
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join([self.W[i] for i in gen_words])



