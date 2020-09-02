# Welcome! In short, this program makes calculations based on simple physics formulas. Each function requires user input in order to calculate their respective formula.

# This function serves to calculate final velocity of an object following the formula V = u + at, where V is the final velocity, u is the initial velocity, a is acceleration, and t is time.

def final_velocity_calculator():
  print("Find Velocity V, given u, a, and t, where ")
  initial_velocity = float(input("initial velocity u = ? (m/s) "))
  acceleration = float(input("acceleration a = ? (m/s^2) "))
  velocity_time = float(input("time t = ? (s) "))

  final_velocity = initial_velocity + (acceleration * velocity_time)

  print(f"The final velocity is {final_velocity} m/s.")

# This function serves to calculate the acceleration of an object following the formula a = (V - u) / t, with the same aforementioned variables.

def acceleration_calculator():
  print("Find Acceleration A, given u, t, and v, where ")
  initial_velocity = float(input("initial velocity u = ? (m/s) "))
  velocity_time = float(input("time t = ? (s) "))
  final_velocity = float(input("final velocity v = ? (m/s) "))

  final_acceleration = (final_velocity - initial_velocity) / velocity_time

  print(f"The final acceleration is {final_acceleration} m/s^2.")

# This function serves to caculate the time an object takes to reach its final velocity following the formula t = (V - u) / a, with the same aforementioned varaibles.

def time_calculator():
  print("Find time T, given u, a, and v, where ")
  initial_velocity = float(input("initial velocity u = ? (m/s) "))
  final_velocity = float(input("final velocity v = ? (m/s) "))
  acceleration = float(input("acceleration a = ? (m/s^2) "))

  velocity_time = (final_velocity - initial_velocity) / acceleration

  print(f"The time it took to achieve the final velocity is {velocity_time} seconds.")

# This function serves to calculate the initial velocity of an object following the formula u = V / at, with the same aforementioned variables.

def initial_velocty_calculator():
  print("Find initial velocity u, given a, t, and v, where ")
  acceleration = float(input("acceleration a = ? (m/s^2) "))
  velocity_time = float(input("time t = ? (s) "))
  final_velocity = float(input("final velocity v = ? (m/s) "))

  initial_velocity = final_velocity - (acceleration * velocity_time)

  print(f"The initial velocity was {initial_velocity} m/s.")

# This is the main function, enabling a user to select each type of calculation by requiring input to select which function to call. If the user inputs 5, the menu is closed and the program ends.

def main():
  menu_choice = 0
  while (menu_choice != 5):
    print("What would you like to calculate? ")
    print("1. Final Velocity ")
    print("2. Acceleration ")
    print("3. Time")
    print("4. Initial Velocity")
    print("5. Exit")
    menu_choice = int(input())
    if menu_choice == 1:
      final_velocity_calculator()
    elif menu_choice == 2:
      acceleration_calculator()
    elif menu_choice == 3:
      time_calculator()
    elif menu_choice == 4:
      initial_velocty_calculator()

# This simply calls the main function.

main()