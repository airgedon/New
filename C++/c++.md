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
