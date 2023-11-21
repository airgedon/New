## Hello World
```c++
#include <iostream>

using namespace std;

int main()
{
    cout<<"Hello World";

    return 0;
}
```
## Scope Resolution operator

```c++
#include <iostream>

using namespace std;

int x;

int main()
{
    int x = 19;
    cout<<"Value of global x is " << ::x;
    cout<<"\nValue of local x is " <<x;

    return 0;
}
```
## Accessing the Data Members

```c++
#include <iostream>

using namespace std;

class Box {
public:
    double len;
    double brd;
    double ht;
};

int main()
{
    Box b1;
    Box b2;
    double vol=0.0;
    
    b1.ht = 5.0;
    b1.brd = 6.0;
    b1.len = 7.0;
    
    b2.ht = 10.0;
    b2.brd = 12.0;
    b2.len = 13.0;

    vol=b1.brd*b1.ht*b1.len;
    cout << "Volume of Box1 is:\n" << vol <<endl;
    return 0;
}
```

```c++
#include <iostream>

using namespace std;

class Person {
public:
    void getDetails(){
        string name="Billa";
        cout<<"My name is: "<<name;
    }
};

int main()
{
    Person p;
    
    p.getDetails();
    return 0;
}
```
# A function outside a class

```c++
#include <iostream>

using namespace std;

class A {
public:
    void fun();
};

void A::fun() {
    std::cout << "fun() Called outside!" << std::endl;
}

int main()
{
    A a;  // A is the class's name and a is the object's name
    a.fun();
    return 0;
}
```

```c++
#include <iostream>

using namespace std;

class Gaint {
public:
    string gaintname;
    int id;
    void printname();
    void printid() {
        std::cout << "\nGaint id: " << id << std::endl;
    }
};
void Gaint::printname(){
    cout << "\nGaintName is: " << gaintname;
}

int main()
{
    Gaint obj;
    obj.gaintname ="xyz";
    obj.id=15;
    obj.printname();
    cout<<endl;  // to give extra line (space)
    obj.printid();
    return 0;
}
```
