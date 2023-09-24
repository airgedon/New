#include <stdio.h>

int main() {
    double total_hours, salaryPerWeek, overtime_hour;

    printf("Enter hours: ");
    scanf("%lf", &total_hours);
    
    double salary = 10.0;  
    double overtime_salary = 15.0; 
    
    if (total_hours <= 40) {
        salaryPerWeek = total_hours * salary;
    } else {
        salaryPerWeek = 40 * salary;
        overtime_hour = total_hours - 40;
        salaryPerWeek += overtime_hour * overtime_salary;
    }

    printf("Weekly income is: %.2f USD \n", salaryPerWeek);

    return 0;
}
