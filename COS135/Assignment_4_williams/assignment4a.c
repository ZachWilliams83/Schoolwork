#include <stdio.h>

// Zachary Williams
// This project will take a temperature in F and convert it to C

int main(){
	// This will store the user input
	double inputTemp;
	printf("Enter the temperature in Fahrenheit: ");
	scanf("%lf", &inputTemp);
	// This will convert the user's input into celsius
	double celsius = (inputTemp-32)/1.8;
	printf("Temperature in Celsius: %7.3lf\n", celsius);
	return 0;
}
