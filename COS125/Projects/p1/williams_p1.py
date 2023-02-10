# File: Williams_p1.py
# Author: Zach Williams
# Date: 11/17/2022
# Section: 1001
# E-mail: zachary.j.williams@maine.edu
# Description: Program takes inputs, either words or files and assesses the sentiment value when compared
# to a movie review file.
# Collaboration: I collaborated with Cam Hughes.

# Function searches movie review file for the entered word and returns the number of appearances
# as well as the average score.
def singleWordScore(userWord, movieData):
    movieData = open('movieReviews.txt', 'r')
    accumulator = 0
    allScore = 0
    # read in data line by line for iteration
    file_data = movieData.readlines()
    #scan each line for the searched word.
    for eachLine in file_data:
        if eachLine.find(userWord or (userWord.title)) != -1:
            #Running count of appearances
            accumulator += 1
            #Slicing the score off of the line
            numAdd = int(eachLine[0:1])
            allScore += numAdd
        else:
            accumulator += 0
            numAdd = 0 
    movieData.close()
    return accumulator, allScore

# Function scores every word from a file given by the user and then gives the average score of
# the file as a whole.
def inputFileScore(userFile, movieData):
    counter = 0
    scoreLine = 0
    totalScore = 0
    movieReviews = movieData.readlines()
    userData = userFile.readlines()
    for eachLine in userData:
        # Splitting user file into individual words in a list
        wordList = eachLine.split()
        for eachWord in wordList:
            for otherLine in movieReviews:
                # Finding each word in the user file and comparing it to the movie review file.
                if otherLine.find(eachWord or (eachWord.title)) != -1:
                    counter += 1
                    scoreLine = int(otherLine[0:1])
                    totalScore += scoreLine
    movieData.close()
    return totalScore, counter

#Function takes a userFile and splits it into a list to iterate through each word individually
# It then returns the highest and lowest scores.
def highLowScore(userFile, movieData):
    counter = 0
    scoreLine = 0
    scoreAdd = 0
    scoreList = []
    movieReviews = movieData.readlines()
    userData = userFile.readlines()
    for eachLine in userData:
        # Splitting user file into individual words in a list
        wordList = eachLine.split(',')
        for eachWord in wordList:
            # Calling earlier function to fully search the file. This allows for multiple searches for multiple occurences.
            counter, scoreLine = singleWordScore(eachWord, movieReviews)
            scoreAdd = scoreLine / counter
            scoreList.append(scoreAdd)
    movieData.close()
    print(scoreList)
    return scoreList, wordList, counter


def main():
    choice = 0
    userInput = ''
    while choice != 4:
        print('')
        print("What would you like to do?")
        print("1. Calculate the sentiment score of a single word")
        print("2. Calculate the average score of words in a file")
        print("3. Find the highest and lowest scoring words in a file.")
        print("4. Exit the program")
        choice = int(input("Enter a number 1-4: "))
        if choice == 1:
            movieData = open('movieReviews.txt', 'r')
            userInput = input("Enter a word: ")
            accumulator, allScore = singleWordScore(userInput, movieData)
            if accumulator != 0:
                print(f'The word {userInput} appeared {int(accumulator)} times.')
                print(f'The average score for reviews containing \"{userInput}\" was {str(allScore/ accumulator)[0:4]}')
            else:
                print("That word did not appear.")
        elif choice == 2:
            movieData = open('movieReviews.txt', 'r')
            fileName = input("What is the file name? ")
            inputFile = open(fileName, 'r')
            totalScore, counter = inputFileScore(inputFile, movieData)
            if counter > 0:
                print(f'The file you submitted was scored a {str(totalScore / counter)[0:4]} out of 4.')
            else:
                print(f'No words were found for comparison.')
        elif choice == 3:
            movieData = open('movieReviews.txt', 'r')
            fileName = input("What is the file name? ")
            inputFile = open(fileName, 'r')
            scoreList, wordList, counter = highLowScore(inputFile, movieData)
            scoreMax = max(scoreList)
            scoreMin = min(scoreList)
            if counter > 0:
                print(f'The word with the highest score was {wordList[scoreList.index(scoreMax)]} with a score of {str(max(scoreList))[0:4]}')
                print(f'The word with the lowest score was {wordList[scoreList.index(scoreMin)]} with a score of {str(min(scoreList))[0:4]}')
            else:
                print(f'No words were found for comparison.')
        elif choice == 4:
            quit
        else: 
            print("Nice try! Enter a number 1-4.")
main()
