# Problem #1

Write a Circle class with proper data members and methods and do the following:
1. Initialize Radius of 3 circles
2. Find area of all of them
3. Find the total area

**Source Code:**
```cpp 
#include <bits/stdc++.h>

using namespace std;

const double pi = 3.14159;

class Circle {
    int radius;
    float area;
public:
    void SetRadius(int radius){
        this->radius = radius;
        area = pi * radius * radius;
    }
    float GetArea(){
        return area;
    }
};

int main(){
    vector<Circle> circles(3);
    int radius;
    double total_area = 0;
    for (int i = 1; i <= 3; i++){
        cout << "Enter the radius of circle " << i << ": ";
        cin >> radius;
        circles[i - 1].SetRadius(radius);
    }
    for (int i = 0; i < 3; i++){
        cout << "The area of circle " << i + 1 << " = " << circles[i].GetArea() << "\n";
        total_area += circles[i].GetArea();
    }
    cout << "Total area of all the circles combined = " << total_area << "\n";
    return 0;
}

```

**Input:**
```
Enter the radius of circle 1: 2
Enter the radius of circle 2: 3
Enter the radius of circle 3: 4
```

**Output:**
```
The area of circle 1 = 12.5664
The area of circle 2 = 28.2743
The area of circle 3 = 50.2654
Total area of all the circles combined = 91.1061
```



# Problem #2

Write a Triangle class with 3 edges as data members and methods and do the following:
1. Initialize edges of a triangle
2. Find area of the triangle
3. Check whether the 3 edges form a triangle


**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

class Triangle{
    int edge1;
    int edge2;
    int edge3;
    float area;
public:
    void SetEdges(int e1, int e2, int e3){
        edge1 = e1;
        edge2 = e2;
        edge3 = e3;
        float s = (e1 + e2 + e3) / 2.0;
        if (s - e1 > 0 && s - e2 > 0 && s - e3 > 0)
            area = sqrt(s * (s - e1) * (s - e2) * (s - e3));
        else
            area = 0;
    }
    bool IsValidTriangle(){
        vector<int> edges = {edge1, edge2, edge3};
        sort(edges.begin(), edges.end());
        if (edges[0] + edges[1] > edges[2]) return true;
        else return false;
    }
    float GetArea(){
        return area;
    }
};

int main(){
    int e1, e2, e3;
    vector<Triangle> triangles(3);
    for (int i = 0; i < 3; i++){
        cout << "Enter three edges of triangle " << i + 1 << ": ";
        cin >> e1 >> e2 >> e3;
        triangles[i].SetEdges(e1, e2, e3);
    }
    for (int i = 0; i < 3; i++){
        cout << "\n";
        if (triangles[i].IsValidTriangle()){
            cout << "Triangle " << i + 1 << " is a valid triangle\n";
            cout << "Area = " << triangles[i].GetArea() << "\n";
        }
        else {
            cout << "Triangle " << i + 1 << " is not a valid triangle\n";
        }
    }
    return 0;
}
```


**Input:**
```
Enter three edges of triangle 1: 6 7 8
Enter three edges of triangle 2: 2 2 5
Enter three edges of triangle 3: 8 10 6

```

**Output:**
```
Triangle 1 is a valid triangle
Area = 20.3332

Triangle 2 is not a valid triangle

