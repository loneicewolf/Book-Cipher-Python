# Book Cipher in Python3!
# this is kinda like "Only Code" for those interested
#Only code and no comments(or at least not needed ones)
# Shortened it and removed stuff to make it more 'elegant' (hopefully it became that too)


# Replace "document1.txt" with whatever your book / document's name is.
BOOK="document1.txt" # This contains your "Word Word Word Word ...." I believed from the very start that you meant, they are not the same - (obviously)

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
