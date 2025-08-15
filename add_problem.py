import os
import sys
from pathlib import Path


def get_problem_num(line: str):
    dot_pos = line.find('.')
    curr_pos = dot_pos - 1
    while curr_pos >= 0 and line[curr_pos:dot_pos].isdigit():
        number = line[curr_pos:dot_pos]
        curr_pos -= 1
    return number


def default_font_diff(line: str) -> str:
    return line


def colored_diff_shields(line: str) -> str:
    if line == 'Easy':
        return '![](https://img.shields.io/badge/Easy-1cb8b8)'
    elif line == 'Med.':
        return '![](https://img.shields.io/badge/Medium-ffa800)'
    elif line == 'Hard':
        return '![](https://img.shields.io/badge/Hard-f63636)'


def add_problem(num: str):
    # add to readme
    with open('problems_list.txt', 'r', encoding='utf-8') as file:
        problems = file.readlines()
        if int(num) > int(get_problem_num(problems[-3])):
            insert_string = (
                f'| [{num}. ]() ' +
                '| [](https://github.com/r-vvch/LeetCode/blob/main/solutions/' +
                num + '_.py) | `` |  |\n')
        else:
            for l_num in range(int(num) * 4 - 4, min(int(num) * 4, len(problems))):
                if int(get_problem_num(problems[l_num])) == int(num):
                    problem_name = problems[l_num][:-1]
                    dot_pos = problem_name.find('.')
                    problem_name_no_num = problem_name[dot_pos + 2:]
                    problem_diff = problems[l_num + 2][:-1]
                    py_file_name = problem_name.lower().replace(' ', '_').replace('.', '') + '.py'
                    insert_string = (
                        f'| [{problem_name}](https://leetcode.com/problems/' +
                        f'{problem_name_no_num.lower().replace(' ', '-')}/) ' +
                        '| [](https://github.com/r-vvch/LeetCode/blob/main/solutions/' +
                        py_file_name + ') ' +
                        '| `` ' +
                        '| ' + colored_diff_shields(problem_diff) + ' '
                        '|\n')
                    break

    with open('README.md', 'r+', encoding='utf-8') as file:
        contents = file.readlines()
        contents_alg = contents[:-8]
        contents_sql = contents[-8:]
        if int(num) > int(get_problem_num(contents_alg[-1])):
            contents_alg.append(insert_string)
        else:
            for l_num in range(6, len(contents_alg) - 1):
                if (int(get_problem_num(contents_alg[l_num])) < int(num) and
                    int(get_problem_num(contents_alg[l_num + 1])) > int(num)):
                    contents_alg.insert(l_num + 1, insert_string)
                    break

        file.seek(0)
        full_contents = contents_alg + contents_sql
        file.writelines(full_contents)

    # add .py file
    sol_path = os.path.join(os.path.dirname(__file__), 'solutions')
    if not os.path.exists(sol_path):
        Path(sol_path).mkdir(parents=True, exist_ok=True)

    py_file = os.path.join(sol_path, py_file_name)
    with open(py_file, 'w') as f:
        f.write('class Solution:\n    pass\n\n\n' +
                'if __name__ == \'__main__\':\n    solution = Solution()\n\n')


if __name__ == '__main__':
    add_problem(sys.argv[1])