Triangle 3 is a valid triangle
Area = 24
```

# Problem #3

Write a Account class with 2 data members and methods and do the following:
1. Initialize 5 accounts
2. Deposit money to an account
3. Withdrawal money from an account
4. Transfer money from one account to another

**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

class Account{
    int number;
    int amount;
public:
    void SetData(int number, int amount){
        this->number = max(number, 0);
        this->amount = amount;
    }
    int GetBalance(){
        return amount;
    }
    void AddBalance(int delta){
        amount += delta;
    }
};

int Total = 0;
vector<Account> accounts;

void Create(){
    int balance;
    Account nw;
    cout << "Your new account number is: " << ++Total << "\n";
    cout << "Enter initial balance -> ";
    cin >> balance;
    nw.SetData(Total, balance);
    accounts.push_back(nw);
    cout << "Congratulations! Your account have been created successfully\n";
}

void Deposit(){
    int n, amount;
    cout << "Enter your account number -> ";
    cin >> n;
    if (n < 1 || n > Total){
        cout << "Invalid account number! Please try again.\n";
        return;
    }
    cout << "Enter deposit amount -> ";
    cin >> amount;
    accounts[n - 1].AddBalance(amount);
    cout << "Successfully completed deposit\n";
    cout << "Your new balance is " << accounts[n - 1].GetBalance() << "\n";
}

void Withdraw(){
    int n, amount;
    cout << "Enter your account number -> ";
    cin >> n;
    if (n < 1 || n > Total){
        cout << "Invalid account number! Please try again.\n";
        return;
    }
    cout << "Enter withdraw amount -> ";
    cin >> amount;
    if (amount > accounts[n - 1].GetBalance()){
        cout << "Not sufficient balance!!!\n";
        cout << "Withdrawal canceled\n";
        return;
    }
    accounts[n - 1].AddBalance(-amount);
    cout << "Successfully completed withdrawal\n";
    cout << "Your new balance is " << accounts[n - 1].GetBalance() << "\n";
}

void FundTransfer(){
    int sender, receiver, amount;
    cout << "Enter your account number -> ";
    cin >> sender;
    if (sender < 1 || sender > Total){
        cout << "Invalid account number! Please try again.\n";
        return;
    }
    cout << "Enter amount to transfer -> ";
    cin >> amount;
    if (amount > accounts[sender - 1].GetBalance()){
        cout << "Insufficient balance\n";
        cout << "Fund transfer canceled\n";
        return;
    }
    cout << "Enter recipients account number -> ";
    cin >> receiver;
    if (receiver < 1 || receiver > Total || receiver == sender){
        cout << "Invalid account number! Please try again.\n";
        return;
    }
    accounts[sender - 1].AddBalance(-amount);
    accounts[receiver - 1].AddBalance(amount);
    cout << "Your new balance is " << accounts[sender - 1].GetBalance() << "\n";
}

void ShowBalance(){
    int n;
    cout << "Enter your account number -> ";
    cin >> n;
    if (n < 1 || n > Total){
        cout << "Invalid account number! Please try again.\n";
        return;
    }
    cout << "Your balance is " << accounts[n - 1].GetBalance() << "\n";
}

int main(){
    int option;
    cout << "\n <===Menu===>\n";
    cout << " 1. Create\n";
    cout << " 2. Deposit\n";
    cout << " 3. Withdraw\n";
    cout << " 4. Fund Transfer\n";
    cout << " 5. Show Balance\n";
    cout << " 6. Exit\n";
    while(true){
        cout << " Enter option(1 - 6): ";
        cin >> option;

        if (option == 6) break;
        switch(option){
            case(1): Create(); break;
            case(2): Deposit(); break;
            case(3): Withdraw(); break;
            case(4): FundTransfer(); break;
            case(5): ShowBalance(); break;
            default: cout << "Invalid Command\n";
        }
    }
    return 0;
}
```

**Input and Output**:

1. Initializing 5 accounts:
```
<===Menu===>
 1. Create
 2. Deposit
 3. Withdraw
 4. Fund Transfer
 5. Show Balance
 6. Exit
 Enter option(1 - 6): 1
Your new account number is: 1
Enter initial balance -> 100
Congratulations! Your account have been created successfully
 Enter option(1 - 6): 1
Your new account number is: 2
Enter initial balance -> 200
Congratulations! Your account have been created successfully
 Enter option(1 - 6): 1
Your new account number is: 3
Enter initial balance -> 300
Congratulations! Your account have been created successfully
 Enter option(1 - 6): 1
Your new account number is: 4
Enter initial balance -> 400
Congratulations! Your account have been created successfully
 Enter option(1 - 6): 1
Your new account number is: 5
Enter initial balance -> 500
Congratulations! Your account have been created successfully

```

2. Deposit money to an account
```
 Enter option(1 - 6): 2
Enter your account number -> 3
Enter deposit amount -> 1000
Successfully completed deposit
Your new balance is 1300
```

3. Transfer money from one account to another
```
 Enter option(1 - 6): 4
Enter your account number -> 3
Enter amount to transfer -> 100
Enter recipients account number -> 5
Your new balance is 1200
```

