//Zachary Williams
// the purpose of this code is to get some basic information and then output it to the terminal in a formatted sentence.

#include <stdio.h>

int main()
{
	// these variables are responsible for getting the input
	char name[40];
	int year;
	double salary;

	//this block is responsible for taking the inputs and assigning them to 
	//the correct variable
	printf("New applicant's name: ");
	scanf("%20[^\n]s", name);
	printf("Enter applicant's birth year: ");
	scanf("%d", &year);
	printf("Enter monthly salary (USD): ");
	scanf("%lf", &salary);

	// does the math for the age of the person
	int age = 2023 - year;

	//outputs the formatted sentence
	printf("%s is a %d years old applicant and requests a monthly salary of %.2lf\n", name, age, salary);

	return 0;
}

