import unittest


# https://leetcode.com/problems/simplify-path

class Solution:

    def find_next_slash(self, start: int, path: str) -> int:
        for i in range(start, len(path)):
            if path[i] == "/":
                return i
        return len(path)

    def simplifyPath(self, path: str) -> str:
        simplified_path = []
        i = 0
        while i < len(path):
            if path[i] == "/":
                i += 1
                continue
            next_slash = self.find_next_slash(i, path)
            path_element = path[i: next_slash]
            if path_element == "":
                break
            elif path_element == "..":
                if len(simplified_path) != 0:
                    simplified_path.pop()
                i += len(path_element)
                continue
            elif path_element == ".":
                i += 1
                continue
            elif len(path_element) > 0:
                simplified_path.append(path_element)
                i += len(path_element)

        return "/" + "/".join(simplified_path)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("/home", Solution().simplifyPath("/home/./"))

    def test_b(self):
        self.assertEqual("/", Solution().simplifyPath("/../"))

    def test_c(self):
        self.assertEqual("/home/foo", Solution().simplifyPath("/home//foo/"))

    def test_d(self):
        self.assertEqual("/c", Solution().simplifyPath("/a/./b/../../c/"))

    def test_e(self):
        self.assertEqual("/a/b/c", Solution().simplifyPath("/a//b////c/d//././/.."))


if __name__ == "__main__":
    unittest.main()
