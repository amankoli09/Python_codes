#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main() {
    string str;
    if (!getline(cin, str)) return 0;
    stringstream ss(str);
    long long value;
    char extra;
    if ((ss >> value) && !(ss >> extra)) {
        cout << value << endl;
    } else {
        cout << str << endl;
    }
    return 0;
}
