#|************************WHILE LOOP************************|
# When the conditon is met, the statement block is executed cyclically, to end the loop use break or continue.
i =0 
while i<= 9:
    i+=1
    if i == 3:
        print("Exit the loop")
    if i ==5:
        print("Exit the current big loop")
    print(i)