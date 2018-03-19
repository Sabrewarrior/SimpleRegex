ESCAPE = "\\"


def check_parentheses(s):
    """ Return True if the parentheses in string s match, otherwise False. """
    j = 0
    if not s.startswith("(?:") or not s.endswith(")"):
        s = "(?:{})".format(s)
    print(s)

    escape = False
    new_group = False
    groups = [["", None, False]]
    cur_group = 0

    for c in range(len(s)):
        if escape:
            if not new_group:
                escape = False
                groups[cur_group][0] += s[c]
            else:
                if s[c] == ":":
                    escape = False
                    new_group = False
        else:
            if new_group:
                if s[c:].startswith("?:"):
                    print(s[c:])
                    groups[cur_group][2] = False
                    escape = True
                    new_group = True
                    continue
                else:
                    new_group = False
                    groups[cur_group][2] = True
                    
            if s[c] in ESCAPE:
                escape = True
            elif s[c] == ')':
                j -= 1
                cur_group = groups[cur_group][1]
                if j < 0:
                    return False
            elif s[c] == '(':
                new_group = True
                groups[cur_group][0] += "\({name}\)".format(name=str(len(groups)))
                groups.append(["", cur_group, None])
                cur_group = len(groups) - 1
                j += 1
            else:
                groups[cur_group][0] += s[c]

    print(groups)
    if not j == 0:
        return False
    group_to_regex(groups)
    print(s)
    print()
    return groups


def group_to_regex(groups):
    regex = [None]*len(groups)
    for group_num in range(len(groups) - 1, 0, -1):
        parent = groups[group_num][1]
        if parent is not None:
            capture = ":?"
            if groups[group_num][2]:
                capture = ""
            if regex[group_num] is None:
                replace_str = "({}{})".format(capture, groups[group_num][0])
            else:
                replace_str = "({}{})".format(capture, regex[group_num])
            print("Replacing: " + "\({}\)".format(group_num))

            if regex[parent] is None:
                regex[parent] = groups[parent][0].replace("\({}\)".format(group_num), replace_str)
                print("in parent {}: {}".format(parent, groups[parent][0]))
            else:
                regex[parent] = regex[parent].replace("\({}\)".format(group_num), replace_str)
                print("in parent {}: {}".format(parent, regex[parent]))

            print("with: " + replace_str)
            print("Checking: " + regex[parent])
            #print(regex)
            print()
    print(groups)
    print(regex)
