from generators import generate_venues, generate_promoters, generate_users, generate_artists, generate_events, generate_tickets, generate_sales, generate_ticket_validations
from export import export_to_csv

def main():
    print("Generating synthetic ticketing platform data...")
    
    # Generate data in dependency order
    print("1. Generating venues...")
    venues = generate_venues(2)
    
    print("2. Generating promoters...")
    promoters = generate_promoters(2)
    
    print("3. Generating users...")
    users = generate_users(2)
    
    print("4. Generating artists...")
    artists = generate_artists(2)
    
    print("5. Generating events...")
    events = generate_events(2, users, artists, venues, promoters)
    
    print("6. Generating tickets...")
    tickets = generate_tickets(events, users)
    
    print("7. Generating sales...")
    sales = generate_sales(tickets, users)
    
    print("8. Generating ticket validations...")
    validations = generate_ticket_validations(tickets, users)
    
    print(f"\nData generation complete!")
    print(f"- {len(users)} users")
    print(f"- {len(artists)} artists")  
    print(f"- {len(venues)} venues")
    print(f"- {len(promoters)} promoters")
    print(f"- {len(events)} events")
    print(f"- {len(tickets)} tickets")
    print(f"- {len(sales)} sales")
    print(f"- {len(validations)} validations")
    
    data = {
        'users': users,
        'artists': artists,
        'venues': venues,
        'promoters': promoters,
        'events': events,
        'tickets': tickets,
        'sales': sales,
        'validations': validations
    }
    
    # Export to CSV files
    export_to_csv(data, 5)

if __name__ == "__main__":
    main() 