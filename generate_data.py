class User:
    def __init__(self, user_id, username, first_name, last_name, email, phone_number, interested_event_ids):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.interested_event_ids = interested_event_ids

class Artist:
    def __init__(self, artist_id, first_name, last_name, artist_name, biography, country):
        self.artist_id = artist_id
        self.first_name = first_name
        self.last_name = last_name
        self.artist_name = artist_name
        self.biography = biography
        self.country = country

class Event:
    def __init__(self, event_id, event_name, description, promoter_id, owner_id, event_admin_ids, artist_ids, start_date, end_date, venue_id, total_tickets, tickets_sold):
        self.event_id = event_id
        self.event_name = event_name
        self.description = description
        self.promoter_id = promoter_id  
        self.owner_id = owner_id
        self.event_admin_ids = event_admin_ids
        self.artist_ids = artist_ids
        self.start_date = start_date
        self.end_date = end_date
        self.venue_id = venue_id
        self.total_tickets = total_tickets
        self.tickets_sold = tickets_sold

class Venue:
    def __init__(self, venue_id, venue_name, venue_description, address, city, country, capacity):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_description = venue_description
        self.address = address
        self.city = city
        self.country = country
        self.capacity = capacity

class Promoter:
    def __init__(self, promoter_id, promoter_name, promoter_email, promoter_phone_number):
        self.promoter_id = promoter_id
        self.promoter_name = promoter_name
        self.promoter_email = promoter_email
        self.promoter_phone_number = promoter_phone_number

class Ticket:
    def __init__(self, ticket_id, event_id, owner_user_id):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.owner_user_id = owner_user_id

class Sale:
    def __init__(self, sale_id, ticket_id, buyer_user_id, sale_date, price):
        self.sale_id = sale_id
        self.ticket_id = ticket_id
        self.buyer_user_id = buyer_user_id
        self.sale_date = sale_date
        self.price = price

class TicketValidation:
    def __init__(self, validation_id, ticket_id, validator_user_id, validation_time):
        self.validation_id = validation_id
        self.ticket_id = ticket_id
        self.validator_user_id = validator_user_id
        self.validation_time = validation_time
        