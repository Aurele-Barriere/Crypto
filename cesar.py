# caesar cipher

word = "iravivqvqrpelcgv"

for i in range(1,27):
    for c in word :
        print(chr((((ord(c)+i)-97)%26)+97), end="")

    print()


