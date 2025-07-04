import csv

def export_to_csv(data, num_examples=5):
    """Export data to CSV files with specified number of examples"""
    
    # Create example_data folder if it doesn't exist
    import os
    os.makedirs('example_data', exist_ok=True)
    
    # Users CSV
    with open('example_data/users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'interested_event_ids'])
        for user in data['users'][:num_examples]:
            writer.writerow([user.user_id, user.username, user.first_name, user.last_name, user.email, user.phone_number, user.interested_event_ids])
    
    # Artists CSV
    with open('example_data/artists.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['artist_id', 'first_name', 'last_name', 'artist_name', 'biography', 'country'])
        for artist in data['artists'][:num_examples]:
            writer.writerow([artist.artist_id, artist.first_name, artist.last_name, artist.artist_name, artist.biography, artist.country])
    
    # Venues CSV
    with open('example_data/venues.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['venue_id', 'venue_name', 'venue_description', 'address', 'city', 'country', 'capacity'])
        for venue in data['venues'][:num_examples]:
            writer.writerow([venue.venue_id, venue.venue_name, venue.venue_description, venue.address, venue.city, venue.country, venue.capacity])
    
    # Promoters CSV
    with open('example_data/promoters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['promoter_id', 'promoter_name', 'promoter_email', 'promoter_phone_number'])
        for promoter in data['promoters'][:num_examples]:
            writer.writerow([promoter.promoter_id, promoter.promoter_name, promoter.promoter_email, promoter.promoter_phone_number])
    
    # Events CSV
    with open('example_data/events.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['event_id', 'event_name', 'description', 'promoter_id', 'owner_id', 'event_admin_ids', 'artist_ids', 'start_date', 'end_date', 'venue_id', 'total_tickets', 'tickets_sold'])
        for event in data['events'][:num_examples]:
            writer.writerow([event.event_id, event.event_name, event.description, event.promoter_id, event.owner_id, event.event_admin_ids, event.artist_ids, event.start_date, event.end_date, event.venue_id, event.total_tickets, event.tickets_sold])
    
    # Tickets CSV
    with open('example_data/tickets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ticket_id', 'event_id', 'owner_user_id', 'ticket_type'])
        for ticket in data['tickets'][:num_examples]:
            writer.writerow([ticket.ticket_id, ticket.event_id, ticket.owner_user_id, ticket.ticket_type])
    
    # Sales CSV
    with open('example_data/sales.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['sale_id', 'ticket_id', 'buyer_user_id', 'sale_date', 'price'])
        for sale in data['sales'][:num_examples]:
            writer.writerow([sale.sale_id, sale.ticket_id, sale.buyer_user_id, sale.sale_date, sale.price])
    
    # Validations CSV
    with open('example_data/validations.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['validation_id', 'ticket_id', 'validator_user_id', 'validation_time'])
        for validation in data['validations'][:num_examples]:
            writer.writerow([validation.validation_id, validation.ticket_id, validation.validator_user_id, validation.validation_time])
    
    print(f"\nCSV files created in example_data/ folder with {num_examples} examples each:")
    print("- example_data/users.csv")
    print("- example_data/artists.csv") 
    print("- example_data/venues.csv")
    print("- example_data/promoters.csv")
    print("- example_data/events.csv")
    print("- example_data/tickets.csv")
    print("- example_data/sales.csv")
    print("- example_data/validations.csv")