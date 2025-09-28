"""
Displaying a menu-driven interface that greets or farewells the user by name.
Options: H for hello, G for goodbye, Q to quit.
Pseudocode:
    get name
    display menu
    get choice
    while choice != Q
       if choice == H
           display "hello" name
       else if choice == G
           display "goodbye" name
       else
           display invalid message
       display menu
       get choice
    display finished message
"""

# Get user's name
name = input("Enter name: ")

# Menu and get initial choice
MENU = "(H)ello\(G)oodbye\(Q)uit"
print(MENU)
choice = input(">>> ").upper()

# Choices until quit
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    # Menu and next choice
    print(MENU)
    choice = input(">>> ").upper()

# Display final message
print("Finished.")