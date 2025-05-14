words = ["I", "love", "Python"]
sen = ""
for word in words:
  sen = sen + word + " "
print(sen)


words = ["I", "love", "Python"]
sen = ""
for word in words:
  #sen = sen + word + " "
  sen += word + " "
print(sen)
#this is an example of a list of words being joined together using augmented assignment operators in a for loop

words = ["I", "love", "peppermint", "patties"]
sen = " ".join(words)
print(sen)
#this is an example of a list of words being joined together with a space separating each word using the "join" function



scale = ""
for note in "ABCDEFG":
  scale += note + ", "