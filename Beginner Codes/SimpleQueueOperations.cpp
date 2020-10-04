#include<stdio.h>

#include<process.h>
#include<conio.h>


#define MAX 50
void insert();
void del();
void display();

int arr[MAX];
int rear= -1;
int front= -1;

int main()
{
	int ch;
	while(1)
	{
		printf("=====QUEUE MENU=====");
		printf("\n1.insertion.....\n 2.deletion....\n 3. for display...\n 4. to Quit...\n");
		printf("enter your choice....");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1 :
				insert();
				break;
			case 2 :
				del();
				break;
			case 3 :
				display();
				break;
			case 4 :
				exit(1);
			default:
				printf("wrong choice..\n");				
				
		}
	}
//	return 0;
}

void insert()
{
	int item;
	if(rear == MAX-1)
	printf("===OVERFLOW===");
	else
	{
		if(front == -1)
		front =0;
		printf("enter the element to be inserted...\n");
		scanf("%d",&item);
		rear = rear+1;
		arr[rear]=item;
	}
}
void del()
{
	if( front == -1 || front > rear)
	{
		printf("==UNDERFLOW==\N");
		return ;
	}
	else
	{
		printf("element deleted from the queue is : %d \n", arr[front]);
		front= front + 1;
	}
	
}

void display()
{
	int i;
	if( front == -1)
		printf(" queue is empty ...\n");
	else
	{
		printf(" Queue is : \n");
		for(i= front; i<= rear; i++)
			printf("%d", arr[i]);
		printf("\n");
		}	
	
}
