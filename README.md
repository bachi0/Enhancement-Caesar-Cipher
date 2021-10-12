# Enhancement-Caesar-Cipher
Modified Caesar Cipher Algorithm

## Caesar Cipher

Caesar Cipher was developed in 50 B.C, the credits go to Julius Caesar, as he was an influential ruler he didn’t want his messages to be known to the other country’s officials or his enemies, thus he came up with a way to encode his messages and this will be sent to the receiver through his trusted men or guards. Now this message can be decoded only by the receiver for whom it was meant for.

In cryptography, a Caesar cipher, also known as Caesar&#39;s cipher, the shift cipher, Caesar&#39;s code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25.[2] Encryption of a letter x by a shift n can be described mathematically as,

E n (x) = (x + n) mod 26.

Decryption is performed similarly,

D n(x) = (x − n) mod 26.

(There are different definitions for the modulo operation. In the above, the result is in the range 0 to 25; i.e., if x + n or x − n are not in the range 0 to 25, we have to subtract or add 26.)

The replacement remains the same throughout the message, so the cipher is classed as a type of mono alphabetic substitution.

The Caesar cipher can be easily broken even in a cipher text-only scenario. Two situations can be considered:

* An attacker knows (or guesses) that some sort of simple substitution cipher has been used, but not specifically that it is a Caesar scheme
* An attacker knows that a Caesar cipher is in use, but does not know the shift value.

## Proposed work

The aim is to enhance the Caesar cipher to raise the CIA level to the max. The original Caesar Cipher works by using a key to encrypt and decrypt however the enhanced version does not require a key.

Encryption process goes like this,

* **Step 1**: The index values of each of the alphabets ranging from 0-25 are taken therefore each alphabet is represented with its index value and these values are saved in an array.
* **Step 2**: Any variable is taken and then multiplied with the index
* **Step 3**: Values greater than 25 are saved in a separate array and modulo of 26 is taken for each of the values
* **Step 4**: Now values lesser than 20 have will have their array index added along with them
* **Step 5**: A random number ranging from 0-10 is generated for each of the values and are added along with them and modulo of 26 is taken for each of them. These random values are saved in an array which will be used for decryption.
* **Step 6**: Now these values are substituted to give the encrypted message

The reverse of this algorithm explains the Decryption.

## Methodology

* **Random Number generator**: This in built function is present in most of the programming languages. The main purpose of introducing this is it will be kind of challenging for the hacker to crack it because the same word when encrypted twice will give different versions which might make the hacker get confused of the approach
* **Variable Multiplication**: Any variable can be multiplied with each of the values to get different values just to add the challenging factor 
* **Array Index Addition**: This is added again to increase the challenging factor of the algorithm by adding the array index value of that particular value if it is lesser than 20.
