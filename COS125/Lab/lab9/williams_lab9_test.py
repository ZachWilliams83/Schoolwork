from lab9_code import *


############################################################
# Name: DivideOnLessThan
# Header: def DivideOnLessThan(a,b)
# Parameters:
#   a: int or float
#   b: int or float
# Return:
#   float
# Description: This function has two parameters: a and b.
#   This function returns a/b if b < a. If b > a, then it
#   return 0.0

# WRITE TEST HERE
# a = 60
# b = 0
# x = DivideOnLessThan(a,b)
# print(x)

#When using b = 0, it throws a ZeroDivisionError, which should be handled by an edge case.

############################################################
# Name: AskYesOrNo
# Header: def AskYesOrNo():
# Parameters:
#   None
# Return:
#   Returns True if the user types any variant of yes or y
#   Returns False if the user types any variant of no or n
# Description:
#   Asks for yes or no repeatedly until the user gives an
#   accepted answer. Ignores case.

# WRITE TEST HERE
# response = AskYesOrNo()
# print(response)

# non is an accepted answer, that yields False
# if you type out leading with 'no' 'n' 'y' or 'yes' you can continue typing and it will take it as true or false.
############################################################
# Name: SearchListInReverse
# Header: def SearchListInReverse(alist, item)
# Parameters:
#   alist: a list
#   item: element to search for
# Return:
#   If item is in the list, returns index of item. 
#   If the item is not found in the list, None is returned.
# Description: This function searches through the list alist
#   for the element stored in item.

# WRITE TEST HERE
# myList = [[0,1,0],[0,0,0],[0,0,0]]
# item = 1
# result = SearchListInReverse(myList,item)
# print(result)

# does not function using a list of lists.
############################################################
# Name: SplitStringAtPunctuation
# Header: def SplitStringAtPunctuation(astring)
# Parameters:
#   astring: a string that might or might not have punctuation.
# Return:
#   Returns a list containing the split strings with the punctuation
#   removed.
# Description: This function splits a string at punctuation.
#   Punctuation includes: . ? !
#   It does not remove whitespace before or after the splits.

# WRITE TEST HERE
# otherStr = 'come...on!'
# myStr = f'I think that {otherStr}is. quite.......stupid'
# print(SplitStringAtPunctuation(myStr))

#cant get it to break
############################################################
# Name: ChoiceDiscrete
# Header: def ChoiceDiscrete(alist, problist):
# Parameters:
#   alist: a list of any type.
#   problist: a list of probabilities (ints or float). 
#       Must be the same size as alist.
# Return:
#   Returns a random element from alist. 
# Description: The probability
#   of each element being returned is given by the
#   problist. For example, if alist has two elements and
#   problist contains [1,8], then the second element in
#   alist is 8 times more likely to be returned than
#   the first element. In other words, probabilities are
#   relative.

# WRITE TEST HERE
# myList = [[0,1],[1,0],[3,5],[3,8],[6,9]]
# probList = [0 ,0, 0, 0 ,0]
# print(ChoiceDiscrete(myList, probList))

#IndexError returned when all probabilities are 0