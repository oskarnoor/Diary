from .monthly_goals import goal
from .previous_dates import PreviousDates
from .today import Today
from .encrypter import encryptedGoals


print(len(encryptedGoals))

for i in range(len(encryptedGoals)):
    file = open("data.txt", "w")
    file.write(f"Goal{i+1}:::{encryptedGoals[i]}")
    file.close()





