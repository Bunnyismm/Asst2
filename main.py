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


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    semCost = annual_cost / SEMESTERS_PER_YEAR
    return f"{semCost:.2f}"


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monCost = annual_cost / MONTHS_PER_YEAR
    return f"{monCost:.2f}"


def cost_per_day(annual_cost):
    dayCost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return f"{dayCost:.2f}"


def cost_per_credit(annual_cost, credits):
    credCost = (annual_cost / credits)/SEMESTERS_PER_YEAR
    return f"{credCost:.2f}"


def cost_per_class(annual_cost, credits):
    classCost = float(cost_per_credit(annual_cost,credits)) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return f"{classCost:.2f}"


# ---- PROGRAM ----
def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Total Cost for one year: "))
    credits = float(input("Credits this semester: "))
    while True:
        # Show your menu here.
        print("Options:\n1. Cost per semester\n2. Cost per month\n3. Cost per day\n4. Cost per credit\n5. Cost per class\nQ. Quit\n")
        choice = str(input("Choose an option: ")).lower()


        if choice == "q":
            break
        elif choice == "1":
            print("$" + str(cost_per_semester(annual_cost)))   
        elif choice == "2":
            print("$" + str(cost_per_month(annual_cost)))
        elif choice == "3":
            print("$" + str(cost_per_day(annual_cost)))
        elif choice == "4":
            print("$" + str(cost_per_credit(annual_cost, credits)))
        elif choice == "5":
            print("$" + str(cost_per_class(annual_cost, credits)))
        else:
            print("Invalid option. Please try again.")

    print("Thank you for using CoA calculator.")
# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
