def numb_multiple_seven_not_five():
    numbers = range(2000, 3200)
    string_numbers = ""
    for number in numbers:
        if number%7 == 0 and number%5 != 0:
            if string_numbers == "":
                string_numbers = str(number)
            else:
                string_numbers = string_numbers + "," + str(number)
    return string_numbers

list_of_sentences = []
list_of_uppercased_sentences = []
def capitizeSequenseOfLines():
    word = input("Enter words or 'Q' if you're done: ")
    if word.lower() == "q":
        for sentence in list_of_sentences:
            print(sentence.upper())
    else:
        list_of_sentences.append(word)
        capitizeSequenseOfLines()

def multiples_five(user_input):
    user_input = user_input.replace(" ", "")
    list_of_inputs = user_input.split(",")
    string_numbers = ""
    for list_item in list_of_inputs:
        if string_numbers == "" and convert_to_baseten(check_if_binary_number(list_item))%5==0:
            string_numbers = check_if_binary_number(list_item)
        elif check_if_binary_number(list_item) != "" and convert_to_baseten(check_if_binary_number(list_item))%5==0:
            string_numbers = string_numbers + "," + check_if_binary_number(list_item)
        else:
            pass

    

    return string_numbers

def check_if_binary_number(number):
    if False in [digit == '0' or digit == '1' for digit in number]:
        return ""
    else:
        return number

def convert_to_baseten(binary):
    n = len(binary)
    answ = 0
    while n > 0:
        answ = answ + (int(binary[n-1])*(2**(n-1)))
        n = n - 1
    return answ

def square_numbers():
    numbers = range(1,21)
    list_squares = []
    for number in numbers:
        list_squares.append(number**2)
    list_firstfive = list_squares[0:5]
    return list_firstfive


# def printList():
#   XXXXXX
#   XXXXXX
    
# printList()


print(numb_multiple_seven_not_five())
capitizeSequenseOfLines()
print(multiples_five(input("Enter number sequence: ")))
print( square_numbers())


