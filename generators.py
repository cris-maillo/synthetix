from faker import Faker
import random
from models import User, Artist, Event, Venue, Promoter, Ticket, Sale, TicketValidation

fake = Faker()

def generate_users(n):
    users = []
    for i in range(n):
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        interested_event_ids = [random.randint(1, 100) for _ in range(random.randint(1, 5))]
        users.append(User(user_id=i+1, username=username, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, interested_event_ids=interested_event_ids))
    return users

def generate_artists(n):
    artists = []
    for i in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        artist_name = fake.name()
        biography = fake.text(max_nb_chars=100)
        country = fake.country()
        artists.append(Artist(artist_id=i+1, first_name=first_name, last_name=last_name, artist_name=artist_name, biography=biography, country=country))
    return artists

def generate_events(n, users, artists, venues, promoters):
    events = []
    for i in range(n):
        event_name = fake.catch_phrase()
        genre = random.choice(["House", "Techno", "Electro", "Trance"])
        venue = random.choice(venues)
        description = f"A night of {genre} featuring {random.choice(artists).artist_name} at {venue.venue_name}"
        owner = random.choice(users)
        promoter_id = random.choice(promoters)
        admin_ids = list({owner.user_id} | {random.choice(users).user_id for _ in range(random.randint(1, 3))})
        artist_ids = [random.choice(artists).artist_id for _ in range(random.randint(1, 4))]
        start_date = fake.date_time_between(start_date='now', end_date='+90d')
        end_date = fake.date_time_between(start_date=start_date, end_date='+90d')
        total_tickets = random.randint(50, 500)
        tickets_sold = random.randint(0, total_tickets)
        events.append(Event(
            event_id=i+1,
            event_name=event_name,
            description=description,
            promoter_id=promoter_id,
            owner_id=owner.user_id,
            event_admin_ids=admin_ids,
            artist_ids=artist_ids,
            start_date=start_date,
            end_date=end_date,
            venue_id=venue.venue_id,
            total_tickets=total_tickets,
            tickets_sold=tickets_sold
        ))
    return events

def generate_venues(n):
    venues = []
    for i in range(n):
        venue_name = fake.company()
        venue_description = fake.text(max_nb_chars=150)
        address = fake.address()
        city = fake.city()
        country = fake.country()
        capacity = random.randint(100, 5000)
        venues.append(Venue(venue_id=i+1, venue_name=venue_name, venue_description=venue_description, address=address, city=city, country=country, capacity=capacity))
    return venues

def generate_promoters(n):
    promoters = []
    for i in range(n):
        promoter_name = fake.company()
        promoter_email = fake.email()
        promoter_phone_number = fake.phone_number()
        promoters.append(Promoter(promoter_id=i+1, promoter_name=promoter_name, promoter_email=promoter_email, promoter_phone_number=promoter_phone_number))
    return promoters

def generate_tickets(events, users):
    tickets = []
    ticket_types = ['General', 'VIP', 'Premium', 'Early Bird']
    for event in events:
        num_tickets = random.randint(10, event.total_tickets)
        for i in range(num_tickets):
            ticket_type = random.choice(ticket_types)
            owner = random.choice(users)
            tickets.append(Ticket(
                ticket_id=len(tickets)+1,
                event_id=event.event_id,
                owner_user_id=owner.user_id,
                ticket_type=ticket_type
            ))
    return tickets

def generate_sales(tickets, users):
    sales = []
    for ticket in tickets:
        buyer = random.choice(users)
        sale_date = fake.date_time_between(start_date='-30d', end_date='now')
        price = random.randint(25, 200)
        sales.append(Sale(
            sale_id=len(sales)+1,
            ticket_id=ticket.ticket_id,
            buyer_user_id=buyer.user_id,
            sale_date=sale_date,
            price=price
        ))
    return sales

def generate_ticket_validations(tickets, users):
    validations = []
    for ticket in tickets:
        if random.random() < 0.7:  # 70% chance of validation
            validator = random.choice(users)
            validation_time = fake.date_time_between(start_date='-7d', end_date='now')
            validations.append(TicketValidation(
                validation_id=len(validations)+1,
                ticket_id=ticket.ticket_id,
                validator_user_id=validator.user_id,
                validation_time=validation_time
            ))
    return validations