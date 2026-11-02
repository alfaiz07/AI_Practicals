# Vacuum Cleaner Simple Reflex Agent

environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while 'Dirty' in environment.values():

    print("\nLocation:", location)
    print("Status:", environment[location])

    if environment[location] == 'Dirty':
        print("Action: Suck")
        environment[location] = 'Clean'

    elif location == 'A':
        print("Action: Move Right")
        location = 'B'

    else:
        print("Action: Move Left")
        location = 'A'

print("\nBoth rooms are clean!")
print("Final Environment:", environment)
print("Performance: 100% Clean")