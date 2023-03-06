//Zachary Williams
//The purpose of this code is to receive a character as an input and determine if it is a vowel or consonant
//this code also quits with an input of #
#include <stdio.h>

int main()
{
	// this variable is responsible for the input of a character by the user.
	char entry;


	// while loop that takes in a letter input by the user and compares that character to ASCII values to determine if it is a vowel or a consonant
	// the vowel / consonant determination is made through nested conditionals separated by upper and lowercase values.
	while (entry != '#'){
		printf("Enter a letter (enter # to quit): ");
		scanf(" %c", &entry);

		if((entry > 64) && (entry < 91)){
			if((entry == 65) || (entry == 69) || (entry == 73) ||
			(entry == 79) || (entry == 85) || (entry == 89)){
				printf("%c is  a vowel\n", entry);
			}
			else{
				printf("%c is a consonant\n", entry);
			}	
		}
		else if ((entry > 97) && (entry < 123)){
			if ((entry == 97) || (entry == 101) || (entry == 105) || (entry 				== 111) || (entry == 117) || (entry == 121)){
				printf("%c is a vowel\n", entry);
			}
			else{
				printf("%c is a consonant\n", entry);
			}
		}
		// quits the loop if a # is entered.
		else if (entry == '#'){
			printf("Goodbye!\n");
			break;
		}

		// this lets the user know that only english alphabet characters are valid.
		else{
			printf("Invalid character\n");
		}

	}
	return 0;
}
