//Zachary Williams
//This program takes the customer's name and the amount of each candy they wish to buy and gives them a receipt for how much they owe
//Additionally, this program will discount the price depending on the amount purchased and total price
#include <stdio.h>

int main()
{

	// this first block of variables handles the inputs
	char name[40];
	int chocNum;
	int toffeeNum;

	//this block handles the predetermined prices of the chocolate and toffee
	double chocPrice = 15.50;
	double toffeePrice = 6.90;

	//this section handles the totals pre and post discounts if applicable
	double preDisChoc;
	double preDisToffee;
	double finalChoc;
	double finalToffee;


	//input block for receiving the amounts and customer name
	printf("Enter customer name: ");
	scanf("%20[^\n]s", name);
	printf("Enter number of chocolate bags: ");
	scanf("%d", &chocNum);
	printf("Enter number of toffee bags: ");
	scanf("%d", &toffeeNum);
	

	// conditionals for discounting purchases
	if (chocNum > 5){
		preDisChoc = chocNum * chocPrice;
		finalChoc = ((chocNum * chocPrice) - ((chocNum* chocPrice)*.10));
	}
	else{
		finalChoc = chocNum * chocPrice;
		preDisChoc = finalChoc;
	}

	if (toffeeNum > 2){
		finalToffee = ((toffeeNum * toffeePrice) - ((toffeeNum * toffeePrice) * .05));
		preDisToffee = toffeeNum * toffeePrice;
	}
	else{
		finalToffee = toffeeNum * toffeePrice;
		preDisToffee = finalToffee;
	}
	
	// variables for the total prices of both purchases and discounts if applicable
	double total;
	double disTotal;

	total = finalChoc + finalToffee;


	// conditionals for determining eligibility of discount
	if (total >= 100){
		disTotal = total - (total *.10);
	}
	else{
		disTotal = total;
	}



	// formatted output of the receipt with the prices and totals.
	printf("%18s %s\n", "Hello", name);
	printf("Chocolates %7c%d %9c %.2lf\n", 'x', chocNum, '$',  preDisChoc);
	printf("%20s%10c %.2lf\n\n", "after discount", '$',  finalChoc);
	printf("Toffees %10c%d %10c %.2lf\n", 'x',  toffeeNum, '$',  preDisToffee);
	printf("%20s%10c %.2lf\n\n", "after discount", '$',  finalToffee);
	printf("%-15s%10c %.2lf\n", "total after discount", '$', total);
	printf("%20s%10c %.2lf\n\n", "After 10% discount", '$', disTotal);
	printf("%20s %9c %.2lf\n", "You owe", '$', disTotal);
	printf("%25s\n", "Thank you");


return 0;
}
