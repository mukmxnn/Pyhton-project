# MATH TIME CHALLENGE
import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " +  operator + " " + str(right)
    answer = eval(expr)
    return expr, answer
# opening decoration
print("~" * 35)
print("WELCOME TO MATH QUIZ CHALLENGE".center(35))
print("~" * 35)

wrong = 0

input("\nPress enter to start! ")
print("-" * 30)

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) +":\n" + expr + " = " )
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-" * 40)
print("Nice work! You finished in", total_time, "seconds!")
print("You got",wrong,"faults") 