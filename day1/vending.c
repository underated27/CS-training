/*design a python program for vending machine which is dedicated for pepsi.Capacity of the machine is 200.you can start with stock in hand as 70
let the customer request for n number of pepsi bottles check whether the machine is having sufficient bottles 
If yes print n times "take your pepsi" Otherwise available bottles count can be printed those many times and
Display an additional message out of stock
Note:
    At both the cases print the last line as Happy drinks*/

#include <stdio.h>

#define CAPACITY 200

int stock = 70;

void request_pepsi() {
    int n;
    printf("How many bottles of Pepsi would you like? ");
    scanf("%d", &n);
    if (n <= stock) 
    {
        for (int i = 0; i < n; i++) 
        {
            printf("Take your Pepsi\n");
        }
        stock -= n;
    }
     else 
     {
        for (int i = 0; i < stock; i++) 
        {
            printf("Take your Pepsi\n");
        }
        printf("Out of stock\n");
        stock = 0;
     }
    printf("Happy drinks\n");
}

int main() {
    request_pepsi();
    request_pepsi();
    request_pepsi();
    return 0;
}

