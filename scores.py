scores=[]
#print(len(scores))
for i in range (3):
    n = int(input("Enter a number "))
    scores.append(n)
print(scores)

average = sum(scores)/len(scores)
print("Average:",average)
print(f"Average:{average}")