4. Withdrawal money from an account
```
 Enter option(1 - 6): 3
Enter your account number -> 5
Enter withdraw amount -> 150
Successfully completed withdrawal
Your new balance is 450
 Enter option(1 - 6): 6
```


# Problem #4

Write a C/C++ program for processing the Gym data using the following constraints:
1. Store ID, Height and Weight of each member
2. A member can be added/removed/updated
3. The should be menu operated
4. Define a structure with data members ID, Height and Weight.
5. Calculate average Height of the members
6. Calculate average Weight of the members
7. Calculate Max Height and Weight
8. Calculate Min Height and Weight
9. Display BMI classification of a given member

**Source Code:**
```cpp
#include <bits/stdc++.h>

using namespace std;

class Member {
    int id;
    float height, weight, bmi;
public:
    void SetNewData(int id, float height, float weight){
        this->id = id;
        this->height = height;
        this->weight = weight;
        bmi = weight / (height * height);
    }
    void SetData(float height, float weight){
        this->height = height;
        this->weight = weight;
        bmi = weight / (height * height);
    }
    float GetHeight(){
        return height;
    }
    float GetWeight(){
        return weight;
    }
    float GetBMI(){
        return bmi;
    }
};

map<int, Member> members;

void AddMember(){
    int id;
    cout << "Enter Member ID -> ";
    cin >> id;
    if (members.find(id) != members.end()){
        cout << "ID already exists. Please try again with a new ID\n";
        return;
    }
    float height, weight;
    cout << "Enter height (m) -> ";
    cin >> height;
    cout << "Enter weight (kg) -> ";
    cin >> weight;
    if (height <= 0 || weight <= 0){
        cout << "Invalid height or/and weight. Please try again\n";
        return;
    }
    members[id].SetNewData(id, height, weight);
    cout << "New Member Created Successfully!\n";
}

void UpdateMember(){
    int id;
    cout << "Enter Member ID -> ";
    cin >> id;
    if (members.find(id) == members.end()){
        cout << "ID does not exist. Please try again\n";
        return;
    }
    float height, weight;
    cout << "Enter New Height -> ";
    cin >> height;
    cout << "Enter New Weight -> ";
    cin >> weight;
    if (height <= 0 || weight <= 0){
        cout << "Invalid height or/and weight. Please try again\n";
        return;
    }
    members[id].SetData(height, weight);
    cout << "Mebmer Updated Successfully\n";
}

void RemoveMember(){
    int id;
    cout << "Enter Member ID -> ";
    cin >> id;
    if (members.find(id) == members.end()){
        cout << "ID does not exist. Please try again\n";
        return;
    }
    members.erase(id);
    cout << "Member Deleted Successfully!\n";
}

void GetMemberInfo(){
    int id;
    cout << "Enter Member ID -> ";
    cin >> id;
    if (members.find(id) == members.end()){
        cout << "ID does not exist. Please try again\n";
        return;
    }
    Member cur = members[id];
    cout << "\nMember Information\n";
    cout << "Height -> " << cur.GetHeight() << " m\n";
    cout << "Weight -> " << cur.GetWeight() << " kg\n";
    cout << "BMI    -> " << cur.GetBMI() << "\n";
}

void GetMaxHeightWeight(){
    float mxheight = 0, mxweight = 0;
    if (!members.size()){
        cout << "No member in database\n";
        return;
    }
    for (auto itr = members.begin(); itr != members.end(); itr++){
        mxheight = max(mxheight, itr->second.GetHeight());
        mxweight = max(mxweight, itr->second.GetWeight());
    }
    cout << "Max Height -> " << mxheight << " m\n";
    cout << "Max Weight -> " << mxweight << " kg\n";
}

void GetMinHeightWeight(){
    float mnheight = 100, mnweight = 1000;
    if (!members.size()){
        cout << "No member in database\n";
        return;
    }
    for (auto itr = members.begin(); itr != members.end(); itr++){
        mnheight = min(mnheight, itr->second.GetHeight());
        mnweight = min(mnweight, itr->second.GetWeight());
    }
    cout << "Min Height -> " << mnheight << " m\n";
    cout << "Min Weight -> " << mnweight << " kg\n";
}

void GetAverageHeightWeight(){
    float heightsum = 0, weightsum = 0;
    int sz = members.size();
    if (!sz){
        cout << "No member in database\n";
        return;
    }
    for (auto itr = members.begin(); itr != members.end(); itr++){
        heightsum += itr->second.GetHeight();
        weightsum += itr->second.GetWeight();
    }
    cout << "Average Height -> " << heightsum / sz << " m\n";
    cout << "Average Weight -> " << weightsum / sz << " kg\n";
}

void GetBMI(){
    int id;
    cout << "Enter Member ID -> ";
    cin >> id;
    if (members.find(id) == members.end()){
        cout << "ID does not exist. Please try again\n";
        return;
    }
    float bmi = members[id].GetBMI();
    cout << "BMI  -> " << bmi << "\n";
    cout << "Type -> ";
    if (bmi < 16) cout << "Severe Thinness\n";
    else if (bmi < 17) cout << "Moderate Thinness\n";
    else if (bmi < 18.5) cout << "Mild Thinness\n";
    else if (bmi < 25) cout << "Normal\n";
    else if (bmi < 30) cout << "Overweight\n";
    else if (bmi < 35) cout << "Obese Class I\n";
    else if (bmi < 40) cout << "Obese Class II\n";
    else cout << "Obese Class III\n";
}

int main(){
    int option;
    while (true){
        cout << "\n********** Main Menu ********\n\n";
        cout << "  1. Add Member\n";
        cout << "  2. Update Member\n";
        cout << "  3. Remove Member\n";
        cout << "  4. Member Information\n";
        cout << "  5. Max Height & Weight\n";
        cout << "  6. Min Height & Weight\n";
        cout << "  7. Average Height & Weight\n";
        cout << "  8. BMI Classification\n";
        cout << "  9. Exit\n";
        cout << "     Enter your option(1-9): ";
        cin >> option;
        if (option == 9) break;
        cout << "\n";
        switch(option){
            case(1): AddMember(); break;
            case(2): UpdateMember(); break;
            case(3): RemoveMember(); break;
            case(4): GetMemberInfo(); break;
            case(5): GetMaxHeightWeight(); break;
            case(6): GetMinHeightWeight(); break;
            case(7): GetAverageHeightWeight(); break;
            case(8): GetBMI(); break;
            default: cout << "Invalid Command\n";
        }
    }
    return 0;
}
```

