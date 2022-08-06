PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}"
}

def is_valid(input: str) -> bool:
    stack = []
    for c in input:
        if c in PAIRS:
            stack.append(PAIRS[c])
        else:
            if len(stack) == 0:
                return False
            if c != stack[-1]:
                return False
            stack.pop()
    if len(stack):
        return False
    return True
    

if __name__ == "__main__":
    input = "({([()()])})"
    print(is_valid(input))