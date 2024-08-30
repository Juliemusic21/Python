#Julie Sakai
#Module 10.2 Assignment

class Employee:
#The __init__ method accepts arguments for the
#name, gender, hourly pay rate, and employee number.

  def __init__(self, name, gender, hourly_pay_rate, employee_number):
    self.__name = name
    self.__gender = gender
    self.__hourly_pay_rate = hourly_pay_rate
    self.__employee_number = employee_number

  #Mutators for the class data attributes for setters.
  def get_name(self):
    return self.__name

  def get_gender(self):
    return self.__gender

  def get_hourly_pay_rate(self):
    return self.__hourly_pay_rate

  def get_employee_number(self):
    return self.__employee_number

  #Accessors for the class data attributes for getters.
  def set_name(self, name):
    self.__name = name

  def set_gender(self, gender):
    self.__gender = gender

  def set_hourly_pay_rate(self, hourly_pay_rate):
    self.__hourly_pay_rate = hourly_pay_rate

  def set_employee_number(self, employee_number):
    self.__employee_number = employee_number

class ProductionWorker(Employee):

  #This class represents a production worker who inherits from the Employee class
  #and adds a shift number attribute.
  
  def __init__(self, name, gender, hourly_pay_rate, employee_number, shift_number):
    Employee.__init__(self, name, gender, hourly_pay_rate, employee_number)
    self.__shift_number = shift_number

  #Mutator for the shift number for getter.
  def get_shift_number(self):
    return self.__shift_number
  
  #Accessors for the shift number for setter.
  def set_shift_number(self, shift_number):
    self.__shift_number = shift_number

  #Additional information of the shift type: day shift, swing shift, or graveyard shift.
  def __str__(self):
    shift_text = {
        1:"Day Shift",
        2:"Swing Shift",
        3:"Graveyard Shift"
    }
    return f"Name: {self.get_name()}\nGender: {self.get_gender()}\n" \
           f"Hourly Pay Rate: ${self.get_hourly_pay_rate():.2f}\n" \
           f"Employee Number: {self.get_employee_number()}\n" \
           f"Shift: {shift_text[self.get_shift_number()]}\n"

def main():
  #Employee class instances.
  employee1 = Employee("Julie Sakai", "Female", 21.25, 98765)
  employee2 = Employee("Josh Van Hooser", "Male", 24.50, 56789)

  #Production work class instances. 
  worker1 = ProductionWorker("Jiji Cat", "Male", 19.25, 12345, 2)
  worker2 = ProductionWorker("Judy Neko", "Female", 20.00, 54321, 1)

  #Display the information to the user of the application.
  print("Employee Information:")
  print(employee1)
  print("\n" + employee2.__str__()) 

  print("\nProduction Worker Information:")
  print(worker1)
  print("\n" + worker2.__str__())

#Call the main function.
if __name__ == "__main__":
  main()