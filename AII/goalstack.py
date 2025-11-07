#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx


class GoalStackPlanner:
    def __init__(self, init, goal, acts):
        self.state = set(init)
        self.goal = goal
        self.actions = acts
        self.stack = list(goal)
        self.plan = []

    def sat(self, f):
        return f in self.state

    def apply(self, a):
        [self.state.discard(x) for x in a["del"]]
        [self.state.add(x) for x in a["add"]]

    def plan_steps(self):
        while self.stack:
            t = self.stack.pop()
            if isinstance(t, str):  # it's a goal
                if not self.sat(t):
                    for a in self.actions:
                        if t in a["add"]:
                            self.stack.append(a)
                            self.stack.extend(a["pre"])
                            break
            else:  # it's an action
                if all(p in self.state for p in t["pre"]):
                    self.apply(t)
                    self.plan.append(t["name"])
        return self.plan


# ---------- USER INPUT ----------
init = input("Initial facts (comma separated): ").split(',')
goal = input("Goal facts (comma separated): ").split(',')
n = int(input("Number of actions: "))
acts = []

for i in range(n):
    print(f"\nAction {i+1}:")
    name = input(" Name: ")
    pre = input(" Preconditions (comma separated): ").split(',')
    add = input(" Add list (comma separated): ").split(',')
    dele = input(" Delete list (comma separated): ").split(',')
    acts.append({"name": name, "pre": pre, "add": add, "del": dele})

planner = GoalStackPlanner(init, goal, acts)
print("\nGenerated Plan:", planner.plan_steps())


#Initial facts (comma separated): A_on_Table,B_on_Table,Clear_A,Clear_B
#Goal facts (comma separated): A_on_B
#Number of actions: 1

#Action 1:
 #Name: Stack_A_on_B
 #Preconditions (comma separated): A_on_Table,Clear_A,Clear_B
 #Add list (comma separated): A_on_B
 #Delete list (comma separated): A_on_Table,Clear_B

 # ------------------------------------------------------
# EXPLANATION OF THE CODE (GOAL STACK PLANNER)
# ------------------------------------------------------

# 📘 AIM:
# To generate a sequence of actions (plan) to reach a goal from the initial state 
# using a **Goal Stack Planner** approach (STRIPS-like AI planning).

# ------------------------------------------------------
# 🧩 CONCEPT USED
# ------------------------------------------------------
# **Goal Stack Planning**:
# - Uses a stack to keep track of goals and actions.
# - Pops items from the stack and satisfies them by applying actions.
# - Ensures all **preconditions** of actions are met before execution.
# - Produces an ordered plan to achieve the goal.

# ------------------------------------------------------
# 🧩 CODE EXPLANATION (LINE BY LINE)
# ------------------------------------------------------

# class GoalStackPlanner:
# → Defines the planner class to handle initial facts, goals, and actions.
# → Maintains a stack of goals/actions and a plan list.

# ------------------------------------------------------
# 1️⃣ INITIALIZATION
# ------------------------------------------------------
# def __init__(self, init, goal, acts):
#     self.state = set(init)
#     self.goal = goal
#     self.actions = acts
#     self.stack = list(goal)
#     self.plan = []
# → state: current facts
# → goal: list of goal facts
# → actions: available actions
# → stack: stack of goals/actions
# → plan: generated sequence of actions

# ------------------------------------------------------
# 2️⃣ CHECK IF GOAL IS SATISFIED
# ------------------------------------------------------
# def sat(self, f):
#     return f in self.state
# → Returns True if a fact is already satisfied in current state.

# ------------------------------------------------------
# 3️⃣ APPLY ACTION
# ------------------------------------------------------
# def apply(self, a):
#     [self.state.discard(x) for x in a["del"]]
#     [self.state.add(x) for x in a["add"]]
# → Updates the current state after performing an action.
# → Removes facts in the delete list, adds facts in the add list.

# ------------------------------------------------------
# 4️⃣ PLAN GENERATION
# ------------------------------------------------------
# def plan_steps(self):
#     while self.stack:
#         t = self.stack.pop()
#         if isinstance(t, str):  # it's a goal
#             if not self.sat(t):
#                 for a in self.actions:
#                     if t in a["add"]:
#                         self.stack.append(a)
#                         self.stack.extend(a["pre"])
#                         break
#         else:  # it's an action
#             if all(p in self.state for p in t["pre"]):
#                 self.apply(t)
#                 self.plan.append(t["name"])
#     return self.plan
# → Pops goals or actions from the stack.
# → If goal not satisfied, finds an action that achieves it.
# → Pushes action and its preconditions on stack.
# → If action preconditions satisfied, applies action and adds to plan.

# ------------------------------------------------------
# 5️⃣ USER INPUT
# ------------------------------------------------------
# init = initial facts (comma separated)
# goal = goal facts (comma separated)
# acts = list of actions with name, preconditions, add, delete lists

# Example Input:
# Initial facts: A_on_Table,B_on_Table,Clear_A,Clear_B
# Goal facts: A_on_B
# Number of actions: 1
# Action 1:
#  Name: Stack_A_on_B
#  Preconditions: A_on_Table,Clear_A,Clear_B
#  Add list: A_on_B
#  Delete list: A_on_Table,Clear_B

# ------------------------------------------------------
# 6️⃣ PLAN OUTPUT
# ------------------------------------------------------
# planner = GoalStackPlanner(init, goal, acts)
# print(planner.plan_steps())
# → Generates plan:
# ['Stack_A_on_B']

# ------------------------------------------------------
# 🧠 SIMPLE UNDERSTANDING
# ------------------------------------------------------
# - Stack keeps track of **unsatisfied goals** and actions.
# - The planner repeatedly chooses actions to satisfy goals.
# - Produces an **ordered sequence of actions** to achieve the goal.
# - Useful in AI for **robot planning**, **blocks world problems**, and automation.

# ------------------------------------------------------
# 🌍 REAL-TIME APPLICATIONS
# ------------------------------------------------------
# 1. Robot task planning (move objects in a sequence).
# 2. Automated assembly lines.
# 3. AI agents in games or simulations.
# 4. Planning operations in logistics or workflow automation.
# ------------------------------------------------------
