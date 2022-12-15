# RBSAPSS_Cipher
Its a group project of a program which is a special kind of cryptosystem where same plaintext can generate different cipher text also same Cipher text can generate different plain text.    
RBSAPSS Cipher

1. First we take the plain text as input
	 [Think it that its “ ABCDAB”]
2. Now we need the key which contains 3 random index value a

3. We can see that the whole text is combined with 6 letter. So if the key is [1] [2] [3] [random]
	
 	As we divide it 6 / 3 = 2 [for a easy way]

 Then the plain text will be divided by 2 part as “ABC” “DAB”

And after every 3index value the key will be repeated.

4. 

A-->1-->ENCRYPT-->B-->1-->DECRYPT-->A

B-->2-->ENCRYPT-->D-->2-->DECRYPT-->B

C-->3-->ENCRYPT-->F-->3-->DECRYPT-->C

D-->1-->ENCRYPT-->E-->1-->DECRYPT-->D

A-->2-->ENCRYPT-->C-->2-->DECRYPT-->A

B-->3-->ENCRYPT-->E-->3-->DECRYPT-->B


ENCRYPTION FORMULA

E=(P1+K1) mod 26

here ,P1 First index of the plain text;

k1= randomly taken first key; [here, P1 = I(A) = 0; k1 = 1]


E=(P2+K2) mod 26

here B = 1 which is plain text (index 1)

for P2 the key will be K2 which is 2(randomly taken)

[B-->2-->ENCRYPT-->D-->2]

E=(P3+K3) mod 26

here C = 0 which is plain text (index 2)

for P3 the key will be K3 which is 3(randomly taken)

[C-->3-->ENCRYPT-->F-->3]

E=(P4+K1) mod 26

here C = 0 which is plain text (index 3)

for P4 the key will be K3 which is 1(randomly taken)

[D-->1-->ENCRYPT-->E-->1]




E=(P5+K2) mod 26

here C = 0 which is plain text (index 4)

for P5 the key will be K3 which is 2(randomly taken)

[A-->2-->ENCRYPT-->C-->2]


E=(P6+K3) mod 26

here C = 0 which is plain text (index 5)

for P6 the key will be K3 which is 3(randomly taken)

[B-->3-->ENCRYPT-->E-->3]

5. then use the decryption formula 
	 
	D1 = (E1-K1) mod 26 
