import csv
from hashmap import HashMap

# Read package data from packages csv
with open('package_data/packages.csv') as package_csv:
    package_data_csv = csv.reader(package_csv, delimiter=',')

    # Create instance of hash map
    hash_map = HashMap()

    # Create lists for each delivery truck
    truck1 = []
    truck2 = []
    truck3 = []

    # Read values from the csv file and insert key and value pairs for each package into
    # the hash table. Time complexity = O(n)
    for row in package_data_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        start = ''
        address_location = ''
        package_status = 'At hub'

        # Create packages for each package in the csv file.
        package = [id, address_location, address, city, state, zip, delivery, size,
                   note, start, package_status]

        # Add package with incorrect details to the final delivery
        if 'Wrong address listed' in package[8]:
            truck3.append(package)

        # Add packages to first delivery. Add all packages that have time constraints which are not just that the
        # package must be delivered by the end of the day to the first truck as these are priority mailing.
        # Any packages that have 'Must' in the notes need to be delivered together so this will exclude those and
        # only add packages that have 'None' in the notes. Add packages while truck1 list is less than 16.
        if package[6] != 'EOD':
            if 'Must' in package[8] or 'None' in package[8]:
                truck1.append(package)

        # Add packages to the second truck delivery. Some packages are required to be on truck 2 so this will filter
        # on notes that say 'can only be' as these must be in truck 2. Additionally, any packages that say 'delayed'
        # in the notes will be added to this delivery.
        if 'Can only be' in package[8] or 'Delayed' in package[8]:
            truck2.append(package)

        # Add remaining packages to the third delivery. Check to make sure it's not in the first truck, not in the
        # second truck, and that it has not yet been added to the third truck. Add more trucks to the 2nd truck
        # if there is still room (i.e. length of delivery 2 is less than 16 packages).
        if package not in truck1 and package not in truck2 and package not in truck3:
            truck2.append(package) if len(truck2) < len(truck3) else truck3.append(package)

        # Insert values into the hash table that was created.
        hash_map.insert(id, package)

    # Get packages on each delivery. Time complexity = O(1)
    def get_delivery1():
        return truck1

    def get_delivery2():
        return truck2

    def get_delivery3():
        return truck3

    # Get a list of all packages. Time complexity = O(1)
    def get_hash_map():
        return hash_map