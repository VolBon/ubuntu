str = "X_DSPAM_Confidence: 0.8475"

n = str.find(" ")

new = str[n:]
print float(new)