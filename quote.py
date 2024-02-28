#exit: program is exit, docstrings, what are the constants, fix the else error (Invalid Input)

'''github link here''' '''ahmad abolhusain'''
'''github link here''' '''name here'''
'''github link here''' '''name here'''

#loops and use of constants
def aed_to_britishPound(money):
   return money*0.2147
def aed_to_dollar(money):
   return money*0.2722
def aed_to_eur(money):
   return money*0.2513
def eur_to_aed(money):
   return money*4
def britishPound_to_aed(money):
   return money*4.66
def dollar_to_aed(money):
   return money*3.67


def code():
   print('"   Main Menu"')
   print("Welcome to Currency Converter")
   print()
   print("------------------------")
   print()
   print("Select the conversion direction:\n1. AED to other currencies\n2. Other currencies to AED\n3. Exit")
   print()
   print()
   money=int(input("Enter your amount you want to convert:"))
   choice=int(input("Enter your choice (1/2/3):"))
   if choice==1:
       print("1. AED to Euro (EUR)\n2. AED to British Pound (GBP)\n3. AED to US Dollar\n4. AED to Exit")
       subchoice=int(input("Enter the Sub choice of currency:"))
       if subchoice==1:
           print(money,"AED is equal to",aed_to_eur(money),"EUR")
       elif subchoice==2:
           print(money,"AED is equal to",aed_to_britishPound(money),"GBP")
       elif subchoice==3:
           print(money,"AED is equal to",aed_to_dollar(money),"USD")
       elif subchoice==4:
           print("Program is exit")
           exit()
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
       else:
           print("Invalid choice!")
   if choice==3:
       print("Program is exit")
       exit()

   #'''the else error (Invalid Input) was on this line like this choice>1 '''
   elif choice>3 or choice<1:
        print("Invalid choice")
def main():
   while True:
       code()
       again=input("Do you want to continue(y/n):")
       if again=='y':
           code()
       elif again=='n':
           print("Program is exit")
           exit()


main()

