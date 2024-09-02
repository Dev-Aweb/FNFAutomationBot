import pyautogui


def apply(num: int):
    string_combo = str(num)
    output = [0, 0, 0]
    i = 1

    while i <= 3:
        try:
            output[-i] = int(string_combo[-i])
        except IndexError:
            output[-i] = 0

        i += 1

    return output

inputs = [0, 9, 15, 54, 100, 999]
expected_outputs = [[0, 0, 0], [0, 0, 9], [0, 1, 5], [0, 5, 4], [1, 0, 0], [9, 9, 9]]

for i, inp in enumerate(inputs):
    if apply(inp) == expected_outputs[i]:
        print(f'test {i} passed')
        continue

    print(f'test {i} failed')
    print(f'Input: {inp} || Output: {apply(inp)} || Expected Output: {expected_outputs[i]}')

pyautogui.moveTo(1285, 279-80)
