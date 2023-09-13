#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const string secret = "5ecR3t_s7r1n9";

int main(int argc, char** argv) {
    if (argc != 2) {
        cout << "Usage: " << argv[0] << " <password>" << endl;
        return 1;
    }
    string input = string(argv[1]);
    bool flag = true;

    for (int i = 0; i < min(secret.length(), input.length()); ++i) {
        if (secret[i] != input[i]) {
            flag = false;
        }
    }

    if (flag) {
        cout << "Correct!" << endl;
        return 0;
    }
    else {
        cout << "Wrong!" << endl;
        return 1;
    }
}
