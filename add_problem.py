import os
import sys
from pathlib import Path


def get_problem_num(line: str):
    dot_pos = line.find('.')
    number = line[3:dot_pos]
    return number


def add_to_readme(num: str, dif: str):
    with open('README.md', 'r+', encoding='utf-8') as file:
        insert_string = f'| [{num}. ]() '
        if dif == 'e':
            insert_string += ('| [😎](https://github.com/r-vvch/LeetCode/blob/main/solutions/'
                              + num + '_.py) ' + '| `` | Easy |\n')
        elif dif == 'm':
            insert_string += ('| [🤔](https://github.com/r-vvch/LeetCode/blob/main/solutions/'
                              + num + '_.py) ' + '| `` | Medium |\n')
        elif dif == 'h':
            insert_string += ('| [😤](https://github.com/r-vvch/LeetCode/blob/main/solutions/'
                              + num + '_.py) ' + '| `` | Hard |\n')

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
        f.write('\n\nif __name__ == \'__main__\':\n    pass\n')


if __name__ == '__main__':
    problem_num = sys.argv[1]
    problem_dif = sys.argv[2]

    add_to_readme(problem_num, problem_dif)
    add_py_file(problem_num)
