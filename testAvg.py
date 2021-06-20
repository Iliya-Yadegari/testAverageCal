print('Please enter your test grades:')

test1 = int(input('Test 1: '))
test2 = int(input('Test 2: '))

testAvg = (test1 + test2) / 2

print('Please enter your quiz grades:')

quiz1 = int(input('Quiz 1: '))
quiz2 = int(input('Quiz 2: '))
quiz3 = int(input('Quiz 3: '))

quizAvg = (quiz1 + quiz2 + quiz3) / 3

print('Please enter your homework average:')

homework = float(input('Homework average: '))

totalAvg = (testAvg * 0.5) + (quizAvg * 0.3) + (homework * 0.2)

print(f'Total average: {totalAvg}')