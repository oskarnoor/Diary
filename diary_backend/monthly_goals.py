class MonthlyGoals:
    def __init__(self, goal0, goal1, goal2):
        self.goal0 = goal0
        self.goal1 = goal1
        self.goal2 = goal2


goal2 = ""
goal0 = input("What is your first goal this month? ")
goal1 = input("What is your second goal this month? (leave empty for only one goal) ")
if goal1 == "":
    goal1 = "EMPTINESS"
else:
    goal2 = input("What is your third goal this month? (leave empty for only two goals) ")
if goal2 == "":
    goal2 = "EMPTINESS"

goals = MonthlyGoals(goal0, goal1, goal2)

goal = [goal0, goal1, goal2]
