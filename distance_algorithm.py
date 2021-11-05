import datetime
import csv

# Read distances files; split between distances and address names.
with open('package_data/distances.csv') as location_distance_csv:
    distance_csv = list(csv.reader(location_distance_csv, delimiter=','))
with open('package_data/addresses.csv') as location_name_csv:
    address_name_csv = list(csv.reader(location_name_csv, delimiter=','))

# Function to get an address. Time complexity = O(1)
def get_address():
    return address_name_csv

# Function to get the total distance from the distance csv file based on row and column values.
# Time complexity = O(1)
def get_total_distance(row, col, total):
    dist = distance_csv[row][col]
    if dist == '':
        dist = distance_csv[col][row]
    return total + float(dist)

# Function to return current distance from row and column values.
# Time complexity = O(1)
def current_distance(row, col):
    dist = distance_csv[row][col]
    if dist == '':
        dist = distance_csv[col][row]
    return float(dist)

# Function to calculate total distance for a delivery truck.
# Time complexity = O(1)
def get_truck_time(distance, package_list):
    time = distance / 18
    time_to_min_conversion = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(time * 60, 60))
    truck_time = time_to_min_conversion + ':00'
    package_list.append(truck_time)
    total_time = datetime.timedelta()
    for i in package_list:
        (hrs, mins, secs) = i.split(':')
        total_time += datetime.timedelta(hours=int(hrs),minutes=int(mins), seconds=int(secs))
    return total_time

# Create lists of sorted trucks as well as their associated indices. Make first index 0 for each list
# as each truck starts at location 0.
truck1 = []
truck1_index = []
truck1_index.insert(0, '0')
truck2 = []
truck2_index = []
truck2_index.insert(0, '0')
truck3 = []
truck3_index = []
truck3_index.insert(0, '0')

# This is the core algorithm used to find the next best location based upon the truck's current location.
# It implement's a greedy approach and recursion in order to do so. The algo has 3 parameters:
# 1. List of packages
# 2. Truck
# 3. Truck's current location

# The first for loop is used to find the shortest distance to the next location, given the current location.
# The loop will run until a minimum value is found.

# The second for loop checks to see which truck the package is associated with. Values are appended to the associated
# truck list. The current package is then 'delivered' and removed from the list and the current location will then move
# to the next closest location based on the first for loop. A recursive call is made for the next location and the
# shorter list; recursion will continue until the base case is reached which is an empty list. This will end the algo.

# As there are two for loops, space/time complexity is O(n^2).

def greedy_algorithm(package_list, truck_num, current_location):
    if len(package_list) == 0:
        return package_list

    min = 15
    location = 0

    for package in package_list:
        value = int(package[1])
        if current_distance(current_location, value) <= min:
            min = current_distance(
                current_location, value)
            location = value

    for package in package_list:
        if current_distance(current_location, int(package[1])) == min:
            if truck_num == 1:
                truck1.append(package)
                truck1_index.append(package[1])
                package_list.pop(package_list.index(package))
                current_location = location
                greedy_algorithm(package_list, 1, current_location)
            elif truck_num == 2:
                truck2.append(package)
                truck2_index.append(package[1])
                package_list.pop(package_list.index(package))
                current_location = location
                greedy_algorithm(package_list, 2, current_location)
            elif truck_num == 3:
                truck3.append(package)
                truck3_index.append(package[1])
                package_list.pop(package_list.index(package))
                current_location = location
                greedy_algorithm(package_list, 3, current_location)

# Functions to return values for each truck.
# Time complexity = O(1)
def delivery1_index():
    return truck1_index

def delivery1_list():
    return truck1

def delivery2_index():
    return truck2_index

def delivery2_list():
    return truck2

def delivery3_index():
    return truck3_index

def delivery3_list():
    return truck3