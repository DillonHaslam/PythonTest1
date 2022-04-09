
nodes = int(input("Input number of nodes in truss: "))

while(nodes < 2):
   nodes = int(input("Please enter a number greater than 1: "))

print(nodes)

locations = [[0 for col in range(nodes)] for row in range(2)]

for i in range(nodes):
    locations[i-1][0] = int(input("Input x coordinate of node " + (str)(i + 1) + ": "))
    locations[i-1][1] = int(input("Input x coordinate of node " + (str)(i + 1) + ": "))
