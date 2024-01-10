"""
Evan Choquette
18 December 2023

This program will allow the user to access lists of gift ideas for the people
the feel like giving gifts to!
"""
# Import modules.
import pickle

# Define global constants
MAIN_MENU = ["View Recipients", "Add Recipient", "Remove Recipient", "Exit Program"]
RECIPIENT_MENU = ["View Gift List", "Add Item", "Remove Item", "Return to Main Menu"]
VIEW = 1
ADD = 2
REMOVE = 3
EXIT = 4
 
def main():
    """Run the mainline logic of the program."""
    # Open program and welcome the user.
    print("Welcome to your gift list manager.")

  # Read pkl file into dictionary.
  with open('gift_ideas.pkl', 'rb') as pick:
	  gift_dict = pickle.load(pick)
    
    # Display menu.
    for option in enumerate(MAIN_MENU):
		  print(option)
		
    # Let user make a selection.
    selection = int(input("What would you like to do? >>>"))
    while not selection.isalnum():
      print("Please enter an integer from 1 to 3.")
      selection = int(input("What would you like to do? >>>")
	
    # Run different functions based on user selection.
    if selection == VIEW:
      view_recipients(gift_dict)
                      
                      

# Display menu.
# Menu should allow user to add and remove people, view a list of people that
# have a gift list, edit the lists for a person, and exit the program.

# Add user function.
def add_user(new_recipient, thick_dict):
    """Add the provided user to the list of gift recipients and create an empty
    list to store the items they may want. Entry is added to dictionary.
    :param new_recipient: person being added to the directory
    :type new_recipient: str
    :param directory_dict: directory containing all the gift recipients and
     their gift ideas
    :type directory_dict: dict
    :returns thick_directory: directory with new recipient added
    :rtype: dict
    """
    
    # While recipient already exists...

        # Inform user that recipient is already included.

    # Add recipient to the dictionary as a key, and make an empty list for the
    # value.

    # Return updated dictionary.

# Remove user function.
def del_user(old_recipient, thin_dict): 
    """Remove the provided recipient from the list of gift recipients (i.e.,
    from the dictionary). Return the updated dictionary.
    :param old_recipient: person being removed from the directory
    :type: str
    :param directory_dict: dictionary containing all the gift recipients and
     their gift ideas
    :type: dict
    :returns thin_directory: directory with old recipient removed
    :rtype: dict
    """

    # While recipient doesn't exist...
        # Inform user that the recipient can't be removed. 

    # Remove recipient from dictionary.

    # Return updated dictionary.

# View recipents as a list.
def view_recipients(recip_dict):
    """Display the list of recipients and allow user to view the gift ideas
    for a selected recipient.
    :param recip_dict: the complete recipient/gift idea dictionary
    :type: dict
    """

    # Use for loop to print names in dict (the keys).
	print("Whose gift list would you like to access?")
	for name, list in recip_dict:
		print(name)
	# Prompt user to select a recipient's list.
	desired_recip = input(">>> ") 

    # While recipient is not in list...
	while desired_recip not in recip_dict:
        # Inform user of error and ask again.
		print("The selected recipient does not exist.")
		desired_recip = input("Select again. ")

	desired_list = recip_dict[desired_recip]

    # Pass input to fnc to view gift ideas.
	print(f"What would you like to do with {desired_recip}'s gift list?")
	for option in enumerate(RECIPIENT_MENU):
		print(option)
	menu_selection = int(input(">>> "))

	if menu_selection == VIEW:
		view_gifts(desired_recip, desired_list)
	elif menu_selection == ADD:
		
	

# View gift ideas for a given recipient.
def view_gifts(queried_recip, queried_list): 
    """Displays the gift ideas for a recipient as a bulleted list.
    :param queried_recip: recipient whose gift ideas are to be viewed
    :type: str
    :param queried_list: list of gift ideas for the queried recipient
    :type: list
    """

    # Display a bulleted list, along with the recipient's name at the top.
	print(queried_recip)
	for idea in queried_list:
		print(f"- {idea}")

# Add new item to the recipient's list.
def add_item(new_gift, all_ideas):
    """Adds a gift idea to a recipients list of gift ideas.
    :param new_gift: the gift idea to be added to the recipient's list
    :type: str
    :param all_ideas: gift list for the recipient
    :type: list
    :returns thick_ideas: gift list with added item
    :rtype: list
    """

# Remove an item from the recipient's list. 
def del_item(old_gift, all_ideas):
    """Removes a gift idea from the recipients list of gift ideas.
    :param old_gift: the gift idea to be removed from the recipient's list
    :type: str
    :param all_ideas: gift list for the recipient
    :type: list
    :returns thin_ideas: gift list without the removed item
    :type: list
    """

# Exit the program.
def sign_off():


