# by Devansh
hot = input("Do you want something hot? (yes/no): ").strip().lower() == "yes"
healthy = input("Do you want something healthy? (yes/no): ").strip().lower() == "yes"
if hot and healthy :
    print("Soup")
elif hot and (not healthy ):
    print("Pizza")
elif (not hot ) and healthy :
    print("Salad")
else:
    print("Sandwich")
