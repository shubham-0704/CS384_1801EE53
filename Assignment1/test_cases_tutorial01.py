import tutorial01 as A1

actual_answers = [9, 12,28,0]
student_answers = []

test_case_1 = A1.add(5,4)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2.0)
student_answers.append(test_case_2)

test_case_3 = A1.multiply(14,2)
student_answers.append(test_case_3)

test_case_4 = A1.divide(14, 0)
student_answers.append(test_case_4)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
