from datetime import datetime

"""
Problem Statement
Health professionals who are helping a client achieve a healthy body weight, 
sometimes use two computed measures named body mass index and basal metabolic rate.
From the U.S. Centers for Disease Control and Prevention we read,

Body mass index (BMI) is a person’s weight in kilograms divided by the square of their height in meters. 
BMI can be used to screen for weight categories such as underweight, normal, overweight, 
and obese that may lead to health problems. However, BMI is not diagnostic of the body 
fatness or health of an individual.
The formula for computing BMI is

bmi = 10,000 weight / height^2

where weight is in kilograms and height is in centimeters.

Basal metabolic rate (BMR) is the minimum number of calories required daily to 
keep your body functioning at rest. BMR is different for women and men and changes with age. The revised Harris-Benedict formulas for computing BMR are

(women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
(men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
where weight is in kilograms and height is in centimeters.
"""


def main():
    # Get the user's gender, birthdate, height, and weight.
     # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    # Print the results for the user to see.
    gender = input("Please enter your gender (M or F): ").upper()
    birth_str = input("Please enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Please enter your weight in pounds: "))
    height = float(input("Please enter your height in inches: "))

    age = compute_age(birth_str)
    kg = kg_from_lb(pounds)
    inches = cm_from_in(height)
    bmi = body_mass_index(kg, inches)  
    bmr= basal_metabolic_rate(gender, kg, inches, age)

    # print(f"{kg}, birth_str: {birth_str}, age: {age}") # test
    print(f"Age (years): {age}")   
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (inches): {inches:.1f}")
    print(f"Body Mass Index: {bmi:.1f}")
    print(f"Basal Metabolic Rate (kcal/day): {bmr:.0f}")  

    # def basal_metabolic_rate(gender, weight, height, age):
def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    print(birthdate)  
    print(today)


    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1

    # if birthdate.month > today.month or \
    #     (birthdate.month == today.month and \
    #         birthdate.day > today.day):
    #     years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    #Convert weight from pounds to kilograms (1 lb = 0.45359237 kg).
    converts__lb_to_kg = pounds * 0.45359237
    return converts__lb_to_kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    #Converts inches to centimeters (1 in = 2.54 cm).
    converts__in_to_cm = inches * 2.54
    return converts__in_to_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    # bmi = 10,000 weight / height^2
    bmi = 10000 * weight / height**2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    # (women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
    # (men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age

    if gender == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    elif gender == "M":
        # bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return bmr


if __name__ == "__main__":
    main()

