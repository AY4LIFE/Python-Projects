#Hi, my name is Ayomide Akinsanya and let me guide on my favourite project yet.
def get_greetings(name):
    if name != "":
        return "Greetings " + str(name) + "! I am your virtual assistant Ayo231."
# So this function called get_greetings(name) takes your name and put it in the sentence.
#  I also added a str() function incase the person tries to add a number or float.


def full_word(sentence, word):  # This is my function full_word() where the user put a sentence and word. Let's see
    sentence = " " + (sentence.lower()) + " "
    # So incase, the character starts or end at the ending, I decided to add spaces between the sentences
    word = word.lower()  # Both for the word and sentence, I use .lower() since it is case insensitive
    n = len(word)  # n is assigned as the length of the word
    i = 0
    while (i < len(sentence)):#while the i assigned is less than the length of the sentence,
        if word == sentence[i:i + n]:#If the word appears in each iteration of the sentence from start to finish.
            if sentence[i - 1].isalnum() == False:#If the character before the word's first letter is non-alphanumeric,
                if word == "":#If the word is just noting,
                    result = False#The result will just be False, because there is no validation
                elif sentence[i + n].isalnum() == False:#If the character after the word's last letter is non-alphanumeric,
                    result = True#The result would be true
                    break#Since it is True, no need for further iterations, hence break the code
                else:#If none of the above happens, just return False
                    result = False
            else:#If the character behind IS alphanumeric, return False
                result = False
        else:#If the word is not even included, just return False
            result = False
        i += 1#I allowed for iterations to keep moving through the sentence for searching
    return result #The product of your result will then be returned


def get_answer(database, sentence):#"I created a function called get_answer() that uses a database and a sentence.
    answers = database.keys()#The possible answers are assigned as the keys of the database.
    for i in answers:#As i moves through the answers option,
        if full_word(sentence,i) == True:#If the full word we created earlier says true,
            return database[i] #Return the output of the key
    else:
        return "Sorry, I do not understand your question."
#Else, just say I don't understand your question

