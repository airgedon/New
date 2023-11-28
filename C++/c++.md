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
        cout << "\nGaint id: " << id << endl;
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
```c++
#include <iostream>

using namespace std;

class Rectangle {
    int width, height;
public:
    void set_values (int, int);
    int area() {return width * height;}
};
void Rectangle::set_values(int x, int y){
    width = x;
    height = y;
}

int main()
{
    Rectangle rect;
    rect.set_values(3,4);
    cout << "area: " << rect.area();
    return 0;
}
```
---

## The public Members

```c++
#include <iostream>

using namespace std;

class Line {
    public:
        double length;
        void setLength( double len);
        double getLength(void);  
};


double Line::getLength(void) {
    return length;
}

void Line::setLength(double len) {
    length = len;
}

int main()
{
    Line line;
    
    line.setLength(6.0);   //method
    cout << "Length of line: " << line.getLength() << endl;
    
    line.length = 10.0;
    cout << "Length of line: " << line.length << endl;

    return 0;
}
```
## Default Constructor

```c++
#include <iostream>

using namespace std;

class Box {
    public:
        double length;
        void setWidth( double wid);
        double getWidth(void); 
        Box();
    private:
        double width;
};

Box::Box(void){
    cout<<"The object is being created!" << endl;
}

double Box::getWidth(void) {
    return width;
}

void Box::setWidth(double wid) {
    width = wid;
}

int main()
{
    Box box;
  
     box.length = 10.0;
    cout << "Length of box: " << box.length << endl;
    
    box.setWidth(6.0);   //method
    cout << "Length of box: " << box.getWidth() << endl;

    return 0;
}
```

## Parameterized Constructor

```c++
#include <iostream>

using namespace std;

class Line {
    public:
        void setLength( double wid);
        double getLength(void); 
        Line(double len);
    private:
        double length;
};

Line::Line(double len){
    cout << "Object is created!" << endl;
    length=len;
}

void Line::setLength(double len) {
    length = len;
}


double Line::getLength(void) {
    return length;
}

int main()
{
    Line line(10.0);
    cout << "Length of line (initially): " << line.getLength() << endl;
    
    line.setLength(6.0);   //method
    cout << "Length of line (After setting): " << line.getLength() << endl;
    return 0;
}
```
## Class Destructor

```c++
#include <iostream>

using namespace std;

class Line {
    public:
        void setLength( double wid);
        double getLength(void); 
        Line();
        ~Line();
    private:
        double length;
};

Line::Line(void){
    cout << "Object is created!" << endl;
}

Line::~Line(void){
    cout << "Object is deleted!" << endl;
}

void Line::setLength(double len) {
    length = len;
}


double Line::getLength(void) {
    return length;
}

int main() {
    Line line;
    line.setLength(6.0);   //method
    cout << "Length of line: " << line.getLength() << endl;
    return 0;
}
```
## Friend Function

```c++
#include <iostream>

using namespace std;

class Box {
    double width;
public:
        friend void printWidth( Box box);
        void setWidth(double wid); 
};


void Box::setWidth(double wid) {
    width = wid;
}


void printWidth(Box box) {
    cout << "Width of Box: " << box.width<< endl;
    
}

int main() {
    Box box;
    box.setWidth(10.0);   
    cout << "Using Friend Function: "<< endl;
    printWidth(box);
    return 0;
}
```
```c++
#include <iostream>

using namespace std;


class Box {
    int length;
public:
    Box(): length(0) {}
    friend int printLength(Box);
};

int printLength(Box b){
    b.length += 10;
    return b.length;
} 

int main()
{
    Box b;
    cout << "Length of Box: " << printLength(b) << endl;
    return 0;
}
```

```c++
#include <iostream>

using namespace std;

class B;

class A {
    int x;
public:
    void setdata(int i) {
        x=i;
    }
    friend void mini(A,B);
};


class B{
    int y;
public:
    void setdata(int i) {
        y=i;
    }
    friend void mini(A,B);
};


void mini(A a, B b) {
    if(a.x<b.y)
        cout<<a.x<<endl;
    else
        cout<<b.y<<endl;
}

int main()
{
    A a;
    B b;
    a.setdata(10);
    b.setdata(4);
    mini(a,b);
    return 0;
}
```

```c++
#include <iostream>

using namespace std;

class B;

class A {
    int x=5;
    friend class B;
};


class B{
public:
    void display(A &a) {
        cout<<"Value of x is:"<<a.x;
    }
};

int main()
{
    A a;
    B b;
    b.display(a);
    return 0;
}
```
```c++
#include <iostream>

using namespace std;

class Account {
public:
    float salary=60000;
};

class Programmer:public Account {
public:
    float bonus=5000;
};

int main()
{
    Programmer p1;
    std::cout << "Salary(from parent):"<<p1.salary << std::endl;
    cout<<"Bonus:(form child)"<<p1.bonus<<endl;
    return 0;
}
```
```c++
#include <iostream>

using namespace std;

class Shape {
    protected:
    int width,height;
public:
    void setwidth(int w) {
        width=w;
    }
    void setheight(int h){
        height=h;
    }
};

class paintcost {
public:
    int getCost(int area){
        return area*70;
    }
};

class Rectangle:public Shape, public paintcost {
    public:
    int getArea(){
        return (width*height);
    }
};

int main()
{
    Rectangle rect;
    int area;
    rect.setheight(5);
    rect.setwidth(7);
    area=rect.getArea();
    cout<<"Total area: " << rect.getArea() << endl;
    cout<<"Total paintcost: "<< rect.getCost(area) << endl;
    return 0;
}
```
