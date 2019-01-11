def main():
    splitByAstrix = input().strip()
    i = 0
    while splitByAstrix != "END":
        splitByAstrix = splitByAstrix.split("*")
        if len(splitByAstrix) > 2:
            splitByAstrix = splitByAstrix[1:-1]
        if len(set(splitByAstrix)) == 1:
            print(i+1, "EVEN")
        else:
            print(i+1, "NOT EVEN")
        i += 1
        splitByAstrix = input().strip()

if __name__ == '__main__':
    main()
