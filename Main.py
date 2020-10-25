# Ryan Franks
# Calculate Body Mass Index, or BMI - developed by Belgium statistician, Adolphe Quetelet, in the 1800's.
# Calculate Basic Metabolic Rate using height, weight, gender and age.
# Calculate Calories to gain or lose weight based on Mifflin - St. Jeor Equation.

# Define Program Functions
def calculate_bmi_number(weight, height):
    # Calculate BMI = (Weight * 703)/Height^2 by Calling Function calculate_bmi_number
    bmi = float((weight * 703) / height ** 2)
    return bmi


def calculate_num_weight_ideal(height):
    # Calculate weight needing to gain or lose by using the algebraically reworked BMI formula:
    # num_weight_ideal is the ideal weight for the 'Normal' range = (Height^2 * BMI Normal Constant 21.7)/703)
    # Also, One-time calculation of BMI 'Normal' Constant was found by adding the Normal range values of 18.5
    # and 24.9 and dividing by 2 to get 21.7
    bmi_const = float(18.5 + 24.9) / 2
    # Calculate ideal weight
    weight_ideal = int((height ** 2 * bmi_const) / 703)
    return weight_ideal


def calculate_num_weight_change(weight_ideal, weight):
    # Calculate whether user has to gain or lose weight?
    if weight_ideal > weight:
        weight_change = weight_ideal - weight
    elif weight_ideal < weight:
        weight_change = weight - weight_ideal
    else:
        weight_change = 0
    return weight_change


def calculate_num_bmr(height, weight, gender, age):
    # Calculate Basic Metabolic Rate based on Mifflin - St. Jeor Equation:
    if gender == "m":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        # 'f' for female
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return int(bmr)


def calculate_your_weight_change(bmr, calories_used_from_log):
    # Take the person's current bmr and multiply by 7 to get recommended week calorie intake
    bmr_week = bmr * 7
    print("Your BMR for one week: ", bmr_week)
    calorie_gain = calories_used_from_log - bmr_week
    # Take calorie_gain and divide by 3500.  To gain or lose one pound in one
    # week you need to gain or lose 3500 calories in one week.
    lbs_change_one_week = float(calorie_gain / 3500)
    return lbs_change_one_week


def print_bmi_category(bmi):
    if bmi >= 30:
        print("Your BMI is in the Obese range at:  ", format(bmi, ".1f"), sep="")
    elif 25.0 <= bmi <= 29.9:
        print("Your BMI is in the Overweight range at:  ", format(bmi, ".1f"), sep="")
    elif 18.5 <= bmi <= 24.9:
        print("Your BMI is in the Normal range at:  ", format(bmi, ".1f"), sep="")
    else:
        print("Your BMI is in the Underweight range at:  ", format(bmi, ".1f"), sep="")


def print_weight_adjustment(bmi, weight, weight_ideal):
    if 18.5 <= bmi <= 24.9:
        print("Your BMI is in the Normal range.")
    elif bmi > 24.9:
        # Call Function calculate_num_weight_change
        num_weight_change = calculate_num_weight_change(weight_ideal, weight)
        print("You need to lose weight.")
        print("Weight you need to lose: ", format(num_weight_change, "d"), "LBS", sep=" ")
    else:
        # bmi_number less than 18.5
        # Call Function calculate_num_weight_change
        num_weight_change = calculate_num_weight_change(weight_ideal, weight)
        print("You need to gain weight.")
        print("Weight you need to gain: ", format(num_weight_change, "d"), "LBS", sep=" ")


def input_calorie_log():
    # Input and total user calories over 7 days
    food_calorie_list = []
    exercise_calorie_list = []
    for i in range(1, 8):
        food_calories = int(input(f"Food calories consumed on day: {i}: "))
        # Error Checking for food calories input
        count = 1
        while food_calories < 0 or food_calories > 10000:
            if count < 3:
                print("You only get 2 tries.  You are on try:  ", count)
                food_calories = int(input(f"Food calories consumed on day {i} from 0 to 10000: "))
                count += 1
            else:
                print("Too many tries.")
                exit()
        food_calorie_list.append(food_calories)
        exercise_calories = int(input(f"Exercise calories burned on day {i}: "))
        # Error Checking exercise calories input
        count = 1
        while exercise_calories < 0 or exercise_calories > 3000:
            if count < 3:
                print("You only get 2 tries.  You are on try:  ", count)
                exercise_calories = int(input(f"Exercise calories burned on day {i} from 0 and 3000: "))
                count += 1
            else:
                print("Too many tries.")
                exit()
        exercise_calorie_list.append(exercise_calories)
    # Sum total calories for one week
    sum_calorie_lists = sum(food_calorie_list) - sum(exercise_calorie_list)
    print("\nTotal calories used in one week: ", sum_calorie_lists)
    return sum_calorie_lists


