readbook = lambda b:(open(b,"r").read()) # takes b (as in book) can be e.g 'document1.txt'
Encrypt = lambda WORDS,BOOK:((readbook(BOOK).find(w)) for w in WORDS) # takes words (e.g "programming is fun") and finds these in the book BOOK trough readbook().
Decrypt= lambda KEYS,BOOK:((readbook(BOOK)[int(KEYS.split()[x])]) for x in range(0,len(str(KEYS).split()))) # opposite of Encrypt, takes a key sequence (e.g "1 33 2") (str) and uses readbook to get the corresponding texts from the key sequence(aka book codes)

CTXT=Encrypt("network amplified is","document1.txt")
PTTX=Decrypt("2 3 11 12 13 5 15 1 6 61 108 7 17 42 17 3 63 1 17 18",'document1.txt')
[(i,j) for i,j in zip(CTXT,PTTX)] # using list comprehension, print out the book codes and the corresponding
                                  # text
# Note I used another text here, one should obviously change the codes and text (in Enc and Dec - rypt)
# respectively to match their own text file and book codes.
# Output test run #
# [(2, 'n'),
#  (3, 'e'),
#  (11, 't'),
#  (12, 'w'),
#  (13, 'o'),
#  (5, 'r'),
#  (15, 'k'),
#  (1, ' '),
#  (6, 'a'),
#  (61, 'm'),
#  (108, 'p'),
#  (7, 'l'),
#  (17, 'i'),
#  (42, 'f'),
#  (17, 'i'),
#  (3, 'e'),
#  (63, 'd'),
#  (1, ' '),
#  (17, 'i'),
#  (18, 's')]
