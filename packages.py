import distance_algorithm
from distance_algorithm import *
import reader

# Lists created to hold each delivery and trucks distances.
delivery1 = []
delivery2 = []
delivery3 = []
reader1 = reader.get_delivery1()
reader2 = reader.get_delivery2()
reader3 = reader.get_delivery3()
truck1_distance = []
truck2_distance = []
truck3_distance = []

# Starting times for each truck
truck1_start = ['8:00:00']
truck2_start = ['9:30:00']
truck3_start = ['11:00:00']


# Function to set delivery start time for a trucks packages to the specified start time.
# Time complexity = O(n)
def set_start(reader, start, delivery):
    for index, value in enumerate(reader):
        reader[index][9] = start[0]
        delivery.append(reader[index])


set_start(reader1, truck1_start, delivery1)
set_start(reader2, truck2_start, delivery2)
set_start(reader3, truck3_start, delivery3)


# Function to compare truck1 addresses to address list. This is a nested for loop.
# Time complexity = O(n^2)
def compare_address_list(delivery, distance):
    for index, outer in enumerate(delivery):
        for inner in distance_algorithm.get_address():
            if outer[2] == inner[2]:
                distance.append(outer[0])
                delivery[index][1] = inner[0]


compare_address_list(delivery1, truck1_distance)
compare_address_list(delivery2, truck2_distance)
compare_address_list(delivery3, truck3_distance)

# Call algorithm to sort packages for each truck
distance_algorithm.greedy_algorithm(delivery1, 1, 0)
distance_algorithm.greedy_algorithm(delivery2, 2, 0)
distance_algorithm.greedy_algorithm(delivery3, 3, 0)


# Function to calculate total distance of each truck and distance of each package.
# Time complexity = O(n)
def calc_final_distance(delivery_index, delivery, start, delivery_list):
    total_distance = 0
    for index in range(len(delivery_index)):
        try:
            total_distance = distance_algorithm.get_total_distance(int(delivery_index[index]),
                                                                   int(delivery_index[
                                                                           index + 1]), total_distance)

            deliver_package = distance_algorithm.get_truck_time(
                distance_algorithm.current_distance(int(delivery_index[index]),
                                                    int(delivery_index[index + 1])), start)
            delivery_list[index][10] = (str(deliver_package))
            reader.get_hash_map().update(int(delivery_list[index][0]), delivery)
        except IndexError:
            pass
    return total_distance


truck1_total_distance = calc_final_distance(delivery1_index(), delivery1, truck1_start, delivery1_list())
truck2_total_distance = calc_final_distance(delivery2_index(), delivery2, truck2_start, delivery2_list())
truck3_total_distance = calc_final_distance(delivery3_index(), delivery3, truck3_start, delivery3_list())


# Function to return the total distance for all packages. Must be less than 140.
# Time complexity = O(1)
def final_distance():
    return truck1_total_distance + truck2_total_distance + truck3_total_distance