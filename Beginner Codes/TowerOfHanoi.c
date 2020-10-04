//Towers of Hanoi by Soumyajit Podder

#include <stdio.h>
void hanoi(char, char, char, int);
void main()
{
	int n, m;
	printf("Enter the number of disks in the Tower: ");
	scanf("%d",&n);
	m=pow(2,n)-1;
	printf("Moves required: %d\n", m);
	printf("Disk moved from: \n");
	hanoi('A', 'B', 'C', n);
}
void hanoi(char from, char auxillary, char to, int n)
{
	if(n==1)
	{
		printf("%c to %c\n",from,to);
		return;
	}
	hanoi (from, to, auxillary, n-1);
	hanoi (from, auxillary, to,1);
	hanoi(auxillary, from, to, n-1);
}
