class ParkingGarage():
    """A model of a garage that takes payment for tickets, keeps track of available parking spaces, and upates current status"""

    def __init__(self):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {'paid': False}

    def takeTicket(self):
        """decreases amount of tickets available by 1
        decreases amount of parking spaces available by 1"""
        self.tickets = list(range(1,10))
        self.parkingSpaces = list(range(1,10))
       # print(self.tickets)
        print("Welcome to JensGarage, please take your ticket")
        self.tickets.pop(0)
        self.parkingSpaces.pop(0)
        #print(self.tickets)
        #print(self.parkingSpaces)


    #Display an input that waits for an amount from the user and store it in a variable
    #If the payment variables not empty then -> display a message to the user that their ticket has been paid and they have 15mins to leave
    #This should update the "currentTicket" dictionary key "paid" to True
    def payForParking(self):  
        """takes payment for ticket, prints message to user on amount of time left and
        updates currentTicket dictionary ket "paid" to True"""

        amount =int(float(input( "Please enter your payment ")))
        if amount > 0:
            print("Your ticket has been paid and you have 15 minutes to leave")
            self.currentTicket['paid'] = True
        else:
            amount = int(float(input("Please enter your payment amount ")))
            self.currentTicket['paid'] = False
            if amount > 0:
                print("Your ticket has been paid and you have 15 minutes to leave")
                self.currentTicket['paid'] = True
            else:
                amount = input("Please enter your payment amount ")
                self.currentTicket['paid'] = False
        
    # If the ticket has been paid, display a message of "Thank You, have a nice day"
    #If the ticket has not been paid, display an input prompt for payment
    #Once paid, display message "Thank you, have a nice day!"
    #Update parkingSpaces list to increase by 1
    #Update tickets list to increase by 1
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print ("Thank you, have a nice day")
            #print(self.tickets)
            self.tickets.append(1)
            self.parkingSpaces.append(1)
            #print(self.parkingSpaces)
        else:
            print("Please enter your payment")
           
    

JensGarage = ParkingGarage()

def run():

    JensGarage.takeTicket()
    
    JensGarage.payForParking()

    JensGarage.leaveGarage()
    

run()