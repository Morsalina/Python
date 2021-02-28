import pyinputplus as pyip
import time
import random

print("How many question you want to set for the quiz ? : ")
numberOfQues = int(input())
correctAns = 0

for i in range(numberOfQues):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '# %s : %s X %s = ' %(i+1623, num1, num2)
    try:
        ans = pyip.inputStr(prompt, allowRegexes=['^%s$' %(num1*num2)],blockRegexes=[('*','Incorrect')], timeout=10, limit=2)
    except pyip.TimeoutException:
        print("Sorry ! you are out of time !!!")
    except pyip.RetryLimitException:
        print("Sorry ! you are out of attempts")
    else:
        print("Correct answer")
        correctAns += 1

        time.sleep(1)

print('Score : %s/%s' %(correctAns, numberOfQues))