def main():
    # Introduction
    print("Weight health calculator.")
    print("Based on height, weight, gender and age.")
    print("Please enter the following information:\n")
    # Input requests to use in calculations
    # Input height in inches
    num_height = int(input("Enter your Height in inches: "))
    # Error check input num_height is between 36 and 84 inches
    count = 1
    while num_height < 36 or num_height > 84:
        count += 1
        if not count == 4:
            print("You only get 3 tries.  You are on try:  ", count)
            num_height = int(input("Height between 36 and 84 inches: "))
        else:
            print("Too many tries.")
            exit()
    # Input weight in pounds
    num_weight = int(input("Enter your Weight in pounds: "))
    # Error check input num_weight is between 50 and 550 lbs
    count = 1
    while num_weight < 50 or num_weight > 550:
        count += 1
        if not count == 4:
            print("You only get 3 tries.  You are on try:  ", count)
            num_weight = int(input("Weight between 50 and 550 pounds: "))
        else:
            print("Too many tries.")
            exit()
    # Input gender m for Male or f for Female
    str_gender = str(input("Enter your Gender.  Please use 'm' for Male and 'f' for Female: "))
    # Make str_gender lowercase
    str_gender = str_gender.lower()
    # Error check input str_gender is 'm' or 'f'
    count = 1
    while str_gender != "m" and str_gender != "f":
        count += 1
        if count < 4:
            print("You only get 3 tries.  You are on try:  ", count)
            str_gender = str(input("Use 'm' for Male and 'f' for Female: "))
            str_gender = str_gender.lower()
        else:
            print("Too many tries.")
            exit()
    # Input age in years
    num_age = int(input("Enter your Age in years: "))
    # Error check input num_age is between 18 and 108
    count = 1
    while num_age < 18 or num_age > 108:
        count += 1
        if count < 4:
            print("You only get 3 tries.  You are on try:  ", count)
            num_age = int(input("Age between 18 and 108: "))
        else:
            print("Too many tries.")
            exit()
    # BMI Categories
    print("\nThe BMI ranges are the following:")
    print("     Obese = 30 or Above")
    print("     Overweight = 25.0 to 29.9")
    print("     Normal Weight = 18.5 to 24.9")
    print("     Underweight = Under 18.5\n")
    # Call Function calculate_bmi_number
    bmi_number = calculate_bmi_number(num_weight, num_height)
    # Call Function to categorize and print BMI into Obese, Overweight, Normal or Underweight
    print_bmi_category(bmi_number)
    print("\nWeight needed to gain or lose to get into the 'Normal' range.\n")
    # Call Function calculate_num_weight_ideal
    num_weight_ideal = calculate_num_weight_ideal(num_height)
    # Call Function to categorize and print the weight that has to gain or has to lose from the ideal weight
    print_weight_adjustment(bmi_number, num_weight, num_weight_ideal)
    # Calculate Basic Metabolic Rate (BMR)
    num_bmr = calculate_num_bmr(num_height, num_weight, str_gender, num_age)
    print("\nTo help lose or gain weight, you need to know how many calories you typically use in one day.")
    print("Based on your height, weight, gender and age, Basic Metabolic Rate (BMR) is calculated.")
    print("The BMR is a baseline to help you to either gain, lose or keep your weight the same.\n")
    print("Your current BMR is: ", format(num_bmr), "Calories Per Day", sep=" ")
    print("\nEnter the number of calories consumed and the number of calories exercised each day.")
    print("This log can help you set calorie goals.\n")
    # Call Function input_calorie_log() to input calories used in 1 week
    calories_used_one_week = input_calorie_log()
    # Call Function calculate_your_weight_change from log and bmr
    your_weight_change = calculate_your_weight_change(num_bmr, calories_used_one_week)
    print("\nPounds change for one week: ", format(your_weight_change, ".2f"), sep="")


# Call to main() #
main()
