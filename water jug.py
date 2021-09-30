jug_1 = int(input("Enter the quantity of largest jug in lt: "))
jug_2 = int(input("Enter the quantity of jug 2 in lt: "))
answer = int(input("Enter the required answer: "))
count = 0
x = y = 0
rules_count = {}

while True:
  if x == answer and y == 0:
    break

  game_rule = int(input("Input Rule: "))
  
  if game_rule is 1: # Rule 1: x = max 
    x = jug_1 
  
  if game_rule is 2: # Rule 2: y = max 
    y = jug_2
  
  if game_rule is 3: # Rule 3: x = 0 
    x = 0
  
  if game_rule is 4: # Rule 4: y = 0 
    y = 0
  
  if game_rule is 5: # Rule 5: y -> x 
    y -= jug_1 - x
    x = jug_1 - x
  
  if game_rule is 6: # Rule 6: x -> y
    x -= jug_2 - y
    y = jug_2 - y

  if game_rule is 7: # Rule 7: (x+y, 0)
    x += y
    y = 0
  
  if game_rule is 8: # Rule 8: (0, x+y)
    y += x
    x = 0
  
  print(f"({x},{y})")
 
  if game_rule not in rules_count.keys(): 
    rules_count[game_rule] = 1
  else:
    rules_count[game_rule] += 1
    
  count += 1

#required Output
print(f"\nSteps neeeded = {count}")

for rule in sorted(rules_count.keys()):
  print(f"Rule {rule} is used {rules_count[rule]} times")