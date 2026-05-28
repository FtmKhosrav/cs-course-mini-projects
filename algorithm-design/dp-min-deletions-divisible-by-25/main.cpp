#include <iostream>
#include <vector>
#include <string>
#include <climits>

using namespace std;

int solve(string s) {

    int n = s.size();
    const int MOD = 25;

    // dp[i][r] = min deletions to get remainder r using first i digits
    vector<vector<int>> dp(n + 1, vector<int>(MOD, INT_MAX));

    dp[0][0] = 0;

    for (int i = 1; i <= n; i++) {

        int digit = s[i - 1] - '0';

        for (int r = 0; r < MOD; r++) {

            if (dp[i - 1][r] == INT_MAX) continue;

            // 1. delete this digit
            dp[i][r] = min(dp[i][r], dp[i - 1][r] + 1);

            // 2. keep this digit
            int new_r = (r * 10 + digit) % MOD;
            dp[i][new_r] = min(dp[i][new_r], dp[i - 1][r]);
        }
    }

    return dp[n][0];
}

int main() {

    int m;
    cin >> m;

    while (m--) {
        string n;
        cin >> n;
        cout << solve(n) << endl;
    }

    return 0;
}
