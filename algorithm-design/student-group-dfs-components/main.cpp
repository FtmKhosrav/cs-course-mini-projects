#include <iostream>
#include <vector>

using namespace std;

void dfs(int node,
         vector<vector<int>>& graph,
         vector<int>& visited,
         vector<int>& component,
         int id) {

    visited[node] = 1;
    component[node] = id;

    for (int next : graph[node]) {
        if (!visited[next]) {
            dfs(next, graph, visited, component, id);
        }
    }
}

int main() {

    int n;
    cin >> n;

    vector<int> supervisor(n);

    for (int i = 0; i < n; i++) {
        cin >> supervisor[i];
    }

    // build graph
    vector<vector<int>> graph(n);

    for (int i = 0; i < n; i++) {
        if (supervisor[i] > 0) {
            int v = supervisor[i] - 1;
            graph[i].push_back(v);
            graph[v].push_back(i);
        }
    }

    vector<int> visited(n, 0);
    vector<int> component(n, -1);

    int group_id = 0;

    // find connected components using DFS
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, graph, visited, component, group_id);
            group_id++;
        }
    }

    // each component represents a group
    cout << group_id << endl;

    return 0;
}
