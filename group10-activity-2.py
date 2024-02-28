'''github link here''' '''ahmad abolhusain'''
'''https://github.com/CjDubaiRIT/GROUP-10.git''' '''CJ'''
'''github link here''' '''Shuja Ahmad'''


#start by defining functions and constants for the currency conversion
def aed_to_britishPound(money):
   dirhams_gbp=0.2154
   return money*dirhams_gbp
def aed_to_dollar(money):
  dirhams_dollar=0.2722
  return money*dirhams_dollar
def aed_to_eur(money):
  dirhams_euro=0.2513
  return money*dirhams_euro
def eur_to_aed(money):
  euro_dirhams=4
  return money*euro_dirhams
def britishPound_to_aed(money):
  gbp_dirhams=4.66
  return money*gbp_dirhams
def dollar_to_aed(money):
  dollar_dirhams=3.67
  return money*dollar_dirhams



#Define function as 'code'
def code():
  #Welcome Message when the currency converter starts
  print('"   Main Menu"')
  print("Welcome to Currency Converter")
  print()
  print("------------------------")
  print()
  #Ask the user whether the currency has to be converted from AED or to AED or exit the program
  print("Select the conversion direction:\n1. AED to other currencies\n2. Other currencies to AED\n3. Exit")
  print()
  print()
  money=int(input("Enter your amount you want to convert:"))
  choice=int(input("Enter your choice (1/2/3):"))
  #If the user chooses a choice then specific subchoices appear
  if choice==1:
      print("1. AED to Euro (EUR)\n2. AED to British Pound (GBP)\n3. AED to US Dollar\n4. AED to Exit")
      subchoice=int(input("Enter the Sub choice of currency:"))
      #If statements are used to give the output for choices and subchoices
      if subchoice==1:
          print(money,"AED is equal to",aed_to_eur(money),"EUR")
      elif subchoice==2:
          print(money,"AED is equal to",aed_to_britishPound(money),"GBP")
      elif subchoice==3:
          print(money,"AED is equal to",aed_to_dollar(money),"USD")
      elif subchoice==4:
          print("Program is exit")
          exit()
      #If a number is entered which does not exists in the subchoices the program will print "Invalid Input!"
      else:
          print("Invalid choice")
  if choice==2:
      print("1. Euro (EUR) to AED\n2. British Pound (GBP) to AED\n3. Dollar to AED\n4. Exit")
      subchoice=int(input("Enter the Sub choice of currency:"))
      if subchoice==1:
          print(money,"EUR is equal to",eur_to_aed(money),"AED")
      elif subchoice==2:
          print(money,"GBP is equal to",britishPound_to_aed(money),"AED")
      elif subchoice==3:
          print(money,"USD is equal to",dollar_to_aed(money),"AED")
      elif subchoice==4:
          print("Program is exit")
          exit()
      #If a number is entered which does not exists in the subchoices the program will print "Invalid choice!"
      else:
          print("Invalid choice!")
  if choice==3:
      print("Program is exit")
      exit()


  #If the user enters choice as any number less than 1 or more than 3 it prints "Invalid chocie!"
  elif choice>3 or choice<1:
       print("Invalid choice")
def main():
  code()
  #While loop is used here to run the function again if the user chooses to do so
  while True:
      again=input("Do you want to continue(y/n):")
      while True:
        if again=='y':
          code()
        elif again=='n':
          print("Program is exit")
          exit()
        break


main()