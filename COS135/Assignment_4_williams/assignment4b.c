#include <stdio.h>

//Zachary Williams
//This program will take a student's name and four grades to give them their
//total as well as their average % and grade.
int main()
{
	char codeInput;
	char classCodes[5] = {'\0', '\0', '\0', '\0', '\0'};
	int currentGrade;
	char studentName[256];
	double gradeTotal = 0;
	int i = 0;

	printf("Enter the student's name (first name and last initial): " );
	scanf("%255s ", studentName);
	while (i <  4){
	// Takes the user input of the subject and grade they received and adds it to the correct variable
		printf("Enter subject code %d and grade(separated by the enter key): ", i + 1);
		if ( scanf(" %c %d", &codeInput, &currentGrade) == 2){
			classCodes[i] = codeInput;
			gradeTotal += currentGrade;
			i++;
		}
		else{
			printf("Invalid input, please try again.\n");
			while (getchar() != '\n');
		}
	}

	// Prints and formats the outputs after manipulation
	double average = (gradeTotal/4);
	printf("\nFinal grades for %s\n", studentName);
	printf("\nTotal for %s: %.0lf\n", classCodes, gradeTotal);
	printf("\nAverage: %.2lf\n", average);
	
	// Prints the letter grade based on conditions.
	int printAverage = (int)average;
		if (printAverage >= 90){
	        printf("Grade: A\n");
		}
		else if ((printAverage >= 80) && (printAverage < 90)){
 		printf("Grade: B\n");
		}
		else if ((printAverage >=70) && (printAverage < 80)){
		printf("Grade: C:\n");
		}
		else{
		printf("Grade: F\n");
		}
		return 0;
}
