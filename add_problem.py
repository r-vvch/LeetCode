import os
import sys
from pathlib import Path


def get_problem_num(line: str):
    dot_pos = line.find('.')
    number = line[3:dot_pos]
    return number


def default_font_diff(line: str) -> str:
    return line


def colored_diff_shields(line: str) -> str:
    if line == 'Easy':
        return '![](https://img.shields.io/badge/Easy-1cb8b8)'
    elif line == 'Medium':
        return '![](https://img.shields.io/badge/Medium-ffa800)'
    elif line == 'Hard':
        return '![](https://img.shields.io/badge/Hard-f63636)'


def add_to_readme(num: str, dif: str):
    with open('README.md', 'r+', encoding='utf-8') as file:
        insert_string = f'| [{num}. ]() '
        if dif == 'e':
            insert_string += ('| [😎](https://github.com/r-vvch/LeetCode/blob/main/solutions/'
                              + num + '_.py) | `` | ' + colored_diff_shields('Easy') + '|\n')
        elif dif == 'm':
            insert_string += ('| [🤔](https://github.com/r-vvch/LeetCode/blob/main/solutions/'
                              + num + '_.py) | `` | ' + colored_diff_shields('Medium') + '|\n')
        elif dif == 'h':
            insert_string += ('| [😤](https://github.com/r-vvch/LeetCode/blob/main/solutions/'
                              + num + '_.py) | `` | ' + colored_diff_shields('Hard') + '|\n')
        contents = file.readlines()

        if int(num) > int(get_problem_num(contents[-1])):
            contents.append(insert_string)
        else:
            for l_num in range(6, len(contents) - 1):
                if (int(get_problem_num(contents[l_num])) < int(num) and
                    int(get_problem_num(contents[l_num + 1])) > int(num)):
                    contents.insert(l_num + 1, insert_string)
                    break

        file.seek(0)
        file.writelines(contents)


def add_py_file(num: str):
    sol_path = os.path.join(os.path.dirname(__file__), 'solutions')
    if not os.path.exists(sol_path):
        Path(sol_path).mkdir(parents=True, exist_ok=True)

    py_file = os.path.join(sol_path, f'{num}_.py')
    with open(py_file, 'w') as f:
        f.write('class Solution:\n    pass\n\n\n' +
                'if __name__ == \'__main__\':\n    solution = Solution()\n\n')


if __name__ == '__main__':
    problem_num = sys.argv[1]
    problem_dif = sys.argv[2]

    add_to_readme(problem_num, problem_dif)
    add_py_file(problem_num)
