# Quiz Game

# Algorithm

# 1. variable to store score (EX: Score)
# 2. ask que to user using input() function
# 3. if user gives correct ans then score + 1 , print(correct)
# 4. if user gives incorrect ans print(incorrect)
# 5. print score of the user


print("Welcome to Quiz game!")

print("NOTE : If the spelling is incorrect the ans  is considered as incorrect ans ")

score = 0
question_no = 0

play = input("Do u want to play , say YES / NO ? ").upper()

if play == "YES":

    question_no += 1
    ques = input(f"\n{question_no}. what is CPU stands for ? "). lower()

    if ques == "central processing unit":
        score += 1
        print("It is correct ans, You got 1 point")

    else:
        print("it is Incorrect ans")

        print(f"correct ans is ---> central processing unit")

    question_no += 1
    ques = input(f"\n{question_no}. what is GPU stands for ? ").lower()
    if ques == "graphical processing unit":
        score += 1
        print("It is correct ans, You got 1 point")

    else:
        print("it is Incorrect ans")

        print(f"correct ans is ---> graphical processing unit")

    question_no += 1
    ques = input(f"\n{question_no}. what is RAM stands for ? ").lower()
    if ques == "random access memory":
        score += 1
        print("It is correct ans, You got 1 point")

    else:
        print("it is Incorrect ans")

        print(f"correct ans is ---> random access memory")

    question_no += 1
    ques = input(f"\n{question_no}. what is PSS stands for ? ").lower()
    if ques == "power supply system":
        score += 1
        print("It is correct ans, You got 1 point")

    else:
        print("it is Incorrect ans")

        print(f"correct ans is ---> power supply system")

    question_no += 1
    ques = input(f"\n{question_no}. what is ROM stands for ? ").lower()
    if ques == "read only memory":
        score += 1
        print("It is correct ans, You got 1 point")

    else:
        print("it is Incorrect ans")
        print(f"correct ans is ---> read only memory")

print(f"No of questions is : {question_no}")
print(f"Your final score is : {score} ")

try:
    percentage = (score*100) / question_no

except ZeroDivisionError:
    print("0% ques are correct")

print(f"your final percentage is : {percentage}")