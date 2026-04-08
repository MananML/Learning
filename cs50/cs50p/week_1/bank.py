
greeting = input("Greeting: ").lower().strip()

first_word = greeting.split()[0]
first_letter = greeting[0]

if first_word == "hello" or first_word == "hello,":
    print("$0")

elif first_letter == "h":
    print("$20")

else:
    print("$100")