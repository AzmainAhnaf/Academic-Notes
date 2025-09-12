
# Introduction

The word polymorphism means having many forms.

In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form.

Polymorphism is an important and basic concept of OOPS.

In C++, an operator or function can be given different meanings or functions.

In C++ polymorphism is mainly divided into two types;
- Compile Time Polymorphism (early binding / static polymorphism)
- Runtime Polymorphism (late binding / dynamic polymorphism)

![[Pasted image 20250722230838.png]]


# Function Overloading

- Function overloading means to have more than one function with the same name but with different parameters.
- Overloaded functions are differentiated by checking
	- Number of arguments
	- Type & sequence of arguments but not by return type of the function

An overloaded function must have
- Different type of parameters
- Different number of parameters
- Different sequence of parameters

for example:
```cpp
void print();
void print(int a);
void print(float a);
void print(int a, int b);
void print(int a, double b);
void print(double a, int b);
```

```cpp
#include<bits/stdc++.h>

using namespace std;

class A{
public:
	int Sum(int a, int b){
		return a + b;
	}

	double Sum(double a, double b){
        return a + b;
	}
};

int main(void){
    A a;
    cout << a.Sum(3, 4) << "\n";
    cout << a.Sum(2.5, 4.6) << "\n";
}
```

# Operator Overloading

- C++ allows us to specify more than one definition for an operator in the same scope, which is called operator overloading.
- We can redefine or overload most of the built-in operators in C++.
- It is a type of polymorphism in which an operator is overloaded to give user defined meaning to it.
- Almost any operator can be overloaded in C++. However there are few operator which can not be overloaded. Operator that are not overloaded are follow
	- Scope operator(::)
	- `sizeof`
	- Member selector(.)
	- Member pointer selector(*)
	- Ternary operator(?:)

## Binary Operator Overloading

```cpp
#include<bits/stdc++.h>

using namespace std;

class Complex {
private:
    int real, imag;
public:
    Complex(int r = 0, int i = 0){
        real = r;
        imag = i;
    }

    Complex operator+(Complex const &obj){
        Complex res;
        res.real = real + obj.real;
        res.imag = imag + obj.imag;
        return res;
    }

    void print(){
        cout << real << " +i" << imag << "\n";
    }
};

int main(){
    Complex c1(10, 5), c2(2, 4);
    Complex c3;
    c3 = c1 + c2;
    c3.print();
}
```

Operator functions are the same as normal functions. The only differences are, that the name of an operator function is always the **operator** keyword followed by the symbol of the operator and operator functions are called when the corresponding operator is used.


## Unary Operator Overloading

```cpp
#include <bits/stdc++.h>

using namespace std;

class Counter {
private:
    int count;
public:
    Counter() : count(0){}

    int get_count(){return count;}

    void operator++(){
        count++;
    }

};

int main(){
    Counter c;
    ++c;
    ++c;
    cout << "c = " << c.get_count() << "\n";
}
```

The operator function uses unary operator. Here ++ operator is used to increment the value of private member data count.


# Function Overriding

- If we inherit a class into the derived class and provide a definition for one of the base class's function again inside the derived class, then that function is said to be overridden, and this mechanism is called function overriding
- Inheritance should be there. Function overriding cannot be done within a class. For this we require a derived class and a base class.
- Function that is redefined must have exactly the same declaration in both base and derived class, that means same name, same return type and same parameter list
- If we create an object of the derived class and call the member function which exists in both the classes then member function in the derived class is invoked and the function in the base class is ignored.

```cpp
class Base {
public:
	void getData(){
		...
	}
};

class Derived: public Base {
public:
	void getData(){
		...
	}
};

int main(){
	Derived obj;
	obj.getData();
	// The function in the derived class will be called
}
```

```cpp
class Base {
public:
	void getData(){
		...
	}
};

class Derived: public Base {
public:
	void getData(){
		Base::getData();
	}
};

int main(){
	Derived obj;
	obj.getData();
	// The function in the Base class is called through the Derived class funtion
}
```

