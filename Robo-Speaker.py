import os
if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 created by Shrey")
    while True:
        x = input("Enter Word you want me to speak: ")
        if x == "q":
            break
        command = f"Say {x}"
        os.system(command)
