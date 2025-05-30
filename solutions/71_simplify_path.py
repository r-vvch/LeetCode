class Solution:
    def simplifyPath(self, path: str) -> str:
        elements = path.split("/")
        output = []

        for el in elements:
            if el == "" or el == ".":
                continue

            if el == "..":
                if output:
                    output.pop()
            else:
                output.append(el)

        return "/" + "/".join(output)


if __name__ == '__main__':
    solution = Solution()

    path = "/home/"
    print(solution.simplifyPath(path)) # "/home"

    path = "/home//foo/"
    print(solution.simplifyPath(path)) # "/home/foo"

    path = "/home/user/Documents/../Pictures"
    print(solution.simplifyPath(path)) # "/home/user/Pictures"

    path = "/../"
    print(solution.simplifyPath(path)) # "/"

    path = "/.../a/../b/c/../d/./"
    print(solution.simplifyPath(path)) # "/.../b/d"

    path = "/a//b////c/d//././/.."
    print(solution.simplifyPath(path)) # "/a/b/c"

    path = "/."
    print(solution.simplifyPath(path)) # "/"

    path = "/.."
    print(solution.simplifyPath(path)) # "/"