```cpp
#include <bits/stdc++.h>

using namespace std;

class A {
public:
    void Print(){
        cout << "Inside A\n";
    }
};

class B: public A {
public:
    void Print(){
        cout << "Inside B\n";
    }
};

int main(void){
    A a;
    a.Print();
    B b;
    b.Print();
}
```
Output
```
Inside A
Inside B
```

```cpp
#include <bits/stdc++.h>

using namespace std;

class A {
public:
    void Print(){
        cout << "Inside A\n";
    }
};

class B: public A {

};

int main(void){
    A a;
    a.Print();
    B b;
    b.Print();
}
```
Output
```
Inside A
Inside A
```

# Virtual Function & Polymorphism

- Polymorphism means same action but different reaction or reply.
- In C++, polymorphism, refers to the property by which objects belonging to different classes are able to respond to the same message, but in different forms
- Polymorphism is also known as late binding / dynamic binding / run-time binding
- In C++, two things are require to achieve polymorphism
	- A virtual function in the base class
	- A pointer of the base class
- The function in the base class is declared as virtual by using the keyword virtual preceding its normal declaration
- When a function is made virtual, C++ determines which function to use at runtime based on the type of the object pointed to by the base pointer.

```cpp
#include <bits/stdc++.h>

using namespace std;

class A{
public:
    virtual void Print(){
        cout << "Inside A\n";
    }
};

class B: public A{
public:
    void Print(){
        cout << "Inside B\n";
    }
};

int main(void){
    A *pa;
    A a;
    pa = &a;
    pa->Print();
    B b;
    pa = &b;
    pa->Print();
}
```

Here pa is the pointer to base class. First it points to base class of object a. So `pa->Print()` calls base class method

After that pa is assigned to B class object b. So `pa->Print()` called derived class method

As the address generates at runtime the statement `pa = &b` will be executed at runtime which ultimately creates run-time calling (dynamic binding) so a base class pointer can point to any derived class objects at run-time.

## Rules of Virtual Function

- The virtual functions should not be static
- It must be member of some class
- A virtual function can be declared as friend for another class.
- Constructors cannot be declared as virtual, but destructors can be declared as virtual.
- They can be accessed by using pointer object
- The prototype of the base class version of virtual function and derived class function prototype must be identical
- Base pointer can point to any type of derived object but derived pointer can not point to base class object
- If virtual function is defined in base class, it is need not be redefine in derived class.


# Pure Virtual Function & Abstract Class

- Sometimes implementation of all functions cannot be provided in a base class because we don't know the implementation. Such a class is called abstract class.
- A pure virtual function (or abstract function) in C++ is a virtual function for which we don't have any implementation, we only declare it. A pure virtual function is declared by assigning 0 in declaration.
- Some important facts
	- A class is abstract if it has at least one pure virtual function.
	- We can have pointers and references of abstract class type
	- If we do not override the pure virtual function in derived class, then derived class also becomes abstract class
	- Abstract classes cannot be instantiated.
- A pure virtual function is used to make a class abstract
- An abstract class is such a class whose object cannot be created
- A virtual function is made **pure virtual** by assigning 0 to the function name. Such a function is also known as 'do-nothing' function
- `virtual void Show() = 0;`

```cpp
#include <bits/stdc++.h>

using namespace std;

class Shape {
public:
    virtual void getArea()=0;
};

class Circle: public Shape {
public:
    void getArea(){
        cout << "Enter circle readius -> ";
        int r;
        cin >> r;
        cout << "Area of circle is: " << (3.14 * r * r) << "\n";
    }
};

class Rectangle: public Shape {
public:
    void getArea(){
        cout << "Enter Length & Breadth -> ";
        int l, b;
        cin >> l >> b;
        cout << "Area of rectangle is: " << (l * b) << "\n";
    }
};

int main(){
    Shape *shape;
    Circle c;
    Rectangle r;
    shape = &c;
    shape->getArea();
    shape = &r;
    shape->getArea();
}
```