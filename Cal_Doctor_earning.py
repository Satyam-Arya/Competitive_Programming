''' A doctor has a clinic where he serves his patients. The doctor's consultation fees are different for different groups of patients depending on their age. If the patient's age is below 17, fees is 200 INR. If the patient's age is between 17 and 40, fees is 400 INR. If patient's age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one array/List of values representing age of patients visited on that day is passed as input.

    Note:
    Age should not be zero or less than zero or above 120
    Doctor consults a maximum of 20 patients a day
    Enter age value (press Enter without a value to stop): '''

def calculate_earnings(age_input):
    total_earnings = 0
    max_patients = 20

    age_list = age_input.split() # Split the input string into a list of ages

    # Check if the list is not empty and contains at most 20 patients
    if age_list and len(age_list) <= max_patients:
        for age_str in age_list:
            try:
                age = int(age_str)
                # Check if age is within valid range
                if 0 < age <= 120:
                    # Calculate fees based on age groups
                    if age < 17:
                        total_earnings += 200
                    elif 17 <= age <= 40:
                        total_earnings += 400
                    else:
                        total_earnings += 300
                else:
                    print("Invalid age detected. Please enter a valid age.")
                    return
            except ValueError:
                print("Invalid input. Please enter valid integer ages.")
                return

        print(f"Total earnings for the day: {total_earnings} INR")
    else:
        print("Invalid input. Please provide a list of ages for up to 20 patients.")

age_input = input("Enter patient ages (separated by space): ")
calculate_earnings(age_input)

