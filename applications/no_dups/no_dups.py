def no_dups(s):
    # Your code here
    if not s:
        return ""
    
    used = set()
    result = []

    for word in s.split():
        if word not in used:
            used.add(word)
            result.append(word)

    return " ".join(result)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))