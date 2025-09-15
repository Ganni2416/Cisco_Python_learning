import json
flight = {'flight': 'LH237', 'airline' : 'Indigo', 'Capacity' : 180, 'price' : 2500, 'source' : 'Delhi', 'destination' :'Hyderabad'}
file_name = 'flight.json'

print('Before write:', flight)
with open(file_name, 'w', encoding='utf-8') as writer:
    json.dump(flight, writer)
    print("saved the flight in the file")

with open(file_name, 'r', encoding='utf-8') as reader:
    flight_from_file = json.load(reader)
    print('After read:', flight)