#include<iostream>
using namespace std;

int Add(int,int);
int Subs(int,int);
int Mult(int,int);
int Div(int,int);


int main(){
    int num1, num2,Op;
    char keep;

    do{
        cout<<"Choose a number of the operation";
    	cout<<"\n1.Add";
    	cout<<"\n2.Substract";
        cout<<"\n3.Multiply";
        cout<<"\n4.Divide";
        cin>>Op;
    	
    	cout<<"\nFirst number: ";
    	cin>>num1;
    	cout<<"\nSecond number: ";
    	cin>>num2;
    	
    	switch(Op){
    		case 1: 
    			cout<<"\nResult: "<<Add(num1,num2);
    			break;
    		case 2:
    			cout<<"\nResult: "<<Subs(num1,num2);
    			break;
    		case 3:
    			cout<<"\nResult: "<<Mult(num1,num2);
    			break;
    		case 4:
    			cout<<"\nResult: "<<Div(num1,num2);
    			break;
    		default:
    			cout<<"\nWrong number.";
    			break;
		}
		cout<<"\nAnother operation? y/n";
		cin>>keep;
	}while(keep=='y' || keep== 'Y');

}

int Add(int fnum, int snum){
	return fnum+snum;
}

int Subs(int fnum, int snum){
	return fnum-snum;
}

int Mult(int fnum, int snum){
	return fnum*snum;
}

int Div(int fnum, int snum){
	return fnum/snum;
}




