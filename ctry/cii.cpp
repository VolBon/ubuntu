#include <iostream>
using namespace std;


int factorial(int n){
    if(n<0){
        throw 99;
    }
    return n;
}

int main() {
    try{
        cout<<factorial(-1)<<endl;
        
    }
    catch(int pError){
        cout<<pError<<endl;
    }
	// your code goes here
	return 0;
}
