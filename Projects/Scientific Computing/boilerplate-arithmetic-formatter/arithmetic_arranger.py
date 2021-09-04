def operation_construction(problems):  # Extract input into lists
    first_operand = []
    second_operand = []
    operator = []

    for problem in problems:
        element = problem.split()
        first_operand.append(element[0])
        second_operand.append(element[2])
        operator.append(element[1])

    return first_operand, second_operand, operator


def conditions(problems):

    first_operand, second_operand, operator = operation_construction(problems)

    # Set limit
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Check for * and /
    if '/' in operator or '*' in operator:
        return "Error: Operator must be '+' or '-'."

    # Check for length of operands (not exceed 4 digits)
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # Check for digits condition
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return 'Error: Numbers must only contain digits.'


def arithmetic_arranger(problems, display=False):
    if conditions(problems):
        return conditions(problems)

    first_operand, second_operand, operator = operation_construction(problems)

    len1 = len(first_operand)
    len2 = len(second_operand)

    first_row = ''
    second_row = ''
    dash_row = ''
    res_row = ''
    space = ' ' * 4
    result = []

    for i in range(max(len1, len2)):
        length = max(len(first_operand[i]), len(second_operand[i])) + 2
        if operator[i] == '+':
            result.append(int(first_operand[i]) + int(second_operand[i]))
        else:
            result.append(int(first_operand[i]) - int(second_operand[i]))
        if i != max(len1, len2) - 1:
            first_row += str(first_operand[i]).rjust(length) + space
            second_row += str(operator[i]) + str(second_operand[i]).rjust(length - 1) + space
            dash_row += '-' * length + space
            res_row += str(result[i]).rjust(length) + space
        else:
            first_row += str(first_operand[i]).rjust(length)
            second_row += str(operator[i]) + str(second_operand[i]).rjust(length - 1)
            dash_row += '-' * length
            res_row += str(result[i]).rjust(length)

    if display:
        arranged_problem = f'{first_row}\n{second_row}\n{dash_row}\n{res_row}'
    else:
        arranged_problem = f'{first_row}\n{second_row}\n{dash_row}'

    return arranged_problem

