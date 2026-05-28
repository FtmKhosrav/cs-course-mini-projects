#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

    string s;
    cin >> s;

    int n = s.length();

    // dp[i] = computed value up to index i
    vector<int> dp(n, 0);

    dp[0] = 0;

    // Build DP array
    for (int i = 2; i < n; i += 2) {

        // If two adjacent characters are equal
        if (s[i] == s[i - 1]) {
            dp[i] = dp[i - 2] + i;
        }
        else {
            dp[i] = dp[i - 1];
        }
    }

    int m;
    cin >> m;

    // Answer queries
    while (m--) {

        int a, b;
        cin >> a >> b;

        int result = dp[b - 1] - dp[a - 1];

        cout << result << endl;
    }

    return 0;
}
