import string
from .decrypted_goals import data as goals


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)


class Encrypter:
    def __init__(self, decryption_text):
        self.encryption = decryption_text


decryptedGoals = []

for i in range(len(goals)):


    encryption = goals[i]

    if encryption == "EMPTINESS":
        continue
    else:
        password = ""
        if "81^1mnfa.,1&adFra1*13T1maul/1dADmb" in encryption and "X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz" in encryption:

            key = ['>', '*', 'K', 'Y', 'W', '?', '1', '%', '$', ' ', '8', 's', 'k', '=', '`', 'M', ';', '\\', '2', '/', '4',
                   'b', 'B', '~', '&', 'c', '3', ':', '<', 'h', 'L', 'v', 'j', 'l', '.', '|', '"', 'n', 'P', 'F', '_', 'C', 'G',
                   '^', 'Q', '(', 'z', '6', 'o', 'r', 'q', 'D', 'g', 'X', 'y', ']', 'i', '}', 'u', 'p', 't', '{', '[', '!', '0',
                   'x', 'A', 'J', 'T', '+', 'w', 'a', "'", '#', '@', 'Z', 'm', 'N', 'V', '7', 'R', ')', 'O', 'd', '9', 'S', 'E',
                   'f', '-', ',', 'H', 'e', 'U', 'I', '5']
            encryption = encryption.replace("X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz", "")
            encryption = encryption.replace("81^1mnfa.,1&adFra1*13T1maul/1dADmb", "")
            for letter in encryption:

                index = key.index(letter)
                password += chars[index]


        if "72&9jeKx0$4LbVp8u5Rc1umM;kf35UF(A%Q" in encryption and "J6dC9eI3uK0oM4kT8zYxP2sB7vA1rZ5wSfGnH" in encryption:

            key = ['(', ')', '\\', 'm', '.', 'h', '0', ']', 'o', 'k', 'O', 'B', '8', ' ', 'J', 'x', 'Z', 'U', 'u', '@', 'K',
                   'E', ',', '}', '*', 'v', 'l', 'y', 'S', '`', 's', '<', '5', 'e', '+', 'z', '4', 'n', 'i', '1', ':', 'V', 'T',
                   'C', 'W', '$', 'c', ';', '{', 'g', 'd', 'G', '3', 'D', 't', 'w', 'H', '%', '"', 'a', 'p', '[', 'r', 'Y', 'M',
                   'q', '&', 'Q', 'N', 'f', 'b', '6', 'A', '#', "'", '|', '9', '?', '>', '^', '7', '2', '_', 'F', '!', '~', '-',
                   'X', 'I', '/', 'R', 'P', '=', 'L', 'j']
            encryption = encryption.replace("J6dC9eI3uK0oM4kT8zYxP2sB7vA1rZ5wSfGnH", "")
            encryption = encryption.replace("72&9jeKx0$4LbVp8u5Rc1umM;kf35UF(A%Q", "")
            for letter in encryption:

                index = key.index(letter)
                password += chars[index]


        if "P5s@kRjFzLw6qXe2nDcnGh24&)g!2tYY" in encryption and "G2yT5vBxP1b$uC4wN6mH9nL3zW7kQ0aD8eSfR" in encryption:

            key = ['l', 'U', '7', 'd', 'E', 'e', '3', 'm', 'B', '6', '\\', '}', '.', "'", '~', ';', '0', ' ', '^', '&', 'L', '*', 'D', 'x', ')', 'C', '9', 'P', ']', '|', '#', '/', ',', '{', 'X', '5', 'b', 'f', '"', '(', '8', '`', '-', 'n', '!', '[', 'Q', 'R', '=', 'z', 'p', 'o', 'W', ':', '4', 'w', 'k', '2', 'T', 'I', '@', 'G', 'h', 'u', '?', 'S', 't', 'Z', 'v', 's', 'r', 'q', '+', 'N', 'y', '1', 'O', 'i', '<', 'g', 'K', 'A', '$', '>', '_', 'V', 'j', 'H', '%', 'c', 'Y', 'F', 'J', 'M', 'a']
            encryption = encryption.replace("G2yT5vBxP1b$uC4wN6mH9nL3zW7kQ0aD8eSfR", "")
            encryption = encryption.replace("P5s@kRjFzLw6qXe2nDcnGh24&)g!2tYY", "")
            for letter in encryption:

                index = key.index(letter)
                password += chars[index]


        if "G9Ynaf&6)=ev#mAiEhW3xUo7tBpQl';r" in encryption and "E5vBpQlA9rZ2wS6xD7cF1gH3jM0kT4zN8uYiO" in encryption:

            key = ['O', '@', '_', '^', '(', 'A', 'I', 'Z', 'B', '|', '}', ',', 'c', '6', "'", 'K', 'o', 'u', ')', '<', 'H', 'y', 'E', 'f', 'm', '#', 'b', 'v', 'V', 'w', '%', 'Q', '`', 'C', 'l', '2', 'N', '+', '{', 'h', '1', ']', ':', 'k', 'i', 'x', '*', 'p', '"', '4', 'z', 'e', '.', 'D', '$', ' ', '!', '9', 'X', 'd', '8', 'J', 'L', 'F', 's', 'j', '7', '0', '~', '-', 'g', '3', '&', 'n', 'Y', 'W', '/', '=', '5', ';', 't', 'S', '>', '[', 'R', 'a', 'T', '?', 'P', 'G', 'U', 'q', 'r', 'M', '\\']
            encryption = encryption.replace("E5vBpQlA9rZ2wS6xD7cF1gH3jM0kT4zN8uYiO", "")
            encryption = encryption.replace("G9Ynaf&6)=ev#mAiEhW3xUo7tBpQl';r", "")
            for letter in encryption:

                index = key.index(letter)
                password += chars[index]


        if "T2z$uHd\\']19lmMnaNfA8rVbC1gMwX" in encryption and "R7kTzYxP4sCmW9nHdQ2fGvBjL6aV1eU8oI3uK" in encryption:

            key = ['G', 'T', ')', 'n', 'J', '>', '4', 'x', '(', 'w', 'a', '\\', 'h', 'e', '=', 'f', 'r', 'u', '2', 'I', 'E', '{', 'H', ' ', '%', '6', 'g', 'v', '1', 'F', 'R', 'A', '7', 'W', '5', "'", 'c', '"', ':', '|', 'i', 'P', 'V', '0', 'C', '!', 'U', '#', '$', 'S', 'b', '}', 'y', 'D', 'Z', 'q', 'd', 'l', 'M', 'B', ';', ']', 's', 't', 'p', '.', 'O', '-', '^', '[', '/', 'z', '*', 'K', '@', 'k', 'j', 'X', '~', '_', 'Y', '+', 'o', '<', '8', 'm', '`', '9', ',', 'L', '3', '&', 'N', 'Q', '?']
            encryption = encryption.replace("R7kTzYxP4sCmW9nHdQ2fGvBjL6aV1eU8oI3uK", "")
            encryption = encryption.replace("T2z$uHd\\']19lmMnaNfA8rVbC1gMwX", "")
            for letter in encryption:

                index = key.index(letter)
                password += chars[index]

        decryptedGoals += [password]
