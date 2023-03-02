import sys

def main():
    offset = 197
    varName = ""

    print("Enter Function Name: ")
    cmdInput = str(input())

    print("Enter Varible Name: ")
    varName = str(input())

    print()

    userInput = ""
    for c in range(0,len(cmdInput)):
        userInput += (hex(ord(cmdInput[c])))

    userInput = userInput.replace("0x", '')
    print("Hex before encode = " + userInput)
    #only hex nubmers from C

    encodedHex = '"'
    plaintext = ''
    for i in range(0,len(userInput),2):
        hexByte = userInput[i:(i + 2)]
        val = int(hexByte,16)
        plaintext += chr(val)
        val += offset
        val = val % 256
        #intgar value established

        newhex = hex(val)
        if(val < 16):
            newhex = newhex[1:newhex.find('x')+1] + '0' + newhex[newhex.find('x')+1:]
        else: 
            newhex = newhex[1:]
        #fix if byte is low 0x2 for C++

        #print("Hex byte " + "0x" + hexByte + " is " + "0" + newhex)
        newhex = "\\" + newhex
        encodedHex += newhex
        #add bytes
        

    encodedHex = "unsigned char " + varName + "[] = " + encodedHex;
    encodedHex += '";'
    print("Plaintext buffer: " +  plaintext)
    print("\nFinal output: \n" + encodedHex)


main()