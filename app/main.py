import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)
 
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    error = False
    # Uncomment this block to pass the first stage
    line=1
    i=0
    #for c in file_contents:
    while i < len(file_contents):
        c=file_contents[i]
        if c == "=":
            if i+1 <len(file_contents) and file_contents[i+1]=="=":
                print("EQUAL_EQUAL == null")
                i+=2
            else:
                print("EQUAL = null")
                i += 1
        elif c == "(":
            print("LEFT_PAREN ( null")
            i += 1
        elif c == "\n":
            line += 1
            i += 1
        elif c == " " or c == "\r" or c == "\t":
            pass
            i += 1
        elif c == ")":
            print("RIGHT_PAREN ) null")
            i += 1
        elif c == "{":
            print("LEFT_BRACE { null")
            i += 1
        elif c == "}":
            print("RIGHT_BRACE } null")
            i += 1
        elif c == ",":
            print("COMMA , null")
            i += 1
        elif c == ".":
            print("DOT . null")
            i += 1
        elif c == "-":
            print("MINUS - null")
            i += 1
        elif c == "+":
            print("PLUS + null")
            i += 1
        elif c == ";":
            print("SEMICOLON ; null")
            i += 1
        elif c == "*":
            print("STAR * null")
            i += 1
        elif c == "/":
            if i+1 <len(file_contents) and file_contents[i+1]=="/":
                #print("BANG_EQUAL != null")
                #i+=2
                while i < len(file_contents) and file_contents[i] != '\n':
                    i += 1
                i+1
                continue
            else:
                print("SLASH / null")
                i += 1
        elif c == ">":
            if i+1 <len(file_contents) and file_contents[i+1]=="=":
                print("GREATER_EQUAL >= null")
                i+=2
            else:
                print("GREATER > null")
                i += 1
        elif c == "<":
            if i+1 <len(file_contents) and file_contents[i+1]=="=":
                print("LESS_EQUAL <= null")
                i+=2
            else:
                print("LESS < null")
                i += 1
        elif c == "!":
            if i+1 <len(file_contents) and file_contents[i+1]=="=":
                print("BANG_EQUAL != null")
                i+=2
            else:
                print("BANG ! null")
                i += 1
        elif c == '"':
            i += 1
            start = i
            while i < len(file_contents) and file_contents[i] != '"':
                i += 1
            if i < len(file_contents) and file_contents[i] == '"':
                print(f'STRING "{file_contents[start:i]}" {file_contents[start:i]}')
                i += 1
            else:
                print(f"[line {line}] Error: Unterminated string.", file=sys.stderr)
                error = True
        else:
            error = True
            #line_number=file_contents.count("\n",0,file_contents.find(c))+1
            print("[line %s] Error: Unexpected character: %s" %(line,c),
                  file=sys.stderr,
                  )
            i += 1
    print("EOF  null") # Placeholder, remove this line when implementing the scanner
    if error:
        exit(65)
    else:
        exit(0)

if __name__ == "__main__":
    main()
