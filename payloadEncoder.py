import sys

def main():
    offset = 197

    file = open('payload.txt', 'r')
    #open file

    data = file.read().replace("\n",'')
    data = data[data.find('=')+1:]
    #aquire big string

    data = data.replace('"', '')
    data = data.replace("\\x", '')
    data = data.replace("\t", '')
    data = data.replace(" ", '')
    data = data.replace(";", '')
    #only hex nubmers from C

    #check only good Chars
    for c in range(ord('g'), ord('z')):
        for i in range(len(data)):
            if(ord(data[i]) == c or ord(data[i]) == (c-32)):
                print("Unknown Char Detected!")
                print("Unknown Char ==  " + data[i])
                return

    encodedHex = '"'
    print("====== USING OFFSET " + str(offset) + " ======")
    print("Encoding Data: " + data[:50])
    for i in range(0,len(data),2):
        hexByte = data[i:(i + 2)]
        val = int(hexByte,16)
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
        

    encodedHex = "unsigned char shellBuf[] = " + encodedHex;
    encodedHex += '";'
    print("Final output: " + encodedHex)

    encPayload = open("encPayload.txt", 'w')
    encPayload.write(encodedHex)
    encPayload.close()



main()