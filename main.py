# Simon Orow 011196580
import datetime

from Dijkstra import *
from HelperFunctions import *
from WGUPSPackage import *
from WGUPSDistances import *
from Truck import *
from HashTable import *
from Settings import *

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


def deliverForTruck(truck):
    print("Truck " + str(truck.id) + " is now en route.")
    while len(truck.packages) != 0:

        if Settings.debug:
            print("Current: " + str(truck.packages))

        truck_current_address_id = HelperFunctions.get_address_id(adddresses,truck.current_address)
        dijkstra_result = Dijkstra.dijkstra_bidirectional_matrix(distances, truck_current_address_id)
        package_delivered_id, distance, address = HelperFunctions.find_closest_next_package(dijkstra_result, truck, packagesHashTable)

        truck.total_miles += distance
        truck.time_elapsed += datetime.timedelta(hours=HelperFunctions.calculate_time_to_arrive(distance, truck.speed_mph))

        truck.packages.remove(package_delivered_id)
        truck.current_address = address

        if Settings.debug:
            print("We are now at " + address)

        current_package = packagesHashTable.retrieve(package_delivered_id)
        # Time package was delivered is equal to time truck left plus the time elapsed since leaving.
        current_package.time_delivered = truck.departure_time + truck.time_elapsed

        print("Delivered package " + str(current_package.id) + " at " + str(current_package.time_delivered))
    print()


# For all packages, add them to the hash table.
for package in package_data:
    packagesHashTable.add(package.id, package)


# Establish trucks

truck1 = Truck(truck_id=1)
truck1.departure_time = datetime.timedelta(hours=8, minutes=0)
for package_id in truck_1_packages:
    truck1.packages.add(package_id)
    truck1.packages_on_board_count = len(truck1.packages)

    package = packagesHashTable.retrieve(package_id)
    package.truck_id = 1
    package.corresponding_truck_departure_time = truck1.departure_time

truck2 = Truck(truck_id=2)
truck2.departure_time = datetime.timedelta(hours=9, minutes=5)
for package_id in truck_2_packages:
    truck2.packages.add(package_id)
    truck2.packages_on_board_count = len(truck2.packages)

    package = packagesHashTable.retrieve(package_id)
    package.truck_id = 2
    package.corresponding_truck_departure_time = truck2.departure_time

truck3 = Truck(truck_id=3)
for package_id in truck_3_packages:
    truck3.packages.add(package_id)
    truck3.packages_on_board_count = len(truck3.packages)
    package = packagesHashTable.retrieve(package_id)
    package.truck_id = 3

    package = packagesHashTable.retrieve(package_id)
    package.truck_id = 3
    package.corresponding_truck_departure_time = truck3.departure_time


# Perform the deliveries for trucks 1 and 2
deliverForTruck(truck1)
deliverForTruck(truck2)

truck1_time = truck1.departure_time + truck1.time_elapsed
truck2_time = truck2.departure_time + truck2.time_elapsed


truckToContinue = None

# Decide which truck finished first and should go back to take truck 3.
# (Truck 1 finishes first)
if truck1_time < truck2_time:
    if Settings.debug:
        print("Truck 1 finished first and is now returning back to the hub.")
    truckToContinue = truck1
else:
    print("Truck 2 finished first and is now returning back to the hub.")
    truckToContinue = truck2

# Get all distances starting from the truck's last location.
truck_current_address_id = HelperFunctions.get_address_id(adddresses, truckToContinue.current_address)
dijkstra_result = Dijkstra.dijkstra_bidirectional_matrix(distances, truck_current_address_id)
distance_to_hub = dijkstra_result[0]

# Travel back to the hub.
truckToContinue.total_miles += distance_to_hub
truckToContinue.time_elapsed += datetime.timedelta(hours=HelperFunctions.calculate_time_to_arrive(distance_to_hub, truckToContinue.speed_mph))


# Driver gets on truck 3 at the time that they arrived back to the hub.
truck3.departure_time = (truckToContinue.departure_time + truckToContinue.time_elapsed)

# Make the driver wait until 10:20 AM when correct package ID is provided for package #9
if truck3.departure_time < datetime.timedelta(hours=10, minutes=20):
    truck3.departure_time = datetime.timedelta(hours=10, minutes=20)

# Update the address and start the route.
package9 = packagesHashTable.retrieve(9)
package9.address = "410 S State St"
package9.zip = "84111"


deliverForTruck(truck3)


while True:
    print("Welcome to the WGUPS tool!")
    time = input("Enter a time that's in 24 hour format and in the hh:mm format (ex: 10:20): ")
    time = time.split(":")
    hour = time[0]
    minutes = time[1]
    status_time = datetime.timedelta(hours=int(hour), minutes=int(minutes))
    package_to_find = input("Enter a package id or leave blank for all packages: ")
    packages_ids = []
    if package_to_find == "":
        packages_ids = truck_1_packages + truck_2_packages + truck_3_packages
    else:
        packages_ids = [int(package_to_find)]

    HelperFunctions.print_package_with_status(packages_ids, packagesHashTable, status_time)


