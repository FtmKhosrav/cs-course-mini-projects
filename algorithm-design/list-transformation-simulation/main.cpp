#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n, s, e;
    cin >> n >> s >> e;

    // initialize list with all 1s
    vector<int> lst(n, 1);

    // repeat until all elements become 0 or 1
    while (true) {

        bool stable = true;

        vector<int> new_lst = lst;

        for (int i = 0; i < n; i++) {

            if (lst[i] != 0 && lst[i] != 1) {

                int x = lst[i];

                int left = (i == 0) ? 0 : lst[i - 1];
                int right = (i == n - 1) ? 0 : lst[i + 1];

                // rule 1
                if (x % 2 == 0 && left == x / 2 && right == x / 2) {
                    new_lst[i] = x / 2;
                }

                // rule 2
                else if (left == x - 1 && right == x + 1) {
                    new_lst[i] = x - 1;
                }

                // rule 3
                else if (left == x + 1 && right == x - 1) {
                    new_lst[i] = x + 1;
                }

                stable = false;
            }
        }

        lst = new_lst;

        if (stable) break;
    }

    // count 1s in range [s, e]
    int count_ones = 0;

    for (int i = s - 1; i < e; i++) {
        if (lst[i] == 1) {
            count_ones++;
        }
    }

    cout << count_ones << endl;

    return 0;
}
