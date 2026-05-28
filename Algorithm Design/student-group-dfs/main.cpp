#include <iostream>
#include <vector>

using namespace std;

// DFS function to explore connected components
void dfs(int node,
         vector<vector<int>>& graph,
         vector<int>& visited,
         vector<int>& group,
         int group_id) {

    visited[node] = 1;      // mark node as visited
    group[node] = group_id; // assign group ID

    // visit all neighbors
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, graph, visited, group, group_id);
        }
    }
}

int main() {
    int n;
    cin >> n;

    // supervisors[i] = supervisor of student i (0 means none)
    vector<int> supervisors(n);

    for (int i = 0; i < n; i++) {
        cin >> supervisors[i];
    }

    // build graph (undirected)
    vector<vector<int>> graph(n);

    for (int i = 0; i < n; i++) {
        if (supervisors[i] > 0) {
            int v = supervisors[i] - 1;

            graph[i].push_back(v);
            graph[v].push_back(i);
        }
    }

    vector<int> visited(n, 0);
    vector<int> group(n, -1);

    int group_id = 0;

    // find connected components
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, graph, visited, group, group_id);
            group_id++;
        }
    }

    // compute group sizes
    vector<int> group_size(group_id, 0);

    for (int i = 0; i < n; i++) {
        group_size[group[i]]++;
    }

    // output result
    int min_groups = 0;

    for (int i = 0; i < group_id; i++) {
        min_groups += max(1, group_size[i]);
    }

    cout << min_groups << endl;

    return 0;
}
