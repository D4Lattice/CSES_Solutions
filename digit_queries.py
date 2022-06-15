num_of_inputs = int(input())
positions = []
num_range = []

for x in range(num_of_inputs):
    y = input()
    positions.append(int(y))
    
upper_limit = max(positions)

for y in range(upper_limit):
    num_range.append(y+1)
    
fullnum = "".join(str(e) for e in num_range)
for x in positions:
    print(fullnum[x-1])