**Input and Output:**

1. Main Menu and Storing Information of members:
```
********** Main Menu ********

  1. Add Member
  2. Update Member
  3. Remove Member
  4. Member Information
  5. Max Height & Weight
  6. Min Height & Weight
  7. Average Height & Weight
  8. BMI Classification
  9. Exit
     Enter your option(1-9): 1

Enter Member ID -> 202501
Enter height (m) -> 1.55
Enter weight (kg) -> 65
New Member Created Successfully!

Enter Member ID -> 202502
Enter height (m) -> 1.65
Enter weight (kg) -> 40
New Member Created Successfully!

Enter Member ID -> 202401
Enter height (m) -> 1.88
Enter weight (kg) -> 110
New Member Created Successfully!
```

2. Updating Member:
```
     Enter your option(1-9): 2

Enter Member ID -> 202401
Enter New Height -> 1.88
Enter New Weight -> 104
Member Updated Successfully
```

3. Deleting Member
```
     Enter your option(1-9): 3

Enter Member ID -> 202502
Member Deleted Successfully!
```

4. Calculating Average Height and Weight
```
     Enter your option(1-9): 7

Average Height -> 1.74 m
Average Weight -> 90.3333 kg
```

5. Calculating Max Height and Weight
```
     Enter your option(1-9): 5

Max Height -> 1.88 m
Max Weight -> 104 kg
```

6. Calculating Min Height and Weight
```
     Enter your option(1-9): 6

Min Height -> 1.55 m
Min Weight -> 65 kg
```

7. BMI Classification
```
     Enter your option(1-9): 8

Enter Member ID -> 202401
BMI  -> 29.4251
Type -> Overweight

     Enter your option(1-9): 8

Enter Member ID -> 202502
BMI  -> 31.8342
Type -> Obese Class I
```