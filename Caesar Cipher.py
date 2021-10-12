import random


def cal():
    #ENCRYPTION PART
    # print("Encryption Part:")
    txt = input("Enter the Plain Text : ")
    a = txt.split(" ")
    AlphaBet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']
    Encrypt = []
    Big = []
    BigNum = {}
    Decrypt = []
    DecryptText = []
    CopyRandom = []
    charIndex = []
    EncryptText = []
    multiplier = random.randint(1, len(a) - 1)
    for i in range (0, len(a)):
        n = AlphaBet.index(a[i])
        charIndex.append(n)
        val = n * multiplier
        if val > 26:
            BigNum[i] = val
        val = val % 26
        if val < 20:
            val = val + i
            Encrypt.append(val)
        else:
            Encrypt.append(val)
    
    for i in range (0, len(Encrypt)):
        r = random.randint(0, 10)
        CopyRandom.append(r)
        Encrypt[i] = Encrypt[i] + r
        Encrypt[i] = Encrypt[i] % 26
        EncryptText.append(AlphaBet[Encrypt[i] % 26])
                
    #DECRYPTION PART

    for i in range (0, len(Encrypt)):
        Encrypt[i] = Encrypt[i] - CopyRandom[i]
        if Encrypt[i] < 20:
            Encrypt[i] = Encrypt[i] - i
        if i in BigNum:
            Encrypt[i] = BigNum[i]
        Decrypt.append(Encrypt[i] // multiplier)
        DecryptText.append(AlphaBet[Decrypt[i]])

    print("\nValue of the given text : ")
    for i in charIndex:
        print(i, end = " ")
    
    print("\nMultiplier -> ",multiplier)
    
    print("\nNumbers > 26 : ")
    for i in BigNum.values():
        print(i, end = " ")
    
    print("\nRandom Values generated : ")
    for i in CopyRandom:
        print(i, end = " ")

    # print("\nEncypted values is :")
    # for i in Encrypt:
    #     print(i, end = " ")

    print("\nEncypted Text is :")
    for i in EncryptText:
        print(i, end = " ")

    # print("\nDecypted values  is :")
    # for i in Decrypt:
    #     print(i, end = " ")
    
    print("\nDecypted Text is :")
    for i in DecryptText:
        print(i, end = " ")

if __name__ == "__main__":
    cal()