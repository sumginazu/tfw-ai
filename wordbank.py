#Database of words.

class Wordbank(object):
    
    def __init__(self, words=[]):
        self.word_to_index = {"":-1, ".":-1, "?":-2, "!":-3}
        self.index_to_word = {-1:".", -2:"?", -3:"!"}
        self.num_words = 0
        self.add(words)

    def __len__(self):
        return self.num_words

    def __getitem__(self, i):
        if type(i) == type(1):
            return self.index_to_word[i]
        return self.word_to_index[i]

    def __setitem__(self, i, j):
        #TODO delete old entries on overwrite
        if type(i) == type(1):
            self.index_to_word[i] = j
            self.word_to_index[j] = i
            return
        self.word_to_index[i] = j
        self.index_to_word[j] = i
        return

    def append(self, word):
        if word in self.word_to_index:
            return
        self.index_to_word[self.num_words] = word
        self.word_to_index[word] = self.num_words
        self.num_words += 1

    def add(self, words):
        for word in words:
            self.append(word)
        return [self[word] for word in words]

""" #test
W = Wordbank()
W.append("dog")
W.append("cat")
W.append("parrot")
print W["dog"]
print W[1]
print W[2]
W[2] = "ferret"
print W[2]
print W.word_to_index
"""
