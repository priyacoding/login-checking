# user name and pin assign default 
name="priya"
pin=8888
n=3
while n>0:
  try:
   #get user name from input 
   username=input("user name")
   if name==username:
   #user input name and given name is same.ask pin 
      userpin=int(input("user pin"))
      if userpin==pin:
      #user input pin and given same and then login sucess athorwise is go to else codition
         print("login sucess ")
         break
      else:
        #this else part for incorrect inputpin and it shows remaining attempts
        n=n-1
        if n==2:
          print("Entered pin is wrong .please enter valid pin ","you have only",n,"attempt left")
        else:
          if n==1:
            print("Entered pin is wrong .please enter valid pin ","you have only",n,"attempt left")
          else:
            print("your card blocked")
   else:
      #this else part for incorrect inputname and it shows remaining attempts
     n=n-1
     if n==2:
       print("Entered  user name is incorrect.please enter valid username","you have only",n," attempt  left")
     else:
      if n==1:
        print("Entered  user name is incorrect.please enter valid username","you have only",n," attempt  left")
      else:
        print("your card blocked")
    # this part show correction for enter input values
  except ValueError:
    print("Enter the password using numbers only")
  except:
    print("Enter the credential in correct format")
    break
