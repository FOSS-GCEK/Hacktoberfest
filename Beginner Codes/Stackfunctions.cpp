#include <iostream>
using namespace std;
#define maxsize 5
int stack[maxsize],top=-1;
void push(int d);
int pop();
void display();
int main ()
{
    int choice,elem;

    while(1)
    {
        cout<<"1.Push"<<endl<<"2.Pop"<<endl<<"3.Display"<<endl<<"4.Exit"<<endl;
        cin>>choice;
        switch(choice)
        {
         case 1:
             {
                cout<<"Enter The Element :";
                cin>>elem;
                push(elem);
                break;
             }
         case 2:
            {
                 pop();
                 break;
            }
         case 3:
            {
                display();
                break;
            }
         case 4:
            exit(0);
         default:
            cout<<"Error"<<endl;
            break;
        }
    }
    return 0;
}
void push(int d)
 {

     if(top==maxsize-1)
        cout<<"Stack Overflow Condition"<<endl;
     else
     {
         top++;
         stack[top]=d;
         cout<<"Element "<<stack[top]<<" Pushed Succesfully!!!!"<<endl;
     }
     
 }
int pop()
 {
     if(top==-1)
        cout<<"Stack Underflow Condition"<<endl;
     else
     {
         int elem;
         elem=stack[top];
         top--;
         cout<<"Element "<<elem<<" deleted Succesfully!!!!"<<endl;
     }
 }
 void display()
  {
      if(top==-1)
        cout<<"Stack is Empty"<<endl;
      else
      {
          cout<<"Current Stack :";
          for(int i=top;i>=0;i--)
            cout<<stack[i]<<" ";
          cout<<endl;
      }

  }
