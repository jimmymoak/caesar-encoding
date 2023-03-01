import sys

def main():
    offset = 197

    file = open('encPayload.txt', 'r')
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

    encodedHex = '"'
    print("Decoding Data: " + data[:50])
    for i in range(0,len(data),2):
        hexByte = data[i:(i + 2)]
        val = int(hexByte,16)
        val -= offset % 256
        val = val % 256
        
        encodedHex += str(chr(val))
        #print(str(chr(val)))
        #add bytes
        

    encodedHex = "unsigned char buf[] = " + encodedHex;
    encodedHex += '";'
    print("Final output: " + encodedHex)

    #unencPayload = open("unencPayload.txt", 'w')
    #unencPayload.write(encodedHex)
    #unencPayload.close()


main()