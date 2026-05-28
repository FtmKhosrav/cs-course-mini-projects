#include <iostream>
#include <vector>

using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {

        int n, m, k;
        cin >> n >> m >> k;

        // dp[i][j] = minimum cost required to reach cell (i, j)
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

        // Initialize first column
        for (int i = 2; i <= n; i++) {
            dp[i][1] = dp[i - 1][1] + 1;
        }

        // Initialize first row
        for (int j = 2; j <= m; j++) {
            dp[1][j] = dp[1][j - 1] + 1;
        }

        // Fill DP table
        for (int i = 2; i <= n; i++) {
            for (int j = 2; j <= m; j++) {

                // Cost if we move from top
                int from_top = dp[i - 1][j] + j;

                // Cost if we move from left
                int from_left = dp[i][j - 1] + i;

                // Choose minimum cost path
                dp[i][j] = min(from_top, from_left);
            }
        }

        // Check whether minimum cost equals target k
        if (dp[n][m] == k) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }

    return 0;
}