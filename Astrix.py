def main():
    for i in range(1000):
        even = True
        inputx = input().split('*')
        if(len(inputx)==1 and inputx[0]=='END'):
            break
        else:
            splitByAstrix = list(filter(None, inputx))
            if(len(splitByAstrix)==1):
                print(i+1, "NOT EVEN")
                even = False
            else:
                if(len(splitByAstrix)):
                    oldValue = len(splitByAstrix[0])
                for values in splitByAstrix:
                    splitByDot = len(values)
                    if(splitByDot!=oldValue):
                        print(i+1, "NOT EVEN")
                        even = False
                        break
                    oldValue = splitByDot
                if even:
                    print(i+1, "EVEN")
if __name__ == '__main__':
    main()
//main body has been changed 
