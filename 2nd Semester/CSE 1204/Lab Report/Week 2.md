# Problem #1

Write a Test class with proper data members and methods and do the following:
1. Initialize private data members **x** and **y** to 0 when empty constructor is called
2. Initialize private data members **x** and **y** using parameterized constructor
3. Initialize private data members **x** and **y** from another object using copy constructor
4. The data member **z** keeps track of total objects created
5. Write a method to initialize **x** and **y**
6. Write a method to display data member **z** only
7. Write a method to display **x**, **y** and **z** where their values can't be changed
8. Create five objects
9. Find the sum of **x**
10. Find the object number whose **y** value is maximum
11. Write destructor

**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

class Test {
private:
    int x;
    int y;
    static int z;

public:
    // empty constructor
    Test(){
        x = 0, y = 0;
        z++;
    }
    // parameterized constructor
    Test(int x, int y){
        this->x = x;
        this->y = y;
        z++;
    }
    // copy constructor
    Test(const Test& other): x(other.x), y(other.y) {
        this->x = x;
        this->y = y;
        z++;
    }
    // method to initialize x and y
    void Init(int x, int y){
        this->x = x;
        this->y = y;
    }
    // method to return x
    int GetX(){
        return x;
    }
    // method to return y
    int GetY(){
        return y;
    }
    // method to get z
    void ShowZ(){
        cout << "z = " << z << "\n";
    }
    // method to display x, y, z where values can't be changed
    void Display() const {
        cout << "x = " << x << "\n";
        cout << "y = " << y << "\n";
        cout << "z = " << z << "\n";
    }
    // destructor
    ~Test(){
        z--;
    }
};

int Test::z = 0;

int get_sum_x(vector<Test> &tests){
    int res = 0;
    for (int i = 0, sz = tests.size(); i < sz; i++){
        res += tests[i].GetX();
    }
    return res;
}

pair<int, int> get_max_y(vector<Test> &tests){
    pair<int, int> res = {-1, INT_MIN};
    for (int i = 0, sz = tests.size(); i < sz; i++){
        if (tests[i].GetY() > res.second){
            res.second = tests[i].GetY();
            res.first = i + 1;
        }
    }
    return res;
}

int main(){
    srand(time(NULL));
    int n = 5, x, y;
    vector<Test> tests(n);
    for (int i = 1; i <= n; i++){
        x = rand() % 100;
        y = rand() % 100;
        tests[i - 1].Init(x, y);
        cout << "Object " << i << "\n";
        tests[i - 1].Display();
    }

    cout << "Summation of x -> " << get_sum_x(tests) << "\n";
    pair<int, int> mxy = get_max_y(tests);
    cout << "Object " << mxy.first << " has the maximum y which is " << mxy.second << "\n";
    return 0;
}
```

**Input and Output:**
```
Object 1
x = 15
y = 71
z = 5
Object 2
x = 7
y = 0
z = 5
Object 3
x = 68
y = 79
z = 5
Object 4
x = 45
y = 17
z = 5
Object 5
x = 29
y = 10
z = 5
Summation of x -> 164
Object 3 has the maximum y which is 79
```


# Problem #2

Write a class A with two data member **a** and **b**. Now set the values of **a** and **b** of an object **obj1** by a setter method **SetData()** and copy the values of **a** and **b** of **obj1** to another object **obj2** by using copy constructor.

**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

class A {
private:
    int a, b;

public:
    // empty constructor
    A(){
        a = 0;
        b = 0;
    }

    // copy constructor
    A(const A &other): a(other.a), b(other.b){
        this->a = a;
        this->b = b;
    }

    // setter
    void SetData(int a, int b){
        this->a = a;
        this->b = b;
    }

    // getter
    void ShowData(){
        cout << "a = " << a << "\n";
        cout << "b = " << b << "\n";
    }
};


int main(){
    A obj1;
    int a, b;
    cout << "Input a -> ";
    cin >> a;
    cout << "Input b -> ";
    cin >> b;
    obj1.SetData(a, b);
    A obj2(obj1);

    cout << "Object 1 Data\n";
    obj1.ShowData();
    cout << "Object 2 Data\n";
    obj2.ShowData();

    return 0;
}
```


**Input and Output:**
```
Input a -> 10
Input b -> 31
Object 1 Data
a = 10
b = 31
Object 2 Data
a = 10
b = 31
```