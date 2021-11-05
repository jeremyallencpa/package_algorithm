from reader import *
from packages import *
from menu import *
import datetime

# This displays program stats and the main menu.
def menu():

    print('*****************************************')
    print('WGUPS Routing Program for C950')
    print('*****************************************\n')
    print('Program Menu')
    print('*****************************************')
    print("Select an option below, or press 0 to quit:")
    print("1 = Show info for specific package")
    print("2 = Show all packages at a specific time")
    print("3 = Print total program stats")
    return ''

# Function that returns a list of all packages along with their status at a given time.
# User input is a specific time, and the output is a list of all packages along with their
# status at that particular time.
# Time complexity = O(n^2)
def package_list_with_status():
    try:
        user_input_time = input('Enter a search time in the format of (HH:MM:SS): ')
        (hrs, mins, secs) = user_input_time.split(':')
        input_time_conversion = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

        # Loop through packages in the hashmap and extract all in transit start times, and delivered times.
        # These will then be compared to the user input time to determine the package status at that time.
        for package in range(1, 41):
            try:
                in_transit_start = get_hash_map().get_hash_value(str(package))[9]
                (hrs, mins, secs) = in_transit_start.split(':')
                in_transit_time_conversion = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                delivered_time = get_hash_map().get_hash_value(str(package))[10]
                (hrs, mins, secs) = delivered_time.split(':')
                delivered_time_conversion = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                package_id = get_hash_map().get_hash_value(str(package))[0]
            except ValueError:
                pass

            # Check in transit time against the input time. If the input time is greater than the in transit time,
            # then this package is still at the hub.
            if in_transit_time_conversion >= input_time_conversion:
                status = get_hash_map().get_hash_value(str(package))[10] = 'At Hub'
                in_transit = get_hash_map().get_hash_value(str(package))[9] = 'Leaves at ' + in_transit_start

                # Print package information
                print(
                    f'**********\n'
                    f'Package ID: ' + package_id,
                    '\n'
                    f'Status: ' + status,
                    '\n'
                    f'Leaves at: ' + in_transit
                )

            # Check in transit time against the input time. If the input time is less than the in transit time,
            # and less than the delivery time, then the package is in transit.
            elif in_transit_time_conversion <= input_time_conversion:
                if input_time_conversion < delivered_time_conversion:
                    status = get_hash_map().get_hash_value(str(package))[10] = 'In transit'
                    in_transit = get_hash_map().get_hash_value(str(package))[9] = 'Left at ' + in_transit_start
                    print(
                      f'**********\n'
                      f'Package ID: ' + package_id,
                      '\n'
                      f'Status: ' + status,
                      '\n'  
                      f'Left at: ' + in_transit
                    )

                # Print package info for packages that have been delivered.
                else:
                    status = get_hash_map().get_hash_value(str(package))[10] = 'Delivered at ' + delivered_time
                    in_transit = get_hash_map().get_hash_value(str(package))[9] = 'Left at ' + in_transit_start

                    # Print package's current info
                    print(
                      f'**********\n'
                      f'Package ID: ' + package_id,
                      '\n'
                      f'Left at: ' + in_transit,
                      '\n'
                      f'Status: ' + status,
                    )
    except IndexError:
        print(IndexError)
        exit()
    except ValueError:
        print('Invalid entry!')
        exit()

# Function to get package details for a specific package. Input is package ID.
# Time complexity = O(1)
def package_lookup():
    try:
        package_id = input('Enter a package ID (1-40): ')
        input_time = input('Enter a time (HH:MM:SS): ')
        (hrs, mins, secs) = input_time.split(':')
        input_time_conversion = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        in_transit_start = get_hash_map().get_hash_value(str(package_id))[9]
        (hrs, mins, secs) = in_transit_start.split(':')
        in_transit_time_conversion = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        delivered_time = get_hash_map().get_hash_value(str(package_id))[10]
        (hrs, mins, secs) = delivered_time.split(':')
        delivered_time_conversion = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        p_id = get_hash_map().get_hash_value(str(package_id))[0]
        address = get_hash_map().get_hash_value(str(package_id))[2]
        required_delivery_time = get_hash_map().get_hash_value(str(package_id))[6]
        weight = get_hash_map().get_hash_value(str(package_id))[7]
        city = get_hash_map().get_hash_value(str(package_id))[3]
        zip = get_hash_map().get_hash_value(str(package_id))[5]


        # Check in transit time against the input time. If the input time is greater than the in transit time,
        # then this package is still at the hub.
        if in_transit_time_conversion >= input_time_conversion:
            status = 'At Hub'
            in_transit = in_transit_start

            print(
            f'**********\n'
            f'Package ID: ' + p_id + '\n'
            f'Delivery address: ' + address + '\n'
            f'Deadline: ' + required_delivery_time + '\n'
            f'City: ' + city + '\n'
            f'Zip: ' + zip + '\n'                         
            f'Weight: ' + weight + '\n'                                
            f'Truck leaves at: ' + in_transit + '\n'
            f'Delivery status: ' + status
            )
        # Check in transit time against the input time. If the input time is less than the in transit time,
        # and less than the delivery time, then the package is in transit.
        elif in_transit_time_conversion <= input_time_conversion:
            if input_time_conversion < delivered_time_conversion:

                status = 'In transit'
                print(
                f'**********\n'
                f'Package ID: ' + p_id + '\n'
                f'Delivery address: ' + address + '\n'
                f'Deadline: ' + required_delivery_time + '\n'
                f'City: ' + city + '\n'
                f'Zip: ' + zip + '\n'                         
                f'Weight: ' + weight + '\n'
                f'Delivery status: ' + status
                )

            # Determine which packages have already been delivered
            else:

                status = get_hash_map().get_hash_value(str(package_id))[10]
                print(
                f'**********\n'
                f'Package ID: ' + p_id + '\n'
                f'Delivery address: ' + address + '\n'
                f'Deadline: ' + required_delivery_time + '\n'
                f'City: ' + city + '\n'
                f'Zip: ' + zip + '\n'                         
                f'Weight: ' + weight + '\n'
                f'Delivered at: ' + status
                )

    except ValueError:
        print('Please enter a valid package number (1-40).')
        exit()

# Function to get final program stats for each truck.
# Time complexity = O(1)
def print_program_stats():
    print('Final Program Stats:')
    print('*****************************************')
    print(f'Time to completion: ' + str(round(final_distance(),2)))
    print('*****************************************')
    print('Truck 1 Packages: ' + str(len(truck1)))
    print('Truck 1 Distance: ' + str(round((truck1_total_distance),2)))
    print('*****************************************')
    print('Truck 2 Packages: ' + str(len(truck2)))
    print('Truck 2 Distance: ' + str(round((truck2_total_distance),2)))
    print('*****************************************')
    print('Truck 3 Packages: ' + str(len(truck3)))
    print('Truck 3 Distance: ' + str(round((truck3_total_distance),2)))