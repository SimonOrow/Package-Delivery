# Simon Orow 011196580

from Dijkstra import *
from HelperFunctions import *
from WGUPSPackage import *
from WGUPSDistances import *
from Truck import *
from HashTable import *
# Truck 1
# Priority packages (Packages marked with a time rather than EOD) and are available.
# Added 19 which is marked EOD, but must be delivered with 14 and 15.
# Depart at 8:00
truck_1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

# Truck 2
# Add packages required for truck 2 or those that arrive at 9:05am.
# Depart 9:05am.
truck_2_packages = [3, 6, 17, 18, 25, 26, 27, 28, 32, 36, 38]

# Truck 3
# Will contain package with wrong address and all remaining packages
truck_3_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 21, 22, 23, 24, 35, 39, 33]

# OVERALL STRATEGY:
# Load Truck 1 with packages that have delivery deadlines and include 19, so everything can make it on time.
# Load Truck 2 with only items that must be in Truck 2 and those arriving at 9:05am.
# Load Truck 3 with everything else.

packagesHashTable = HashTable(40)
package_data = WGUPSPackage.get_all_packages()

distances = Distances.get_distances_data()
adddresses = Distances.get_addresses()

# For all packages, add them to the hash table.
for package in package_data:
    packagesHashTable.add(package.id, package)

truck1 = Truck(truck_id=1)
for package_id in truck_1_packages:
    truck1.packages.add(package_id)
    truck1.packages_on_board_count = len(truck1.packages)
    truck1.departure_time = datetime.timedelta(hours=8, minutes=0)

truck2 = Truck(truck_id=2)
for package_id in truck_2_packages:
    truck2.packages.add(package_id)
    truck2.packages_on_board_count = len(truck2.packages)

truck3 = Truck(truck_id=3)
for package_id in truck_3_packages:
    truck3.packages.add(package_id)
    truck3.packages_on_board_count = len(truck3.packages)






def deliverForTruck(truck):

    while len(truck.packages) != 0:

        print("Current: " + str(truck.packages))

        truck_current_address_id = HelperFunctions.get_address_id(adddresses,truck.current_address)
        dijkstra_result = Dijkstra.dijkstra_bidirectional_matrix(distances, truck_current_address_id)
        package_delivered_id, distance, address = HelperFunctions.find_closest_next_package(dijkstra_result, truck, packagesHashTable)

        truck.total_miles += distance
        truck.time_elapsed += datetime.timedelta(hours=HelperFunctions.calculate_time_to_arrive(distance, truck.speed_mph))

        truck.packages.remove(package_delivered_id)
        truck.current_address = address

        print("We are now at " + address)

        #product = HashTable.retrieve(package_delivered_id)



deliverForTruck(truck1)

print()
print(truck1.time_elapsed)
print(truck1.total_miles)