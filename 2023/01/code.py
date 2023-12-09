import os


def get_end_digits(string: str) -> tuple[str, str]:
    """Returns the farthest left or right "digit" in a given string."""

    NUMS = [str(num) for num in range(1,10)]
    WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    DIGITS = {text: num for text, num in list(zip(WORDS, NUMS))}

    search_results = {'left': [], 'right': []}
    for digit in [*DIGITS.keys(), *DIGITS.values()]:
        digit_index_l = string.find(digit)
        digit_index_r = string.rfind(digit)

        if digit in WORDS:
            digit = DIGITS[digit]

        if digit_index_l >= 0:
            search_results['left'].append((digit_index_l, digit))
        if digit_index_r >= 0:
            search_results['right'].append((digit_index_r, digit))

    [array.sort() for array in search_results.values()]
    return (search_results['left'][0][1], search_results['right'][-1][1])

def convert_digits(digits: tuple[str]) -> int:
    """Returns a a single 2-char integer from a tuple of two string-integers."""
    return int("".join([*digits]))

def get_calibration_numbers(string_input: str) -> [str]:
    """Returns an array of two-char ints from a line's end digits."""
    calibration_results = []
    for line in string_input.strip().split("\n"):
        end_digits = get_end_digits(line)
        calibration_number = convert_digits(end_digits)
        calibration_results.append(calibration_number)

    return calibration_results


if __name__ == "__main__":
    file_name = "input.txt"
    base_directory = os.path.dirname(__file__)
    input_file_path = os.path.join(base_directory, file_name)

    file_input = None
    with open(input_file_path, 'r') as file:
        file_input = file.read()

    result = sum(get_calibration_numbers(file_input))
    print(result)
