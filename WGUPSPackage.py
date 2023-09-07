import csv
import datetime


class WGUPSPackage:
    def __init__(self, package_id, address, city, state, zip, delivery_deadline, weight, notes):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.truck_id = 0
        self.time_delivered = datetime.timedelta()

    @staticmethod
    def get_all_packages():
        data = list(csv.reader(open("csv_files/WGUPSPackageFile.csv")))  # Open csv file
        packages = []  # Initialize empty array
        count = 0
        for row in data:
            # Do not include the first 8 rows. We must capture row 9 and beyond as that's where the data points are.
            if count < 8:
                count = count + 1
                continue

            current_package = WGUPSPackage(package_id=row[0], address=row[1], city=row[2], state=row[3], zip=row[4], delivery_deadline=row[5], weight=row[6], notes=row[7])
            packages.append(current_package)
        return packages
