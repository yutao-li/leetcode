def find_hidden_string(input_string):
    if len(input_string) < 2:
        return input_string
    right, length = 0, 1
    for i in range(1, len(input_string)):
        long = input_string[i - length - 1:i + 1]
        short = input_string[i - length:i + 1]
        eq = input_string[i - length + 1:i + 1]
        if i - length - 1 >= 0 and long == long[::-1]:
            length += 2
            right = i
        elif i - length >= 0 and short == short[::-1]:
            length += 1
            right = i
        elif eq == eq[::-1] and eq < input_string[right - length + 1:right + 1]:
            right = i
    if length == 1:
        return "None"
    else:
        return input_string[right - length + 1:right + 1]
