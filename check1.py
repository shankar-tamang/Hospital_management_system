with open('appointment.txt') as file:
        lines = file.readlines()
        new = "".join(lines[0])
        print(new)