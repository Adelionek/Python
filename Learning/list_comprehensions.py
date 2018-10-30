sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split()
#words_len = []

#for word in words:
#   if word != "the":
#        words_len.append(len(word))

#print(words_len)


words_len = [len(word) for word in words if word != "the"]
#ciekawe
print(words_len)
