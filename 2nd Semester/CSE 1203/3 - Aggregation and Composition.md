
# Aggregation 

```cpp
#include <bits/stdc++.h>

using namespace std;

class Employee {
    string ename;
public:
    // constructor
    Employee(string s){
        ename = s;
        cout << "Employee " << s << " constructor\n" ;
    }

    // setter
    void SetName(string s){
        ename = s;
    }

    // getter
    string GetName(){
        return ename;
    }

    // destructor
    ~Employee(){
        cout << "Employee: " << ename << " destroyed\n";
    }
};

class Company {
    string cname;
    Employee *emp;
public:
    Company(string s, Employee *p){
        cname = s;
        emp = p;
        cout << "Company " << s << " constructor\n";
    }
    void Display(){
        cout << "Company: " << cname << "\n\t-> Employee Name: " << emp->GetName() << "\n";
    }
    ~Company(){
        cout << "Company " << cname << " destroyed\n";
    }

};

int main(){

    Employee e("Kamal");

    cout << "1. " << e.GetName() << "\n";
    {
        Company c("HP", &e);
        c.Display();
    }

    cout << "2. " << e.GetName() << "\n";

    return 0;
}
```


# Composition

```cpp
#include <bits/stdc++.h>

using namespace std;

class Birthdate {

    int day, month, year;
public:
    Birthdate(int x = 0, int y = 0, int z = 0){
        cout << "Birthdate constructor called\n";
        day = x;
        month = y;
        year = z;
    }
    void SetData(int x, int y, int z){
        day = x;
        month = y;
        year = z;
    }
    void Display(){
        cout << "Date of Birth: " << day << "/" << month << "/" << year << "\n";
    }
    ~Birthdate(){
        cout << "Birthdate is destroyed\n";
    }
};

class Person {
    string name;
    Birthdate dt;
public:
    Person(string s, int d, int m, int y){
        cout << "Person constructor called\n";
        name = s;
        dt.SetData(d, m, y);
    }

    void Display(){
        cout << name << "\n";
        dt.Display();
    }


    ~Person(){
        cout << "Person is dead\n";
    }

};

int main(){

    Person p("Kamal", 12, 5, 2006);
    p.Display();

    return 0;
}
```