#include <stdio.h>

// Zachary Williams
// This program receives input and outputs a budget and whether or not they are 
// on track to maintain their budget
int main(){
	
	// Initialize all variables for use in input and output
	double expenseGoal;
	double rent;
	double utilities;
	double transpo;
	double food;
	double carPayment = 581.99;
	// init name at 255 for buffer
	char name[255];


	//receive and assign all input to its respective variable
	printf("Enter your name ");
	scanf("%s", name);
	printf("Enter monthly expense goal (USD): ");
	scanf("%lf", &expenseGoal);
	printf("Enter rent (USD): ");
	scanf("%lf", &rent);
	printf("Enter utilities (USD): ");
	scanf("%lf", &utilities);
	printf("Enter transportation (USD): ");
	scanf("%lf", &transpo);
	printf("Enter food costs (USD): ");
	scanf("%lf", &food);

	// Assess input into these variables for later output
	double expenses = rent + utilities + transpo + food +  carPayment;
	double leftover = expenseGoal - expenses;


	//formatted budget chart of all calculated values, as well as inline percentage calculations.
	printf("Budget Chart for %s\n", name);
	printf("%15s%15s%15s\n", "Expense", "Amount $", "Percent %");
	printf("%15s%15.2lf%15.2lf\n", "Car Payment", carPayment, ((carPayment/expenseGoal)*100));
	printf("%15s%15.2lf%15.2lf\n", "Rent", rent, ((rent/expenseGoal)*100));
	printf("%15s%15.2lf%15.2lf\n", "Utilities", utilities, ((utilities/expenseGoal)*100));
	printf("%15s%15.2lf%15.2lf\n", "Transportation", transpo, ((transpo/expenseGoal)*100));
	printf("%15s%15.2lf%15.2lf\n", "Food", food, ((food/expenseGoal)*100));
	printf("%15s%15.2lf\n", "Expense Goal", expenseGoal);
	printf("%15s%15.2lf\n", "Total expenses", expenses);
	printf("%15s%15.2lf\n", "Leftover amount", leftover);

	// Conditional for whether or not they are saving enough
	if (leftover >= (expenseGoal/5))
		printf("Good job. You are saving enough!\n");
	else
		printf("Try to save more!\n");


	return 0;
}
