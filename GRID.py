#Get user input for size of grid.
col = input('How many columns would you like?')
row = input('How many rows would you like?')
grid = [col, row]

#convert input strings into integers.
col = int(col)
row = int(row)

#create columns
def createcol():
    print(list(range(0, col))) 
    
#create rows
for x in range(row):
    createcol()

print("DONE")
