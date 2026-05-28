#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    // reports[i] = player reported by player (i+1)
    vector<int> reports(n);

    for (int i = 0; i < n; i++) {
        cin >> reports[i];
    }

    // red_cards:
    // 0 = not processed
    // 1 = starting/reporting player
    // 2 = final player in the chain
    vector<int> red_cards(n, 0);

    // Traverse each player
    for (int i = 0; i < n; i++) {

        int player = i + 1;

        // Follow reporting chain until we reach a processed node
        while (red_cards[player - 1] == 0) {

            int reported_by = reports[player - 1];

            // If next player in chain is not processed, continue traversal
            if (red_cards[reported_by - 1] == 0) {
                player = reported_by;
            }
            else {
                // Mark starting player
                red_cards[i] = 1;

                // Mark final affected player in the chain
                red_cards[player - 1] = 2;

                break;
            }
        }
    }

    // Output result
    for (int i = 0; i < n; i++) {
        cout << red_cards[i] << " ";
    }

    cout << endl;

    return 0;
}
