#include <stdio.h>

int main()
{
	int i = 0;
	printf("%-10s%-10s%-10s\n","Country", "Region", "Population (M)");
	for (i = 0; i<35; i++)
	{
		printf("%c",'-');
	}
	printf("\n%-10s%-10s%-10d", "USA", "America", 332);
	printf("\n%-10s%-10s%-10d", "Japan", "Asia", 126);
	printf("\n%-10s%-10s%-10d", "France", "Europe", 68);
	printf("\n%-10s%-10s%-10d\n", "Ghana", "Africa", 33);
	return 0;

}
