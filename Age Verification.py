#  Hi This is Ayomide Akinsanya and I would like to talk to you about my code.
month = {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 30,
         "September": 30, "October": 31, "November": 30, "December": 31}  # Firstly, I added a data dictionary called
# month.
# They keys represent the month names while the items represent the number of names in each month.
month2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'
                                                                                                            'December']
answers = ["yes", "no", "Yes", "No"]  # This represents all the valid answers you can write.
valid = ["yes","Yes"]  # This represents all the answers that represent Yes.
invalid = ["no", "No"]  # This represents all the answers that represent No.
response1 = input("Are you a Canadian citizen?")
if response1 in valid:  # This means if your input to response1 is in the valid answers Yes or yes, move to the next question.
    response2 = input("Are you a resident of Alberta?")
    if response2 in valid:  # This means that if your input to response2 are in the valid answers No or no, move to next question
        month1 = input("What is your birth month?")  # month1 is where the user will input their birth month
        if month1 in month:
            day = int(input("What day were you born?"))#If the month the user inputs falls in the month bracket, it is valid
            year = int(input("What year were you born?"))  # The user will input his/her birth year
            if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
# If the year cannot divide 4 without any remainder, then it is not a leap year and hence February has 28 days then. Exception is 1900 as it is a leap year.
                month["February"] = 28
            else:
                month["February"] = 29
            if month[month1] >= day:#If the day of the month he/she put is less than or equal to the maximum number of days, it is valid
                if 1900 > year > 2024:#If the year inputted is not between 1900 and 2024, it is invalid
                    print("Invalid birth date.")
                elif 2024 - year >= 18:#If the person age is 18 and above, he/she can vote and that can be found by subtracting the birth year from 2024.
                    print("You are eligible to vote.")
                    quit()
                elif 2024 - year == 18 and month2.index(month) < month2.index('September'):#If the person is 18 and is born on month before September, he/she can vote
                    print("You are eligible to vote")
                    quit()
                elif 2024 - year == 18 and month2.index(month) == month2.index('September') and day <= 27:
                    #if the person is 18, born on the month September and his/her birthday falls less than 27, the person can vote
                    print("You are eligible to vote.")
                    quit()

                else:
                    print("Invalid birth date.")#If none of the criteria happens, invalid birth date.
                    quit()
            else:
                print("Invalid response.")#If the day of the month he/she put is greater than the maximum number of days, it is invalid
                quit()
        else:
            print("Invalid response.")#If the month the person inputted does not fall under the month bracket, it's inalid.
            quit()
    elif response2 in invalid:#If the answer the person put is under No, then he/she is not eligible to vote.
        print("You are not eligible to vote.")
        quit()
    elif response2 not in answers:#if the answer is neither in valid nor invalid, the response is invalid.
        print("Invalid response.")
        quit()
elif response1 in invalid:#Same for response 1
    print("You are not eligible to vote.")
    quit()
elif response1 not in answers:
    print("Invalid response.")
    quit()
# Also the quit() command means that no other operation can occur after.