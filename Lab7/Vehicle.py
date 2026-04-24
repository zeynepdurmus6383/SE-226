class Vehicle:
    def __init__(self, id, model, year):
        self.vid = str(id)
        self.model = str(model)
        self.year = int(year)

    def __str__(self):
        return "VID: " + self.vid + ", Model: " + self.model + ", Year: " + str(self.year)

    def  __eq__(self, other):
        if self.vid == other.vid:
            return True
        else:
            return False

    def is_new(self, n):
        if self.year >= 2026-n:
            return True
        else:
            return False

class Car(Vehicle):
    def __init__(self,id, model, year, fuel, door):
        super().__init__(id, model, year)
        self.fuel_type = str(fuel)
        self.doors = int(door)

    def __str__(self):
        return "[Car]         " + super().__str__() + " , Fuel: " + self.fuel_type + " , Doors: "  + str(self.doors)

class Truck(Vehicle):
    def __init__(self, id, model, year, load, axles ):
        super().__init__(id, model, year)
        self.max_load = int(load)
        self.axles = int(axles)

    def __str__(self):
        return "[Truck]       " + super().__str__() + " , Max Load: " + str(self.max_load) + " , Axles: "  + str(self.axles)

class Motorcycle(Vehicle):
    def __init__(self, id, model, year, cc , type):
        super().__init__(id, model, year)
        self.engine_cc = int(cc)
        self.type = str(type)

    def __str__(self):
        return "[Motorcycle]  " + super().__str__() + " , Engine(cc): " + str(self.engine_cc) + " , Type: " + self.type

def save_fleet_to_file(vehicles, filename):
    file = open(filename , "w")
    for v in vehicles:
        if type(v) == Car:
            file.write("Car" + ", " + v.vid + ", " + v.model + ", " + str(v.year) + ", " + v.fuel_type + ", " + str(v.doors) + "\n")
        elif type(v) == Truck:
            file.write("Truck"+ ", " + v.vid + ", " + v.model + ", " + str(v.year) + ", " + str(v.max_load) + ", " + str(v.axles) + "\n")
        if type(v) == Motorcycle:
            file.write("motorcycle" + ", " + v.vid + ", " + v.model + ", " + str(v.year) + ", " + str(v.engine_cc) + ", " + v.type + "\n")


def load_fleet_from_file(filename):
    file = open(filename).readlines()
    vehicles = []
    for line in file:
        parts = line.split(",")
        if parts[0].strip() == "Car":
            vehicles.append(Car(parts[1],parts[2],parts[3],parts[4],parts[5]))
        elif parts[0].strip() == "Truck":
            vehicles.append(Truck(parts[1], parts[2], parts[3], parts[4], parts[5]))
        elif parts[0].strip() == "Motorcycle":
            vehicles.append(Motorcycle(parts[1], parts[2], parts[3], parts[4], parts[5]))
    return vehicles



a = Vehicle(12 , 12, 1975)
print(a)
c1 = Car("V001" ,"Tesla Model 3",2023, "Electric", 4)
t1 = Truck("T101","Volvo FH16",2019, 25000, 6)
m1 = Motorcycle("M301","Yamaha R1",2024, 998, "Sport")
c2 = Car("V002", "Toyota Corolla",2018, "Petrol", 4)
t2 = Truck("T102", "Mercedes Actros",2021, 18000, 4)
m2 = Motorcycle("M302","Harley Davidson",2015, 1200, "Cruiser")
print(c1)
print(t1)
print(m1)
save_fleet_to_file([c1,t1,m1,c2,t2,m2],"fleet.txt")
vehicles = load_fleet_from_file("fleet.txt")

print("--- All Vehicles ---")
for v in vehicles:
    print(v)
print("\n")

print("--- Recent Vehicles (Last 4 Years) ---")
for v in vehicles:
    if v.is_new(4):
        print(v)
print("\n")


print("--- Electric Cars Only ---")
for v in vehicles:
    if type(v) == Car:
        if v.fuel_type == "Electric":
            print(v)
print("\n")
