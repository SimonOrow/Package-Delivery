from WGUPSDistances import *


class HelperFunctions:

    @staticmethod
    def calculate_time_to_arrive(distance_miles, speed_mph):
        return distance_miles/speed_mph

    @staticmethod
    def get_address_id(address_list, address_to_find):
        for address in address_list:
            if address_to_find in address:
                return address_list.index(address)
        raise Exception("Could not find the address")

    @staticmethod
    def find_closest_next_package(dijkstra_result, truck, packages):
        # Convert the Dijkstra result to a map, keeping only the package ids in our truck.
        current_data = {}
        addresses = Distances.get_addresses()
        for package_id in truck.packages:
            package_address = packages.retrieve(package_id).address
            package_address_id = HelperFunctions.get_address_id(addresses, package_address)


            current_data[package_id] = dijkstra_result[package_address_id]



        # current_data = {}
        # for key, value in enumerate(dijkstra_result):
        #     if key in truck.packages:
        #         current_data[key] = value
        #
        # print(truck.packages)
        print("D Result: " + str(dijkstra_result))
        print("Data: " + str(current_data))
        shortest_path_product_id = min(current_data, key=current_data.get)
        print(f"The next package is {shortest_path_product_id} with distance {current_data[shortest_path_product_id]}")


        return shortest_path_product_id, current_data[shortest_path_product_id], package_address