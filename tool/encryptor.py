import string

# Encrypt the normal position numbers into Bend-Tech's weird encryption
def encrypt(num) :
    numList = list(str(num))
    encryptedDigits = []
    numLen = len(numList)

    if numLen == 1 :
        digit = int(numList[0])

        if (digit >= 0) and (digit <= 6) :
            encryptedDigits.append(str(digit + 3))
        elif (digit == 7) :
            encryptedDigits.append(":")
        elif (digit == 8) :
            encryptedDigits.append(";")
        elif (digit == 9) :
            encryptedDigits.append("<")

    elif numLen == 2 :
        for i in numList :
            digit = int(numList[i])

            if (digit >= 0) and (digit <= 6) :
                encryptedDigits.append(str(digit + 3))
            elif (digit == 7) :
                encryptedDigits.append(":")
            elif (digit == 8) :
                encryptedDigits.append(";")
            elif (digit == 9) :
                encryptedDigits.append("<")
        
        encryptedDigits.sort(reverse=True)

    elif numLen == 3:
        for i in numList : 
            digit = int(numList[i])

            if i == 2 :
                if (digit >= 0) and (digit <= 7) :
                    encryptedDigits.append(str(digit + 2))
                elif (digit == 8) :
                    encryptedDigits.append(":")
                elif (digit == 9) :
                    encryptedDigits.append(";")
            elif i == 1 :
                if (digit >= 0) and (digit <= 6) :
                    encryptedDigits.append(str(digit + 3))
                elif (digit == 7) :
                    encryptedDigits.append(":")
                elif (digit == 8) :
                    encryptedDigits.append(";")
                elif (digit == 9) :
                    encryptedDigits.append("<")
            elif i == 0 :
                if (digit >= 0) and (digit <= 6) :
                    encryptedDigits.append(str(digit + 3))
                elif (digit == 7) :
                    encryptedDigits.append(":")
                elif (digit == 8) :
                    encryptedDigits.append(";")
                elif (digit == 9) :
                    encryptedDigits.append("<")
            
        encryptedDigits.sort(reverse=True)

    encryptedNum = "".join(encryptedDigits)

    return(encryptedNum)