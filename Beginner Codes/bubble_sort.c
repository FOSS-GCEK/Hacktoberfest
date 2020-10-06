/*bubble sort*/

/*OUTPUT
enter the size of the array
5
enter the elements of the array
5
4
1
8
9
the sorted array is
1	4	5	8	9	*/

#include<stdio.h>
#include<math.h>
void main()
{
	int A[100];
	int i,j,n,temp;
	printf("enter the size of the array\n");
	scanf("%d",&n);
	printf("enter the elements of the array\n");
	for (i=0;i<n;i++)
	{
		scanf("%d",&A[i]);
	}
	for (i=1;i<=n-1;i++)
	{
		for (j=0;j<n-i;j++)
		{
			if(A[j]>A[j+1])
			{
				temp=A[j];
				A[j]=A[j+1];
				A[j+1]=temp;
			}
		}
	}
	printf("the sorted array is\n");
	for (i=0;i<n;i++)
	{
		printf("%d\t",A[i]);
	}
}	

	
