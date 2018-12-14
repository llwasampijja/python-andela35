

"""Qn0"""
def grading_system():
    student_marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    marks_below_fifty = []
    marks_above_fifty = []
    for mark in student_marks:
        if mark < 50:
            marks_below_fifty.append(mark)
        else:
            marks_above_fifty.append(mark)

    for mark in marks_below_fifty:
        print(grader(mark))
    for mark in marks_above_fifty:
        print(grader(mark))

def grader(mark):
    if 100 >= mark and 90 <= mark:
        return f"{mark}%: Excellent"
    elif 90 > mark and 70 <= mark:
        return f"{mark}%: is Very Good"
    elif 70 > mark and 60 <= mark:
        return f"{mark}%: Good"
    elif 60 > mark and 40 <= mark:
        return f"{mark}%: Poor"
    elif 40 > mark and 20 <= mark:
        return f"{mark}%: Very Poor"
    elif 20 > mark and 0 <= mark:
        return f"{mark}%: Repeat"
    elif 100 >= mark and 90 <= mark:
        return f"{mark}%: Is in an unknown range"


# 89 - 70 for 
# 69 - 60 for good
# 59 - 40 for poor
# 39 - 20 for very poor
# 19 - 0 for repeat


"""Qn1"""
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

"""Qn2"""
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

"""Qn3"""
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
    if False in ([digit == '0' or digit == '1' for digit in number] or len(number)==4):
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

"""Qn4"""
account_balance = 0
def bankingFunction(user_transation):
    global account_balance
    user_transation = user_transation.strip()
    user_transation_0 = user_transation.replace(" ", "")
    if user_transation_0 == "":
        return "Empty input not allowed"
    else:
        transaction_parts  = user_transation.split(" ")
        if transaction_parts[0].strip() == "D" and (transaction_parts[1].strip()).isdigit():
            account_balance = account_balance + int(transaction_parts[1].strip())
            return account_balance
        elif transaction_parts[0].strip() == "W" and (transaction_parts[1].strip()).isdigit():
            if account_balance > int(transaction_parts[1].strip()):
                account_balance = account_balance - int(transaction_parts[1].strip())
            else:
                return "Low balance, Add more funds to withdraw"
            return account_balance
        else:
            return "Unknown Request"

def transaction_prompt(from_user):
    if from_user.lower() == "q":
        return "Thanks, Goodbye"
    else:
        print(bankingFunction(from_user))
        transaction_prompt(input("make your transaction: "))



"""Qn5"""
def square_numbers():
    numbers = range(1,21)
    list_squares = []
    for number in numbers:
        list_squares.append(number**2)
    list_firstfive = list_squares[0:5]
    return list_firstfive

"""Qn 0"""
grading_system()

"""Qn 1"""
print(numb_multiple_seven_not_five())

"""Qn 2"""
capitizeSequenseOfLines()

"""Qn 3"""
print(multiples_five(input("Enter binary number sequence: ")))

"""Qn 4"""
print(transaction_prompt(input("make your transaction: ")))

"""Qn 5"""
print( square_numbers())


