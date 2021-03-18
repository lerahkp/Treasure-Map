row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

j=int(position[0])
k=int(position[1])
print(j)
print(k)
if(j==1 and k==1):
  row1[0]="X"
elif(j==1 and k==2):
  row2[0]="X"
elif(j==1 and k==3):
  row3[0]="X"
elif(j==2 and k==1):
  row1[1]="X"
elif(j==2 and k==2):
  row2[1]="X"
elif(j==2 and k==3):
  row3[1]="X"
elif(j==3 and k==1):
  row1[2]="X"
elif(j==3 and k==2):
  row2[2]="X"
elif(j==3 and k==3):
  row3[2]="X"

print(f"{row1}\n{row2}\n{row3}")
