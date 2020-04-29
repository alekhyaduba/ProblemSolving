def buildString(stringList):
    testString = []
    for item in stringList:
        buildstring = "_"
        for char in item:
            buildstring += char
            if char == "*":
                buildstring += "*"
        testString.append(buildstring + "_")
    return testString


numTCs = int(input())


def solve_post(post):
    name = get_name(post)
    flagPossible = True
    for each in post:
        temp = each
        if temp != name:
            if name.find(temp, len(name) - len(temp), len(name)) != -1:
                flagPossible = True
            else:
                flagPossible = False
                break

    if flagPossible:
        result = name
    else:
        result = "*"
    return result.replace('_', "")

def get_name(pre):
    name =""
    longestlen = 0
    for item in pre:
        if (longestlen < len(item)):
            name = item
            longestlen = len(item)
    return name

def solve_pre(pre):
    name = get_name(pre)
    flagPossible = True
    for each in pre:
        temp = each
        if temp != name:
            if name.find(temp, 0, len(name)) != -1:
                flagPossible = True
            else:
                flagPossible = False
                break

    if flagPossible:
        result = name
    else:
        result = "*"
    return result.replace('_', "")


def solve_mid(mid):
    return ''.join(mid)


def main():
    for i in range(numTCs):
        result = ""
        numStr = int(input())
        stringList = []
        testString = []
        flagPossible = True
        for j in range(numStr):
            stringList.append(input())

        name = ""
        longestlen = 0

        testString = buildString(stringList)
        # print(testString)
        pre = []
        post = []
        mid = []
        for each in testString:
            x = each.split("**")
            pre.append(x[0])
            post.append(x[-1])
            mid.extend(x[1:-1])

        # print(pre, mid, post)

        ans_pre = solve_pre(pre)
        ans_post = solve_post(post)

        if ans_pre == "*" or ans_post == "*":
            ans = "*"
        else:
            ans = ans_pre + solve_mid(mid) + ans_post

        print("Case #" + str(i + 1) + ": " + ans)


if __name__ == '__main__':
    main()