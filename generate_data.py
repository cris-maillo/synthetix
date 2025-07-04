class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Artist:
    def __init__(self, artist_id, name, biography, country):
        self.artist_id = artist_id
        self.name = name
        self.biography = biography
        self.country = country

class Event:
    def __init__(self, event_id, event_name, description, owner_id, event_admin_ids, artist_ids, date, location, total_tickets, tickets_sold):
        self.event_id = event_id
        self.event_name = event_name
        self.description = description
        self.owner_id = owner_id
        self.event_admin_ids = event_admin_ids
        self.artist_ids = artist_ids
        self.date = date
        self.location = location
        self.total_tickets = total_tickets
        self.tickets_sold = tickets_sold

class Ticket:
    def __init__(self, ticket_id, event_id, owner_user_id, status):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.owner_user_id = owner_user_id
        self.status = status

class Sale:
    def __init__(self, sale_id, ticket_id, buyer_user_id, sale_date, price):
        self.sale_id = sale_id
        self.ticket_id = ticket_id
        self.buyer_user_id = buyer_user_id
        self.sale_date = sale_date
        self.price = price

class TicketValidation:
    def __init__(self, validation_id, ticket_id, validator_user_id, validation_time, location):
        self.validation_id = validation_id
        self.ticket_id = ticket_id
        self.validator_user_id = validator_user_id
        self.validation_time = validation_time
        self.location = location