import datetime


class Truck:
    def __init__(self, truck_id):
        self.id = truck_id
        self.packages = set()  # Set to ensure we do not have duplicates.
        self.speed_mph = 18
        self.current_address = "4001 South 700 East"
        self.time_elapsed = datetime.timedelta()
        self.departure_time = datetime.timedelta()
        self.total_miles = 0
