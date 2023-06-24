while True:

    original = []
    reverse = []
    naww = input("\nEnter a word: ")
    aksiNaw = naww[::-1]

    for i in naww:
        original.append(i)
    for ii in aksiNaw:
        reverse.append(ii)
    if naww=="q":
        print("\nThank you for using Palindrome Test. Goodbye!\n")
        break   
    elif naww == aksiNaw:
        print("The word is Palindrome.")
    elif naww.casefold() == aksiNaw.casefold():
        print("The word is Palindrome if we ignore the uppercase.")
    

    else:
        if original[1:] == reverse[:-1]:
            print("First letter out and it's Palindrome")
        
        elif original[:-1] == reverse[1:]:
            print("last letter out and it's Palindrome")
        else:
            print("The word isn't Palindrome.")

