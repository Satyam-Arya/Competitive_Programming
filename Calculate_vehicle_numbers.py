def calculate_vehicle_numbers(total_vehicles, total_wheels):
    wheels_per_two_wheeler = 2
    wheels_per_four_wheeler = 4
    
    two_wheeler_count = (total_wheels - wheels_per_four_wheeler * total_vehicles) / (wheels_per_two_wheeler - wheels_per_four_wheeler)
    four_wheeler_count = total_vehicles - two_wheeler_count
    
    return int(two_wheeler_count), int(four_wheeler_count)

# Take input from the user
total_vehicles = int(input("Enter the total number of vehicles: "))
total_wheels = int(input("Enter the total number of wheels: "))

# Calculate the number of two-wheelers and four-wheelers
two_wheeler_count, four_wheeler_count = calculate_vehicle_numbers(total_vehicles, total_wheels)

# Print the results
print(f"Number of Two-wheelers: {two_wheeler_count}")
print(f"Number of Four-wheelers: {four_wheeler_count}")
