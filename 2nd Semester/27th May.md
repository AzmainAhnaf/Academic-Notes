# Problem Statement 1: 
Use the following class Test with the data members and methods. 
i) Initialize private data members x and y to 0 when empty constructor is called 
ii) Initialize private data members x and y using parameterized constructor is called 
iii) Initialize private data members x and y from another object using copy constructor 
iv) The data member z keeps track of total objects created 
v) Write a method to initialize x and y vi) Write a method to display data member z only 
vii) Write a method to display x, y and z where their values can’t be changed 
viii) Create five objects ix) Find the sum of x 
x) Find the object number whose y value is maximum 
xi) Write destructor

**Source Code**:
```cpp
#include<bits/stdc++.h>
using namespace std;

class Test
{
    int x;
    int y;
    static int z;
    public:
    Test()
    {
        x=0;
        y=0;
        z++;
    }
    Test(int a, int b)
    {
        x=a;
        y=b;
        z++;
    }

    Test(const Test &t)
    {
        x=t.x;
        y=t.y;
        z++;
    }

    void SetData(int a, int b)
    {
        x=a;
        y=b;
    }
    int GetX()
    {
        return x;
    }

    int GetY()
    {
        return y;
    }

    void show()
    {
        cout << "X: " << x << ", Y: " << y << endl;
    }

    void showZ()
    {
        cout << "Z: " << z;
    }

    void showAll()
    {
        show();
        showZ();
    }

    ~Test()
    {
        z--;
    }
};

int Test :: z=0;

int main()
{
    vector<Test> a(5);
    for (int i = 1; i <= 5; i++)
    {
        a[i-1].SetData(i,i*10);
    }
    Test mx = a[0];
    int Obj=1;
    for (int i = 1; i < a.size(); i++)
    {
        if (a[i].GetY() > mx.GetY())
        {
            mx = a[i];
            Obj=i+1;
        }
    }
    cout << "Max Y is in object " << Obj << " which is : " << mx.GetY() << endl;
    int sum = 0;
    for (int i = 0; i < a.size(); i++)
    {
        sum += a[i].GetX();
    }
    cout << "Sum of all X: " << sum << endl;
    return 0;
}
```

**Output:**
![[Pasted image 20250614123550.png]]


# Problem Statement 2: 
Write a class A with two data member a and b. Now set the values of a and b of an object obj1 by a setter method SetData() and copy the values of a and b of obj1 to another object obj2 by using copy constructor.

**Source Code:**
```cpp
#include<bits/stdc++.h>
using namespace std;

class A
{
    int a,b;

    public:
    A()
    {
        a=0;
        b=0;
    }

    void SetData(int x, int y)
    {
        a=x;
        b=y;
    }
    
    A(const A &obj)
    {
        a=obj.a;
        b=obj.b;
    }

    void ShowData()
    {
        cout << "A: " << a << ", B: " << b << endl;
    }
};

int main()
{
    A obj1;
    int a,b;
    cout << "Input A: ";
    cin >> a;
    cout << "Input B: ";
    cin >> b;
    obj1.SetData(a,b);
    A obj2(obj1);
    cout << "Data in Onject 1: ";
    obj1.ShowData();
    cout << "Data in Onject 2: ";
    obj2.ShowData();
}
```

**Output**:
![[Pasted image 20250614123651.png]]

