for i in range(1, 5):
    for j in range(1, 6):
        if j < i + 1:
            print("🌼", end=" ")
        else:
            print(end="A ")
        
    print("")

print("process finished")    
