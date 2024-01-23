# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation

# Make sure that your program runs like a program. It should have a while loop that repeats until the user decides to quit.

# When the project is completed, commit the final changes and submit your GitHub link.

# class Garage():

#     def __init__(self, total_tickets, total_ParkingSpaces):
#         self.tickets = list(range(1, total_tickets + 1))
#         self.ParkingSpaces = list(range(1, total_ParkingSpaces + 1))
#         self.currentTicket = {}

#     def takeTicket(self):
#         if self.tickets:

class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket = {"ticket_number": ticket_number, "parking_space": parking_space, "paid": False}
            print(f"Ticket {ticket_number} issued. Park at space {parking_space}.")

    def payForParking(self):
        if not self.currentTicket:
            print("No ticket to pay for.")
            return

        payment = input("Enter the amount to pay: ")
        if payment:
            print(f"Ticket {self.currentTicket['ticket_number']} has been paid. You have 15 minutes to leave.")
            self.currentTicket['paid'] = True
            ticket_number = self.tickets
            parking_space = self.parkingSpaces

    def leaveGarage(self):
        if not self.currentTicket:
            print("No ticket to leave.")
            return

        if self.currentTicket['paid']:
            print("Thank you, have a nice day!")
        else:
            payment = input("Payment pending. Enter the amount to pay: ")
            if payment:
                print("Thank you, have a nice day! (Ticket paid)")
                self.currentTicket['paid'] = True

                # Release parking space and ticket for reuse
                self.parkingSpaces.append(self.currentTicket['parking_space'])
                self.tickets.append(self.currentTicket['ticket_number'])

# Example usage:
def lot():
    lot = ParkingGarage(total_tickets=10, total_parking_spaces=10)

    while True:
        print("\nOptions:")
        print("1. Take a ticket")
        print("2. Pay for parking")
        print("3. Leave the garage")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            lot.takeTicket()
        elif choice == '2':
            lot.payForParking()
        elif choice == '3':
            lot.leaveGarage()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


lot()










