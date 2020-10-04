//Hello! I am Arpit Raj and wants to contribute in open source and learn through Hacktoberfest.

//C program to print prime numbers between 1 to 100

#include<stdio.h>
int main()
{
  int i,j,count;
  printf("Prime numbers between 1 and 100 are :");
  for(i=1;i<=100;i++)
  {
    count=0;
    for(j=1;j<=i;j++)
    {
      if(i%j==0)
      count++;
    }
    if(count==2)
    printf(" %d",i);
  }
}
