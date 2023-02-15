#include <stdio.h>

int main()
{
	char storeName[] = "The Z Store";
	double item1 = 21.45;
	double item2 = 10.00;
	double item3 = 14.90;
	double item4 = 33.50;

	printf("Welcome to %s\n\n", storeName);
	printf("%-10s$%-10.2f%-10s$%-10.2f\n","Item 1",item1,"x2",item1*2);
	printf("%-10s$%-10.2f%-10s$%-10.2f\n","Item 2",item2,"x2",item2*2);
	printf("%-10s$%-10.2f%-10s$%-10.2f\n","Item 3",item3,"x2",item3*2);
	printf("%-10s$%-10.2f%-10s$%-10.2f\n\n","Item 4",item4,"x2",item4*2);
	printf("%-10s$%-10.2f\n\n", "Item Total:", ((item1*2)+(item2*2)+(item3*2)+(item4*2)));
	printf("%-10s$%-10.2f\n", "GST:", ((item1*2)+(item2*2)+(item3*2)+(item4*2))*.10);
	printf("%-10s$%-10.2f\n", "Total:", (((item1*2)+(item2*2)+(item3*2)+(item4*2))+(((item1*2)+(item2*2)+(item3*2)+(item4*2))*.10)));
	return 0;
}
