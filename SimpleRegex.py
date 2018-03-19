import re
from _parse import *

def convert_to_re(simple_regex):
    print(simple_regex)
    print(re.escape(simple_regex))


if __name__ == "__main__":
    test_regex = r'zero-well (one-(?:two-[^(?:three-no )]halp)|(?:four-no halp)) (five-does it actually work) ok'
    print(check_parentheses(test_regex))
