while True:

    original = []
    reverse = []
    naww = input("enter name: ")
    aksiNaw = naww[::-1]

    for i in naww:
        original.append(i)
    for ii in aksiNaw:
        reverse.append(ii)
        
    if naww == aksiNaw:
        print("you are correct")
    elif naww.casefold() == aksiNaw.casefold():
        print("needs correction")
    

    else:
        if original[1:] == reverse[:-1]:
            print("First letter wrong")
        
        elif original[:-1] == reverse[1:]:
            print("last letter is wrong")
        print("end of line")

