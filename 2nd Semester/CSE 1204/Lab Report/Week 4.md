# Problem 1
**Topic 1:** : Define a class Test where overload a method Sum() to sum numbers sent from main() function.

**Source Code:**
```cpp
#include<bits/stdc++.h>

using namespace std;

class Test {
public:

    template <typename T1>
    void Sum(T1 x){
        cout << "Sum = " << x << "\n";
    }

    template <typename T1, typename T2>
    void Sum(T1 x, T2 y){
        cout << "Sum = " << x + y << "\n";
    }
};

int main(){
    Test t;
    t.Sum(10);
    t.Sum(10, 20);
    t.Sum(5.7, 20);
    t.Sum(10, 2.6);
    t.Sum(10.5, 20.7);
    return 0;
}
```

**Input and Output:**
```
Sum = 10
Sum = 30
Sum = 25.7
Sum = 12.6
Sum = 31.2
```


# Problem 2

**Statement:** Suppose in a AC circuit, there are 3 impedances z1=3+j4, z2=4-j3 and z3=j6 are connected in parallel. Now find the current in the circuit if input voltage is 100+j50. Implement operator overloading concept for your calculation. Use class Circuit and initialize the impedance values (real & img) by a constructor.

**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

class Circuit{
private:
    double real;
    double img;
public:
    // Write Constructor
    Circuit() : real(0), img(0){}
    Circuit(double x, double y) : real(x), img(y){}

    // Write Operator Overloaded Method
    Circuit operator+(Circuit &other){
        return {real + other.real, img + other.img};
    }

    Circuit operator-(Circuit &other){
        return {real - other.real, img - other.img};
    }

    Circuit operator*(Circuit &other){
        return {real * other.real - img * other.img, real * other.img + other.real * img};
    }

    Circuit operator/(Circuit &other){
        double sqr = other.real * other.real + other.img * other.img;
        Circuit second = {other.real / sqr, -other.img / sqr};
        return (*this) * second;
    }

    //write a display method to display real and img
    void Display(){
        if (img >= 0) cout << real << " + j" << img;
        else cout << real << " - j" << -img;
    }
};

int main(){
    Circuit z1(3, 4), z2(4, -3), z3(0, 6), v(100, 50), one(1, 0);

    // Finding reciprocal of all the loads
    Circuit I1 = (one / z1);
    Circuit I2 = (one / z2);
    Circuit I3 = (one / z3);

    // Adding reciprocal of all the loads
    Circuit z = I1 + I2 + I3;

    // Finding equivalent impedance
    z = (one / z);

    // Calculating current
    Circuit I = (v / z);

    // Showing result
    cout << "The current is ";
    I.Display();
    cout << " Ampere\n";
    return 0;
}
```

**Input and Output:**
```
The current is 38.3333 - j6.66667 Ampere
```


# Problem 3
**Statement:** : Write a program using unary operator overloading to control the sound of a TV remote. If ‘+’ button is pressed then sound increases and if ‘-‘ button pressed then sound decreases.

**Source Code:**
```cpp
#include<bits/stdc++.h>

using namespace std;

class Remote {
    int sound;
public:
    Remote(int sound = 0){
        this->sound = sound;
    }

    void Display(){
        cout << "Current Sound Level = " << sound << "\n";
    }

    // Operator Overloading
    Remote operator++(int){
        Remote ret = *this;
        if (sound < 100) sound++;
        return ret;
    }

    Remote operator--(int){
        Remote ret = *this;
        if (sound > 0) sound--;
        return ret;
    }

    Remote operator++() {
        if (sound < 100) sound++;
        return *this;
    }

    Remote operator--() {
        if (sound > 0) sound--;
        return *this;
    }
};

int main(){

    Remote rs(99);
    (rs++).Display();
    ++rs;
    rs.Display();
    rs--;
    --rs;
    rs.Display();

    return 0;
}
```

**Input and Output:**
```
Current Sound Level = 99
Current Sound Level = 100
Current Sound Level = 98
```


# Problem 4
**Statement:** Suppose your money is deposited in two banks through their private data members money1 and money2 respectively. Now based on the statements in main() function, write a program to calculate your total money using a friend function Sum().

**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

// class initialization for using friend function
class Bank2;

class Bank1 {
private:
    int money;
public:
    Bank1(int x = 0): money(x){}

    int GetMoney(){
        return money;
    }

    friend int Sum(Bank1 &b1, Bank2 &b2);
};

class Bank2 {
private:
    int money;
public:
    Bank2(int x = 0): money(x){}

    int GetMoney(){
        return money;
    }

    friend int Sum(Bank1 &b1, Bank2 &b2);
};

int Sum(Bank1 &b1, Bank2 &b2){
    return b1.GetMoney() + b2.GetMoney();
}


int main(){
    Bank1 b1(2000);
    Bank2 b2(4000);
    cout << "Bank1 Money = " << b1.GetMoney() << " bdt\n";
    cout << "Bank2 Money = " << b2.GetMoney() << " bdt\n";
    cout << "Total Sum = " << Sum(b1, b2) << " bdt\n";
    return 0;
}
```

**Input and Output:**
```
Bank1 Money = 2000 bdt
Bank2 Money = 4000 bdt
Total Sum = 6000 bdt
```
