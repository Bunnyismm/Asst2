"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
MINUTES_PER_CREDIT = 2250

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semCost = annual_cost / SEMESTERS_PER_YEAR
    return semCost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monCost = annual_cost / MONTHS_PER_YEAR
    return monCost


def cost_per_day(annual_cost):
    dayCost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return dayCost


def cost_per_credit(annual_cost, credits):
    credCost = (annual_cost / credits)/SEMESTERS_PER_YEAR
    return credCost


def cost_per_class(annual_cost, credits):
    classCost = cost_per_credit(annual_cost,credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return classCost

def cost_per_minute(annual_cost, credits):
    minuteCost = cost_per_semester(annual_cost) / (credits * MINUTES_PER_CREDIT)
    return minuteCost

# ---- PROGRAM ----
def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Total Cost for one year: "))
    credits = float(input("Credits this semester: "))
    while True:
        # Show your menu here.
        print("Options:\n1. Cost per semester\n2. Cost per month\n3. Cost per day\n4. Cost per credit\n5. Cost per class\n6. Cost per minute\nQ. Quit\n")
        choice = str(input("Choose an option: ")).lower()


        if choice == "q":
            break
        elif choice == "1":
            print(f"${cost_per_semester(annual_cost):.2f}")   
        elif choice == "2":
            print(f"${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            print(f"${cost_per_minute(annual_cost, credits):.2f}")
        else:
            print("Invalid option. Please try again.")

    print("Thank you for using CoA calculator.")
# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
