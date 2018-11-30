
number = input("Enter a number: ")
number = int(number)
if number > 5:
    print(number, " is greater than five!")
else:
    print("Not right")
    sentence = input("Write a sentence with less than 140 characters:")
    if len(sentence) > 140:
        print("Wrong. Try again.")
    else:
        print(sentence.upper())
        print(len(sentence))
        sentence2 = input("Write another sentence with less than 140 characters:")
        if len(sentence2) > 140:
            print("Wrong. Try again.")
        else:
            print(sentence2.upper())
            print(len(sentence2))
            print(len(sentence) + len(sentence2))

  

#https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
#https://www.w3schools.com/python/python_operators.asp