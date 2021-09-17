import sys

text = open(sys.argv[1]).readlines()[0]
result = ""
print("Before {}".format(text))
for i in range(0, len(text) - 1):
    result = result + chr(ord(text[i]) - i)
print("After {}".format(result))