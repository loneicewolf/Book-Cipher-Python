# Book Cipher in Python3!
# this is kinda like "Only Code" for those interested
# Shortened it and removed stuff to make it more 'elegant' (hopefully it became that too)

# Recommending this link. Provided a full very good and detailed question. https://stackoverflow.com/q/42926663/14346786
# It is the question I have origininally been following for more than 2 years+.  Wished someone would just 'come along with a solution'.. But that never happend.
# In this case, It was myself who came up with a (hopefully, acceptably- Okay) Solution. Or answer. 
# If you like this, or if this is/will/was helpful - In any **possible way** PLEASE tell me that! Either via mail, or just about anything.
# Thank you!

BOOK="document1.txt"

# Read book into "boktxt"
def GetBookContent(BOOK):
    ReadBook = open(BOOK, "r")
    txtContent_splitted = ReadBook.read();
    ReadBook.close()
    Words=txtContent_splitted

    return(txtContent_splitted.split())


boktxt = GetBookContent(BOOK)

words=input("input text: ").split()
print("\nyou entered these words:\n",words)

i=0
words_len=len(words)
for word in boktxt:
    while i < words_len:
        print(boktxt.index(words[i]))
        i=i+1

x=0
klist=input("input key-sequence sep. With spaces: ").split()
for keys in klist:
        print(boktxt[int(klist[x])])
        x=x+1
