import pytumblr, json

# Authenticate via OAuth
with open("secret.txt", 'rb') as f:
    a, b, c, d = f.read().split(',')
    client = pytumblr.TumblrRestClient(a, b, c, d.strip())

# Make the request
raw = client.info() #create_text('tfw-ai', state='published', body="""test""")
#print raw[:20]
pretty = json.dumps(raw, indent=4, sort_keys=True)
f = open('pretty.txt', 'wb')
f.write(pretty)
print pretty



"""
CONSUMER_KEY = 'YNWaabdpNkvo6B9Sps642tIoa0YqDWnrpV6HmA4NgPaR84Rbva'
CONSUMER_SEC = 'B5DUstW45wUrmqX7XOmNbArnAkCq2z7W55exe8yMdTKk2VIk8Q'

t = Tumblpy(CONSUMER_KEY, CONSUMER_SEC)
auth_props = t.get_authentication_tokens(callback_url='http://tfw-ai.tumblr.com')
auth_url = auth_props['auth_url']

OAUTH_TOKEN_SECRET = auth_props['oauth_token_secret']

f = open('secrets', 'wb')
f.write(CONSUMER_KEY + '\n')
f.write(CONSUMER_SEC + '\n')
f.write(OAUTH_TOKEN_SECRET + '\n')

print 'Connect with Tumblr via: %s' % auth_url

# https://www.tumblr.com/oauth/authorize?oauth_token=
#yjrcP1Wf9BsM02G2s2pGE9mED6wetVw7WnuLP6CuihTJofm4CF&oauth_callback=http%3A%2F%2Ftfw-ai.tumblr.com

#iFKXoKoqKkbq0EwSPncrjWFtqkozx9UU4G6OtavLncA1Fbo1XK
"""
"""
CONSUMER_KEY, CONSUMER_SEC, OAUTH_TOKEN_SECRET = open('secrets', 'rb').read().split()
print CONSUMER_KEY, CONSUMER_SEC
print OAUTH_TOKEN_SECRET
t = Tumblpy(CONSUMER_KEY, CONSUMER_SEC,
            'yjrcP1Wf9BsM02G2s2pGE9mED6wetVw7WnuLP6CuihTJofm4CF',
            OAUTH_TOKEN_SECRET)
authorized_tokens = t.get_authorized_tokens('iFKXoKoqKkbq0EwSPncrjWFtqkozx9UU4G6OtavLncA1Fbo1XK')
final_oauth_token = authorized_tokens['oauth_token']
final_oauth_token_secret = authorized_tokens['oauth_token_secret']

f = open('allsecrets', 'wb')
d = {'consumer_key':CONSUMER_KEY,
     'consumer_secret':CONSUMER_SEC,
     'oauth_token':'yjrcP1Wf9BsM02G2s2pGE9mED6wetVw7WnuLP6CuihTJofm4CF',
     'oauth_token_secret':OAUTH_TOKEN_SECRET,
     'oauth_verifier':'iFKXoKoqKkbq0EwSPncrjWFtqkozx9UU4G6OtavLncA1Fbo1XK',
     'final_oauth_token':final_oauth_token,
     'final_oauth_token_secret':final_oauth_token_secret}
f.write(str(d))
f.close()
"""
