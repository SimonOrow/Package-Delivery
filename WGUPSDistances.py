import csv


class Distances:
    # Opens CSV file and loads necessary data, skipping over non-data columns.
    @staticmethod
    def get_distances_data():
        data = list(csv.reader(open("csv_files/WGUPSDistanceTable.csv")))  # Open csv file
        distance_data = []  # Initialize empty array
        count = 0
        for row in data:
            # Do not include the first 8 rows. We must capture row 9 and beyond as that's where the data points are.
            if count < 8:
                count = count + 1
                continue
            # Only append the 3rd column and beyond.
            # We don't want the first two columns (addresses).
            distance_data.append(row[2:])
        return distance_data

    @staticmethod
    def get_addresses():
        data = list(csv.reader(open("csv_files/WGUPSDistanceTable.csv")))  # Open csv file
        addresses = []
        count = 0
        for row in data:
            # Do not include the first 8 rows. We must capture row 9 and beyond as that's where the data points are.
            if count < 8:
                count = count + 1
                continue
            # Only append the 3rd column and beyond.
            # We don't want the first two columns (addresses).
            addresses.append(row[0])
        return addresses
