



try:
    from .decrypter import decryptedGoals
    with open("data.txt", "r") as file:
        toDecrypt = [file.read()]


except FileNotFoundError:
    from .encrypter import encryptedGoals


    for i in range(len(encryptedGoals)):
        with open("data.txt", "a") as file:
            file.write(f"{encryptedGoals[i]}\n")
            file.close()


