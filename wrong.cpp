#include <iostream>
#include <string>

using namespace std;

const string secret = "5ecR3t_s7r1n9";

int main(int argc, char** argv) {
    if (argc != 2) {
        cout << "Usage: " << argv[0] << " <password>" << endl;
        return 1;
    }
    string input = string(argv[1]);

    if (secret.length() != input.length()) {
        cout << "Wrong!" << endl;
        return 1;
    }

    for (int i = 0; i < input.length(); ++i) {
        if (secret[i] != input[i]) {
            cout << "Wrong!" << endl;
            return 1;
        }
    }

    cout << "Correct!" << endl;
    return 0;
}
