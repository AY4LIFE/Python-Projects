#Hi. My name is Ayomide Akinsanya and welcome to any understanding about my code. I will also be use my comments to walk you through.
j = 0
question = int(input("How many data points do you have?"))#Ayomide Akinsanya: This is where the user will input how many data points they have.
while question < 2 and j < 1:#Ayomide Akinsanya: Basically, if the input to the question asked is less than 2 and j(variable) is less than 1(which will always be), #it will print "Must enter at least two data points" and re-ask the question until the input is greater or equal to 2.
    print("Must enter at least two data points.")
    question = int(input("How many data points do you have?"))
years = []#Ayomide Akinsanya: I created a list to store the years that will be inputted later on
fertility_rates = dict()#Ayomide Akinsanya: I created a dictionary that will store the year along with their fertility rates that the user will input later on.
for i in range(1,question+1):#Ayomide Akinsanya: I used a for loop for i that will start with 1 and end with the number of the question +1 so question will be included.
    print("What is the year of data point",i,"?")#Ayomide Akinsanya: The user will be asked for the year of data point (i). i represent what i is at the loop for easier understanding.
    year = int(input())#Ayomide Akinsanya: This is where year will be stored
    k = 0
    while k < 1 and (year < 0 or year > 2024):#Ayomide Akinsanya: If the year is less than 0 or greater than 2024 and k is less than 1(which will obviously be),
        #it will print invalid input and ask the question again, until year is valid
        print("invalid input")
        print("What is the year of data point",i,"?")
        year = int(input())
    years.append(year)#Ayomide Akinsanya: the year the user inputted if passed the validity test will be added to the years list I showed you above.
    print("What is the fertility rate of data point",i,"?")#Ayomide Akinsanya: After, the user will be asked for the fertility rate for the year of data point(i)
    fertility_rate = round(float(input()),2)#Ayomide Akinsanya: Assuming fertility rate will always be 2 decimal places, the code will round whatever input the user entered.
    fertility_rates[year] = fertility_rate#Ayomide Akinsanya: the fertility rate the user entered will be added to the dictionary earlier with the year being the key and fertility rate being the item.
    if year == year:#Ayomide Akinsanya: If the earlier year inputted is the same as the latter year inputted,
        fertility_rates[year] = fertility_rate#Ayomide Akinsanya: the latest fertility rates will then be the item for the year
while (len(years) == years.count(year)):#We are looking for at least two distinct points. To find that I used a loop showing that while the number of numbers in the years loop
    #is equal to the number of times a particular year occurs,
    print("Pick another year of data point for distinct recording")#Ayomide Akinsanya: I will ask the user to pick another year for distinct recording
    year = int(input())#Ayomide Akinsanya: It will still be stored as year
    years.append(year)#Ayomide Akinsanya: It will also be added to the list.
    print("What is the fertility rate for that recording?")#Ayomide Akinsanya: As well as its fellow fertility rate
    fertility_rate = round(float(input()), 2)#Ayomide Akinsanya: Still being stored as fertility_rate
    fertility_rates[year] = fertility_rate#Ayomide Akinsanya: It will also be added to the dictionary.


start_year = int(input("Which year would you like to start with?"))#Ayomide Akinsanya: The user will be asked to input the start_year.
if start_year not in fertility_rates:#Ayomide Akinsanya: If the start year is not in fertility_rates dictionary,
    print("The start year does not exist.")#Just print the start year does not exit and stop the code.
else:
    fertile1 = fertility_rates[start_year]#Ayomide Akinsanya: Else, the program will pick the fertility rate from that year inputted for start year
    end_year = int(input("Which year would you like to end with?"))#Ayomide Akinsanya: Then it will repeat the process for end year.
    if end_year not in fertility_rates:
        print("The end year does not exist.")
    elif end_year <= start_year:#Ayomide Akinsanya: However, if the end year is less than the start year, it should print that End year must be after start year.
        print("End year must be after start year.")
    elif question >= 3 and end_year <= start_year:
        print("End year must be after start year.")
    else:
        fertile2 = fertility_rates[end_year]#Ayomide Akinsanya: Else, the program will pick the fertility rate from that year inputted for end year
        average = (fertile1 + fertile2)/2#Ayomide Akinsanya: The average ferility rates will be the sum of the two fertile rates divided by 2.
        faverage = f"{average:.2f}"#Ayomide Akinsanya: I also formatted it so that the output always comes with two decimal places. For example, 2.5 becomes 2.50
        if fertile2 < fertile1:#Ayomide Akinsanya: If fertile 2 is less than fertile 1, print the average as well as print there is a downward trend.
            print("The average fertility rate of these two years is "+faverage+".")
            print("There is a downward trend.")
        elif fertile2 == fertile1:#Ayomide Akinsanya: If equal to, then sideways trend
            print("The average fertility rate of these two years is "+faverage+".")
            print("There is a sideways trend.")
        elif fertile2 > fertile1:#Ayomide Akinsanya: If greater than, upward trend
            print("The average fertility rate of these two years is "+faverage+".")
            print("There is an upward trend.")









