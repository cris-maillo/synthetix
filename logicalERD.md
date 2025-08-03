---
config:
  theme: mc
  look: classic
  layout: elk
---
classDiagram
%% do i limit each class to its own remit? or start creating associations to other classes
  class Event {
    id
    name
    description
    startDateTime
    endDateTime
    %% do ticket per ticket range get defined here
  }
  class Artist {
    id
    artistName
    firstName
    lastName
    bio
    socialMediaLink 
    %% more than one attribute
    %% what about account management
  }
  class Promoter {
    id
    name
    description
  }
  class Customer {
    id
    %% both email and id? do i put id at this stage
    username
    email
    password
    firstName
    lastName
  }
  class Sale {
    id
    saleDateTime
    price
  }
  class Ticket {
    id
    status
  }
  class Venue {
    id
    name
    address
    city
    country
    description
  }
  class VenueManager {
  }
  Event "*" -- "1...*" Artist : hosts
  Promoter "*" -- "*" Event : manages
  Customer "1" -- "*" Sale : places
  Sale "1" -- "1...*" Ticket : contains
  Customer "1" -- "*" Ticket : owns
  Event "1" -- "1...*" Ticket : issues
  Venue "1" -- "1...*" VenueManager : managed by
  Venue "1" -- "*" Event : hosts
%%   what about user following an artist, or a venue, or being interested in an event