def Tokenize(text,endtext,startint):
    startinto = startint
    while True:
        if text[startint] == endtext:
            break
        else:
            startint = startint + 1
    returname = text[startinto:startint]
    return returname