def matches(open, close):
    if open == "(" and close == ")":
        return True

    elif open == "{" and close == "}":
        return True

    elif open == "[" and close == "]":
        return True

    return False

def well_formed(string):
    stack = []
    for i in string:
        if i == "[" or i == "(" or i == "{":
            stack.append(i)
        elif i == "]" or i == ")" or i == "}":
            if len(stack) == 0:
                return False
            v = stack.pop()
            if not matches(i, v):
                return False

    if len(stack) == 0:
        return True

    return False

def main():
    s = "[({)]}"
    print(well_formed(s))

if __name__ == "__main__":
    main()