# This class represents a Help Desk ticket
class Ticket:
    # A counter to keep track of ticket numbers
    counter = 0

    # Constructor to create Ticket objects with basic information that is required
    def __init__(self, staff_id, creator_name, contact_email, description):
        Ticket.counter += 1
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    # Deals with password change requests by generating a new password for a ticket, providing a response to
    # the ticket and closing the ticket
    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password: {new_password}"
            self.status = "Closed"

    # Provides a response to a ticket
    def respond(self, response):
        self.response = response

    # Reopens a tickect that has been closed
    def reopen(self):
        self.status = "Reopened"

    # Calculates ticket statistics given a list of tickets
    @staticmethod
    def ticket_stats(ticket_list):
        # Calculates the total number of tickets currently
        total_tickets = len(ticket_list)
        # Calculates the total number of resolved/closed tickets currently
        resolved_tickets = sum(1 for ticket in ticket_list if ticket.status == "Closed")
        # Calculates the total number of open tickets currently
        open_tickets = total_tickets - resolved_tickets
        # Returns the total number of tickets, resolved/closed tickets and open tickets
        return total_tickets, resolved_tickets, open_tickets

    # Displays the information about the tickets
    def display_ticket(self):
        print("Ticket Number:", self.ticket_number)
        print("Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Status:", self.status)
        print()

# Main class to deal with the opperations of the ticket system
class Main:
    @staticmethod
    def run():
        # Create a list of ticket instances
        tickets = [
            Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working"),
            Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars"),
            Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password change")
        ]

        # Deal with password change requests
        for ticket in tickets:
            ticket.resolve_password_change()

        # Display statistics of the tickets
        total, resolved, open_tickets = Ticket.ticket_stats(tickets)
        print("Ticket Statistics\n")
        print("Total Tickets:", total)
        print("Resolved Tickets:", resolved)
        print("Open Tickets:", open_tickets)
        print()

        # Print information about the tickets
        print("Printing Tickets:")
        for ticket in tickets:
            ticket.display_ticket()

        # Responds to some of the tickets we have got
        tickets[0].respond("The monitor has been replaced.")
        tickets[1].respond("Not Yet Provided")

        # Reopen a ticket
        tickets[1].reopen()

        # Display the ticket statistics after being updated
        total, resolved, open_tickets = Ticket.ticket_stats(tickets)
        print("Updated Ticket Statistics\n")
        print("Total Tickets:", total)
        print("Resolved Tickets:", resolved)
        print("Open Tickets:", open_tickets)
        print()

        # Print information about the tickets after being updated
        print("Printing Tickets:")
        for ticket in tickets:
            ticket.display_ticket()

# Simply runs the main program by using the Main object's run method
Main.run()
