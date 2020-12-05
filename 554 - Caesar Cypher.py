dic = []
for i in range(100):  # Dictionary Input
    vr = input()
    if vr != '#':
        dic.append(vr)
    else:
        break

cipherstr = input()  # Cipher String Input
parr = []
k = 1
for j in range(0, 26):  # Computing all the 26 possible cipher strings
    nstr = ''
    for i in cipherstr:
        if i == ' ':
            nstr += chr(64 + 27 - k)
        elif not((ord(i) - k) < 65):
            nstr += chr(ord(i) - k)
        elif (ord(i) - k) == 64:
            nstr += ' '
        else:
            nstr += chr(ord(i) + 27 - k)
    k += 1
    parr.append(nstr)  # Storing each of possible De-Ciphered texts in parr

kmax = 0
kpos = 0
for i in range(len(parr)):  # Checking which De-Ciphered string contains the
    mx = 0  # most words from the dictionary
    for word in dic:
        if word in parr[i]:
            mx += 1
    if mx > kmax:
        kmax, kpos = mx, i
var = parr[kpos]
output = []
i = 0
count = 0
while i < len(var):  # Left Aligning the Chosen De-Ciphered string
    if count < 60:
        output.append(var[i])
        count += 1
    else:
        if var[i] != ' ':
            while var[i] != ' ':
                i -= 1
                output.pop()
            while output[-1] == ' ':
                output.pop()
            output.append('\n')
            count = 0
        else:
            while output[-1] == ' ':
                output.pop()
            output.append('\n')
            while var[i + 1] == ' ':
                i += 1
            count = 0
    i += 1
while output[0] == ' ':  # Removing all the spaces from the start
    output.pop(0)
while output[-1] == ' ':  # Removing all the space from the end
    output.pop()
print(''.join(output))  # Displaying the processed De-Ciphered String
