def isUrl():
    url = input("Enter the url  ")
    end = '.com'
    inc = 3
    if(len(url) <= 3):
        return False
    else:
        for i in range(len(url), len(url)-4, -1):
            if url[i-1] == end[inc]:
                inc -= 1
            else:
                return False
        return True


def removVowel():
    txt = input("Please enter the text ")
    temp = ''
    for i in range(0, len(txt), 1):
        if(txt[i] == 'a' or txt[i] == 'e' or txt[i] == 'i' or txt[i] == 'o' or txt[i] == 'u'):
            temp += 'X'
        else:
            temp += txt[i]
    return temp


def splitlist(txt, pattern):
    list = []
    temp = ''
    for i in range(0, len(txt), 1):
        if txt[i] == pattern:
            list.append(temp)
            temp = ''
        else:
            temp += txt[i]
    return list


def freqchar(txt):
    greater = 0
    temp = 0
    ch = ''
    ic = 0
    for i in range(0, len(txt), 1):
        for j in range(i+1, len(txt), 1):
            if txt[i] == txt[j]:
                temp += 1
                ch = txt[i]
                ic = i

        if temp > greater:
            greater = temp
            ch = txt[ic]

        temp = 0
        ch = ''
        ic = 0
    return ch


if __name__ == '__main__':
    # Reverse the string
    # reve = ''
    # name = input("Please enter your name ")
    # for num in range(len(name), 0, -1):
    #     reve += name[num-1]
    # print(reve)

    # Count upper and lower case letter
    # text = input("Please enter the text  ")
    # lower = 0
    # upper = 0
    # for i in range(0, len(text), 1):
    #     a = ord(text[i])
    #     if a >= 65 and a <= 90:
    #         upper += 1
    #     elif a >= 97 and a <= 122:
    #         lower += 1
    # print("Lower Case is ", lower)
    # print("Upper Case is ", upper)

    # print(isUrl())
    # print(removVowel())
    #print(splitlist('>cookies>milk>fudge>cake>ice cream', '>'))
    print(freqchar('rishabhrawat'))
