import pickle
flight = {'flight': 'LH237', 'airline' : 'Indigo', 'Capacity' : 180, 'price' : 2500, 'source' : 'Delhi', 'destination' :'Hyderabad'}
file_name = 'flight.dat'

print('Before write:', flight)
with open(file_name, 'wb') as writer:
    pickle.dump(flight, writer)
    print("saved the flight in the file")

with open(file_name, 'rb') as reader:
    flight_from_file = pickle.load(reader)
    print('After read:', flight)