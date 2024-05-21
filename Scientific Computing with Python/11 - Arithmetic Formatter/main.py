def arithmetic_arranger(problems, show_answers=False):
    row_one = []
    row_two = []
    row_three = []
    dashes = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        problem_list = problem.split(" ")
        operand_one = problem_list[0]
        operand_two = problem_list[2]
        operator = problem_list[1]

        if operator == '*' or operator == '/':
            return "Error: Operator must be '+' or '-'."
        if not operand_one.isnumeric() or not operand_two.isnumeric():
            return 'Error: Numbers must only contain digits.'
        if len(operand_one) > 4 or len(operand_two) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        answer = str(eval(operand_one + operator + operand_two))
        max_operand_length = max(len(operand_one), len(operand_two))
        problem_length = max_operand_length + 2

        # Calculate number of spaces needed for each row
        row_one_spaces = problem_length - len(operand_one)
        row_two_spaces = problem_length - len(operand_two) - 1
        row_three_spaces = problem_length - len(answer)

        # Build each row
        row_one.append(" " * row_one_spaces + operand_one)
        row_two.append(operator + " " * row_two_spaces + operand_two)
        row_three.append(" " * row_three_spaces + answer)
        dashes.append('-' * problem_length)

        # Add four spaces between each problem
        if problem != problems[-1]:
            row_one.append(" " * 4)
            row_two.append(" " * 4)
            row_three.append(" " * 4)
            dashes.append(" " * 4)
    
    # Problems without answers
    results = ''.join(row_one) + "\n" + ''.join(row_two) + "\n" + ''.join(dashes)
    
    # Append answers to problems
    if show_answers:
        results += "\n" + ''.join(row_three)
        
    return results

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')