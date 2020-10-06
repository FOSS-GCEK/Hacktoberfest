#include <stdio.h>      
int main()    
{    
	int i,n,arr[100];
    printf("enter the number of elements in an array:");
    scanf("%d",&n);
    printf("enter the elements of array:");     
    for(i=0;i<n;i++)
    {
	scanf("%d",&arr[i]);
    }  
    printf("Original array: \n");    
    for (int i = 0; i < n; i++) {     
        printf("%d ", arr[i]);     
    }             
    printf("\n");         
    printf("Array in reverse order: \n");    
    //Loop through the array in reverse order    
    for (i =n-1; i >= 0; i--)
    {     
        printf("%d ", arr[i]);     
    }     
    return 0;    
}    
