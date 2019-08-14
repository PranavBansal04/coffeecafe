
#dictionary with zipcode as keys and number of items as values
zipcodelist={54984:0}
#list for storing age of the customers
agelist=[]
#counter variable for keeping track of number of customers less than 30
c30less=0
#counter variable for keeping track of number of customers equal to and more than 30
c30more=0
#variable for keeping count of order number
ordernum=1
print("ZipCode of the Cafe - 54984")
#infinite loop
while(True):
    
    #print order number
    print("Order",ordernum)
    #if zip code is entered as 0 then we will need to break execution of 2 loops
    #execution of first loop can be broken by simple break statement
    #the termination of second loop will be based on the value of flag variable
    #the flag will be equal to one when first loop is broken due to zip code 0
    flag=0
    while(True):
        #input for zipcode
        print("Enter ZipCode: (press 0 to exit)")
        zip_code=int(input())
        #if zipcode is zero then we need to stop program execution
        #for that assign 1 to flag variable so execution of outerloop
        #can be terminated
        if(zip_code==0):
            flag=1
            break
        #invalid input condition(given in the question)
        if(len(str(zip_code))>5):
            print("Invalid ZipCode!")
            #continue taking input for zipcode until a
            #valid number is entered
            continue
        #if valid zipcode is entered then break the loop
        else:
            break
    #check if above loop is broken due to zipcode value 0
    #if so then stop the outer loop using break
    if(flag==1):
        print("Goodbye.")
        break
    #reprompt the user for age input until valid age is entered
    while(True):
        #input for age
        print("Enter Age: ")
        age=int(input())
        #validation condition
        if(age<10 or age>110):
            print("Invalid Age!")
            continue
        else:
            break

    #Maximum 3 reprompts are to be done for
    #number of items
    count=0
    #with the help of flag variable we can discard the present order
    #and do not save the values for it into the arrays
    flag=0
    while(True):
        #increase count for the attempt
        count+=1
        #input for number of items
        print("Enter number of items: ")
        n=int(input())
        #if its third attempt and still a big number is entered
        #then acccept the number
        if(count==3):
            break
        #in the third attempt a negative number is entered
        if(n<0 and count==3):
            #assign 1 to flag
            flag=1
            #display error message for the order
            print("ERROR!Order Discarded.")
        #vaidation condition
        if(n<1 or n>12):
            print("Invalid number!")
            continue
        else:
            break
    #if above loop is terminated due to negative value input in third attempt
    #then do not save the data for this order, also the order number will not
    #increase
    if(flag==1):
        continue
    #if the zipcode is already in the dicionary then
    #increase the value of number of items by entered number of items
    #for this order
    if(zip_code in zipcodelist.keys()):
        zipcodelist[zip_code]+=n
    #if zipode is not in the list then add a new key to the dictionary
    #and assign number of items for current order as its value
    else:
        zipcodelist[zip_code]=n
    #add age of the customer to the age list
    #the data from age list will be used later
    #for calculating average age
    agelist.append(age)

    #we need to display total number of items
    #ordered by customers under 30 and above 30
    
    #if age is less than 30
    #then add number of items to
    #the relevant variable
    if(age<30):
        c30less+=n
    #otherwise add number of items to
    #the other variable
    else:
        c30more+=n

    ordernum+=1


#number of items ordered from same zipcode as the cafe shop can be found by accessing the required key
print("Number of items ordered by customers from the same zipcode as cafe(549840):",zipcodelist[54984])
#display data for other zipcodes
print("Total number of items ordered by cutomers from different ZipCodes: ")
for i in zipcodelist.keys():
    #skip the zipcode of cafe shop
    #as data for it has already been displayed
    if(i==54984):
        continue
    #display number of items for the zipcode
    print(i,":",zipcodelist[i])

#calculate average age
print("Average customer Age:",sum(agelist)/len(agelist))
#display c30less and c30more
print("Total number of items ordered by customers under 30:",c30less)
print("Total number of items ordered by cutomers 30 and older:",c30more)

