f = open('book.txt', 'r')
content = f.read().split(" ")
import hw51


banned_words = ["something", "through"]
x = 0

frequencies = {}
while x < len(content):
    try:
        frequencies[content[x]] += 1
    except:
        frequencies[content[x]] = 0
    x += 1


print()