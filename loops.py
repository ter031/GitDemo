greeting = "good morning"

if greeting == "mrng":
    print("condition doesn't match")
else:
    print("condition matches")

print("if else block completed")

## for loop
obj = [2,3,5,7,9]
for x in obj:
    print(x*2, end=' ')

## sum of 1st 100 natural nos
summation = 0

for a in range(1,101,2):
    summation = summation + a
print(summation)
