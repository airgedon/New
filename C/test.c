#include <stdio.h>

int test(int x);
    
int main()
{
    int x = 20;
    printf("Before test function called: %d \n", x); 
    test(x);
    printf("After test function called: %d \n", x);

    return 0;
}                                                                 // CALL BY VALUE

int test(int x) {
    x = 90;
    printf("Test function: %d\n",x);
    return 0;
}

// Output: 
// Before test function called: 20 
// Test function: 90
// After test function called: 20 

// -----------------------------------------------------------------------------------------

#include <stdio.h>

int test(int *x);
    
int main()
{
    int x = 20;
    printf("Before test function called: %d \n", x);
    test(&x);
    printf("After test function called: %d \n", x);

    return 0;                                                           //  CALL BY REFERENCE   
}

int test(int *x) {
    *x = 90;
    printf("Test function: %d\n",*x);
    return 0;
}

// Output: 
// Before test function called: 20 
// Test function: 90
// After test function called: 90 
