import textwrap
class solution:
    def text_wrap(string, max_width):
        return textwrap.fill(string, max_width)
if __name__ == '__main__':
    s = "ABCDEFGHIJKLOMN"
    width = int(input("Enter :"))
    obj = solution.text_wrap(s, width)
    print(obj)