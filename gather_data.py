#Download and parse posts, saving the model to a file. 

from markov import *
import pytumblr, json, string
import nltk

LIMIT = 1000000

seed_words = [
    "tfw", 
    'when'
]

M = Markov(seed_words)

# Authenticate via OAuth
with open("secret.txt", 'rb') as f:
    a, b, c, d = f.read().split(',')
    client = pytumblr.TumblrRestClient(a, b, c, d.strip())

#List of tags to search
taglist = [
    "tfw",
    "that feel when",
    "rant",
    "angst",
    "feels"
    ]

badchars = dict((ord(char),None) for char in ',()\\/|;:<>-+_=*^%$#@"')

#List of most recent post IDs; these posts are ones we have already parsed
prevpostID = {}

#Filter text to make sure it includes a trigger pattern
def filter_text(words):
    return True

#tokenze / parse
def parse(raw):
    nopunc = raw.translate(badchars)
    return nltk.word_tokenize(nopunc)

#retrieve posts
def get_tag(tag_text):
    if tag_text not in prevpostID:
        return client.tagged(tag_text, limit=LIMIT, filter='text')
    else:
        return client.tagged(tag_text, before=prevpostID[tag_text], 
                             limit=LIMIT, filter='text')

for tag in taglist:
    posts = get_tag(tag)
    for post in posts:
        try:
            raw = post['body']
        except:
            continue
        lower = raw.lower()
        tokens = parse(lower)
        if not filter_text(tokens):
            continue
        #save text data
        M.add_words(tokens)


print M.generate_markov_text(size=200)

text = M.generate_markov_text(size=300)
text = text.encode('utf-8')
# Make the request
raw = client.create_text('tfw-ai', state='published', body=text)
