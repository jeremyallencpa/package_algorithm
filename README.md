Stated Problem
The purpose of this project is to create an algorithm using Python to deliver 40 packages in under 140 miles. The project has the following constraints:
1)	Three trucks available for deliveries
2)	Two drivers available: driver stays with the same truck as long as that truck is still making deliveries
3)	40 packages to deliver
4)	Maximum mileage of 140 miles
5)	Maximum speed of 18 miles per hour
6)	Maximum 16 packages per truck
7)	Trucks have infinite amount of gas and no need to stop
8)	Trucks leave hub no earlier than 08:00 a.m.
9)	Delivery and loading times are instantaneous
10)	Delivery address for package #9 is wrong and will be corrected at 10:20 a.m.
11)	Distances provided in the distance table are equal regardless of direction traveled
12)	Day ends when all 40 packages are delivered.

Algorithm Identification
The core algorithm in this program is a function called ‘greedy_algorithm’. It is located in the distance_algorithm.py python file.
Logic Comments
The function ‘greedy_algorithm’ has the following parameters:
1)	‘package_list’ – list of packages on a specific truck.
2)	‘truck_num’ – truck number used in algorithm.
3)	‘current_location’ – recursive variable to track the current location of a given truck.
The ‘current_location’ is compared to the distances to the address for each package in the ‘package_list’ to determine what the shortest distance is. Once the minimum value is found (‘min’) then that package is removed from the ‘package_list’ and the truck will move to that location (‘current_location’) and that package is added to an optimized package list along with its index. The end goal of the function is to have an optimized delivery route for each truck. This is a recursive algorithm that will run until the base case is reached (i.e. length of ‘package_list’ = 0).
Pseudocode:
Take in the function parameters described above (‘package_list’, ‘truck_num’, ‘current_location’)
Create the base case to break the recursion algorithm
	If the length of the package list = 0
		Return the package list
If the length of the package list is not 0, enter the recursive portion of the function
	Set min = 15 (variable used to hold the location that is closest to the current location)
	Set location = 0 (variable used to hold value for next location for truck)
	If length of ‘package_list’ != 0:
Enter first for loop  For each package in ‘package_list’
If ‘current_distance’ <= ‘min’ (searches through distances from current location to package location)
	Update ‘min’ to ‘current_distance’
	Update ‘location’ to ‘value’ (value represents new current location)
			Enter second for loop  if ‘current_distance’ = ‘min’
					If ‘truck_num’ = 1
						truck1.append(package) (append package to optimized list truck1)
