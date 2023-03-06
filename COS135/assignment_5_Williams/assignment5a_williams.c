//Zachary Williams
//The purpose of this code is to input 3 numbers and see if at least 2 of them are equal and then output the correct number.

#include <stdio.h>


int main()
{
	/* this block of 3 nums will hold the input values for the 3 numbers
	 */
	int num1;
	int num2;
	int num3;
	// These two variables will hold the truth value for a correct equality
	// while the equality value is essentially a true or false value for an equality found
	int equality;
	int truthVal;
	
	// Input for the numbers.
	printf("Enter the first number: ");
	scanf("%d", &num1);
	printf("\nEnter the second number: ");
	scanf("%d", &num2);
	printf("\nEnter the second number: ");
	scanf("%d", &num3);


	// conditionals for assessing equality of at least 2 numbers as well as assigning the correct value to be re-used in output.
	if (num1 == num2){
		equality = 1;
		truthVal = num1;
	}
	else if (num1 == num3){
		equality = 1;
		truthVal = num1;
	}
	else if (num2 == num3){
		equality = 1;
		truthVal = num2;
	}
	else
		equality = 0;

	// output for both cases of output possiiblity.
	if (equality == 1)
		printf("\nValue: %d\n", truthVal);
	else
		printf("\nValue: ERROR\n");	
	return 0;
}
