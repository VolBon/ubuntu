def censor(text, word):
    length = len(word)
    words = text.split()
    final = [i.replace(word,'*'*length) for i in words]
    return " ".join(final)

print censor("I am me, met yo me me me mememememememememe", "me")