truck1_index.append(package[1]) (append current package number to optimized truck index list)
package_list.pop(package_list.index(package)) (remove ‘delivered’ package from package list)
‘current_location’ = ‘location’ (set new current_location to the location of the package that was just delivered’
‘greedy_algorithm’ recursive call to loop through the new ‘package_list’ that has shorted by the delivered packages and has a new ‘current_location’ of recently delivered package(s). Will run until ‘package_list’ is empty.
					Repeat above for truck_num = ‘2’. Will run until ‘package_list’ is empty.
					Repeat above for truck_num = ‘3’. Will run until ‘package_list’ is empty.
		Base case is reached and the algorithm is finished.

Development Environment
This program was written using Python 3.9 with PyCharm Community Edition v.2020.3.5x64 on a Windows computer.
Space-Time and Big-O
The overall program has a time and space complexity of O(n^2) for the worst-case scenario. See tables below, broken down by each python file within the program.
distance_algorithm.py
Function	Time Complexity	Space Complexity
get_address	O(1)	O(1)
get_total_distance	O(1)	O(1)
current_distance	O(1)	O(1)
get_truck_time	O(1)	O(1)
greedy_algorithm	O(n^2)	O(n^2)
delivery1_index	O(1)	O(1)
delivery2_index	O(1)	O(1)
delivery3_index	O(1)	O(1)
Total	=O(7+n^2) --> O(n^2)	=O(7+n^2) --> O(n^2)


hashmap.py 
Function	Time Complexity	Space Complexity
create_hash_key	O(1)	O(1)
insert	O(1)	O(1)
update	O(n)	O(n)
get_hash_value	O(n)	O(n)
Total	=O(2+2n) --> O(n)	=O(2+2n) --> O(n)

main.py 
Function	Time Complexity	Space Complexity
user_input = 1	O(1)	O(1)
user_input = 2	O(n^2)	O(n^2)
user_input = 3	O(1)	O(1)
user_input = 0	O(1)	O(1)
Total	=O(n^2 + 3) --> O(n^2)	=O(n^2 + 3) --> O(n^2)

menu.py  
Function	Time Complexity	Space Complexity
menu	O(1)	O(1)
package_list_with_status	O(n^2)	O(n^2)
package_lookup	O(1)	O(1)
print_program_stats	O(1)	O(1)
Total	=O(n^2 + 3) --> O(n^2)	=O(n^2 + 3) --> O(n^2)

packages.py  
Function	Time Complexity	Space Complexity
set_start	O(n)	O(n)
compare_address_list	O(n^2)	O(n^2)
calc_final_distance	O(n)	O(n)
final_distance	O(1)	O(1)
Total	=O(n^2 + 3) --> O(n^2)	=O(n^2 + 3) --> O(n^2)


Reader.py 
Function	Time Complexity	Space Complexity
N/A - line 16	O(n)	O(n)
get_delivery1	O(1)	O(1)
get_delivery2	O(1)	O(1)
get_delivery3	O(1)	O(1)
get_hash_map	O(1)	O(1)
Total	=O(n+ 4) --> O(n)	=O(n+ 4) --> O(n)

Scalability and Adaptability
This solution is highly scalable and adaptable as the greedy algorithm approach used can adjust to any amount of packages or any set of address data and still achieve a reasonably minimal mileage.
Software Efficiency and Maintainability
The efficiency is low as the worst-case scenario of this program is O(n^2) in terms of time complexity. This works fine with only 40 packages, however, if there were larger numbers of packages introduced into the program the program could run slowly. The code is easy to maintain as there are relatively few functions, relevant comments within the program, and simple core functionality.
Self-Adjusting Data Structures
The strengths of the ‘greedy_algorithm’ are that it performs all required functions, meets project constraints, and is able to quickly find the optimal truck route. The weaknesses of this approach are that the program will be less efficient when more packages are introduced as the time complexity is O(n^2). The strengths of the hash table are that it is dynamic and it can store, update and get data easily – most operations with the hash table are O(1) in time complexity. A weakness of the hash table approach is its scalability; were the number of packages to increase there could be collisions in the data which would slow down the program significantly.
Original Code
Code is original.
Identification Information
See ‘main.py’ file.
Process and Flow Comments
Code is commented generously.
Data Structure
The hash map is a self-adjusting data structure that is used with the ‘greedy_algorithm’ to easily hold, update, insert, and retrieve data.
Explanation of Data Structure
The hash map is a self-adjusting data structure that is used with the ‘greedy_algorithm’ to easily hold, update, insert, and retrieve data. It holds all package data including delivery times, what truck the package is on, and what times it leaves.
 Hash Table
See screenshot below from hashmap.py:
 
Look-up Function
See screenshot below from hashmap.py:
 
Interface
See screenshot below from main. Option 1 will show specific package data, option 2 will display all package data at a given time, and option 3 shows total program stats.:
 
Strengths of Chosen Algorithm
The strengths of the ‘greedy_algorithm’ are that it 1) performs all required functions, 2) meets project constraints, and 3) is able to quickly find the optimal truck route.
Other Possible Algorithms
Other possible algorithms I could have used include: 1) breadth first search, and 2) depth first search. Both algorithms start at a root node (in this case, the root node would be the hub) and traverses a tree to find the shortest distance between points. Both of these algorithms would therefore satisfy the requirements of the scenario.
Algorithm Differences
The main difference between the two approaches above and my approach are that each of the above algorithms uses a graph data structure, while the greedy algorithm approach in my solution utilizes a hash table data structure.
Verification of Data Structure
Program meets all requirements, there is verification of total miles for all trucks, total delivery distance is less than 140 miles, all packages delivered on time, hash table is present, and reporting is accurate and efficient.
Efficiency
As the number of packages increases in this program, the time complexity increases at O(n^2); while the lookup function itself is O(1), the program must run completely prior to the lookup and therefore as the number of packages increases the lookup would become more slow.
Overhead
As the number of packages increased, the space required for the data structure would increase at the rate of O(n) as the hash table would need to adjust in size to hold the packages to avoid collisions as much as possible.
Implications
As the number of trucks and cities increased look-up time and space usage would also increase. Look-up time would increase at a rate of O(n^2) and space usage would increase at a rate of O(n).
Other Data Structures
Two other data structures that could be used to meet the project requirements would be a graph, and a binary search tree.
Data Structure Differences
A graph has a finite amount of vertices, edges, and values that connect them (and can have values assigned to the edges). A binary search tree stores data with nodes greater than the keys in the nodes left subtree than those in the right subtree and is used for lookups. The hash table is a list of lists with data stored by an index.
Sources
See citations below. Citations are referenced in sections K2 and K2A :
1)	Breadth-first search: https://en.wikipedia.org/wiki/Breadth-first_search (accessed May 2021)
2)	Depth-first search: https://en.wikipedia.org/wiki/Depth-first_search (accessed May 2021)
3)	Graph: https://en.wikipedia.org/wiki/Graph_(abstract_data_type) (accessed May 2021)
4)	Binary search tree: https://en.wikipedia.org/wiki/Binary_search_tree (accessed May 2021)
5)	Hash table: https://www.geeksforgeeks.org/hashing-data-structure/ (accessed May 2021)

