
rows, cols = (3, 3)
arr = [[" " for i in range(cols)] for j in range(rows)]

# returns true if every term in new array is the same
def check(arrr):
  result = all(element == arrr[0] for element in arrr)
  if (result and arrr[0] != " "):
    return True
  else:
    return False


def gameovercheck():
  #check if any rows, col, or diag have same character 
  
  col1 = [arr[0][0],arr[1][0],arr[2][0]]
  col2 = [arr[0][1],arr[1][1],arr[2][1]]
  col3 = [arr[0][2],arr[1][2],arr[2][2]]

  diag1 = [arr[0][0],arr[1][1],arr[2][2]]
  diag2 = [arr[0][2],arr[1][1],arr[2][0]]

 # Check if any possible win scenarios occur, if so return false 

  if check(arr[0]) or check(arr[1]) or check(arr[2]) or check(col1) or check(col2) or check(col3) or check(diag1) or check(diag2):
    return False #false means someone wins 
  else:
    return True #no one wins 


def player(ch,num):
  if ch == "x":
    oppchr="o"
  else:
    oppchr="x"

  row=int(input("What row do you want player " +num +": "))
  col=int(input("What col do you want player " +num+": "))

  if arr[row-1][col-1] ==" " and arr[row-1][col-1] != oppchr:
    arr[row-1][col-1] = ch
  print("")
  print("     col1  col2  col3")
  print("row 1", arr[0])
  print("row 2",arr[1])
  print("row 3",arr[2])
  print("")
  
print("     col1  col2  col3")
print("row 1", arr[0])
print("row 2",arr[1])
print("row 3",arr[2])
turns = 1
# game can only run 9 times max ever, check if < 9 and if no one wins (gameovercheck()==true)
while (turns <=9) and gameovercheck():
  if turns % 2 != 0:
    player("o","1")

  else:
    player("x","2")
  turns=turns+1

if turns == 10 and gameovercheck():
  print("DRAW") 
elif turns % 2!=0:
  print("player 2 wins!")
else:
  print("player 1 win!")

