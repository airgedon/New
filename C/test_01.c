#include <stdio.h>

struct Student {
  char name[50];                                 //Structures Example
  int age;
  float gpa;
};

int main() {
  struct Student student1;

  printf("Enter student name: ");
  scanf("%s", student1.name);

  printf("Enter student age: ");
  scanf("%d", &student1.age);

  printf("Enter student GPA: ");
  scanf("%f", &student1.gpa);

  printf("\nStudent information:\n");
  printf("Name: %s\n", student1.name);
  printf("Age: %d\n", student1.age);
  printf("GPA: %.2f\n", student1.gpa);

  return 0;
}

-------------------------------------------------------------------------


  #include <stdio.h>

union Contact {
  char phone[20];                                                       // Union Example
  char email[50];
};

int main() {
  union Contact contact1;

  printf("Enter phone number or email address: ");
  scanf("%s", contact1.phone);

  printf("Enter phone number or email address: ");
  scanf("%s", contact1.email);

  printf("\nContact information:\n");
  printf("Phone number: %s\n", contact1.phone);
  printf("Email address: %s\n", contact1.email);

  return 0;
}
