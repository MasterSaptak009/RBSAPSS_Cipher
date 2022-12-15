import random

def key_generator():
    a=random.randint(0,25)
    b=random.randint(0,25)
    c=random.randint(0,25)
    key=(a,b,c)
    return key

def encrypt(plain_text):
    key=key_generator()
    cipher_text=""
    ln=len(plain_text)
    j=0
    for i in range(0,ln):
        # ch=''
        if(j>2):
            j=0
        if(plain_text[i]==' '):
            cipher_text+=cipher_text.join(' ')
            continue
        elif(plain_text[i].isupper()):
            ch=chr((ord(plain_text[i])-65+key[j])%26+65)
        else:
            ch=chr((ord(plain_text[i])-97+key[j])%26+97)
        cipher_text+=cipher_text.join(ch)
        j+=1
    return key,cipher_text


def decrypt(key,cipher_text):
    plain_text=""
    ln=len(cipher_text)
    j=0
    for i in range(0,ln):
        if(j>2):
            j=0
        if(cipher_text[i]==' '):
            plain_text+=plain_text.join(' ')
            continue
        if(cipher_text[i].isupper()):
            ch=chr(((ord(cipher_text[i])-65)-key[j])%26+65)
        else:
            ch=chr((((ord(cipher_text[i])-97)-key[j])%26)+97)
        plain_text+=plain_text.join(ch);
        j+=1
    return plain_text


if __name__=="__main__":
     while(True):        
        print("1. Encrypt\n2. Decrypt\n3. Exit\n")
        choice=int(input("Enter your choice- "))
        print()
        if(choice==1):
            text=input("Enter the text to encrypt- ")
            key,cipher=encrypt(text)
            print(f"Key= {key}\nCipherText= {cipher}")
        elif(choice==2):
            cipher=input("Enter the Cipher Text to decrypt- ")
            user_in=input("Enter the keys space seperated- ")
            key=tuple(int(i) for i in user_in.split())
            plain_text=decrypt(key,cipher)
            print("Decrypted Plain Text- "+plain_text)
        elif(choice==3):
            exit()
        else: print("Invalid Choice, Try again.")
        print()