"""
Evan Choquette
18 December 2023

This program will allow the user to access lists of gift ideas for the people
the feel like giving gifts to!
"""

# Define global constants

 
def main():
    """Run the mainline logic of the program."""
    # Open program and welcome the user.
    print("Welcome to your gift list manager.")

    # Load directory into program for editing.
    
    # Display menu.

    # Let user make a selection.

    # Run different functions based on user selection.

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
def view_recipients():
    """Display the list of recipients and allow user to view the gift ideas
    for a selected recipient.
    """

    # Use for loop to print names in dict (the keys).

    # Ask user whose gift ideas they want to see. 

    # While recipient is not in list...
        # Inform user of error and ask again.

    # Pass input to fnc to view gift ideas.

# View gift ideas for a given recipient.
def view_gifts(queried_recip): 
    """Displays the gift ideas for a recipient as a bulleted list.
    :param queried_recip: person whose gift ideas are to be viewed
    :type: str
    """

    # Display a bulleted list, along with the recipient's name at the top.

    # Ask user what they would like to do with the list: return to main menu,
    # remove an item, or add an item. 

    # If add (option 1) send to add item. 

    # If remove (option 2) send to remove item.

    # Else return to main menu. 

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


