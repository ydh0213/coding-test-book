#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int N, arr[11], minAns = 1e9, maxAns = -1e9;
vector<int> v;

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) scanf("%d", &arr[i]);

    int op;
    for (int i = 0; i < 4; ++i) {
        scanf("%d", &op);
        for (int j = 0; j < op; ++j) v.emplace_back(i);
    }

    do {
        int res = arr[0];
        for (int i = 0; i < N - 1; ++i)
            if (v[i] == 0) res += arr[i + 1];
            else if (v[i] == 1) res -= arr[i + 1];
            else if (v[i] == 2) res *= arr[i + 1];
            else if (v[i] == 3) res /= arr[i + 1];

        maxAns = max(maxAns, res);
        minAns = min(minAns, res);
    } while (next_permutation(v.begin(), v.end()));

    printf("%d\n%d\n", maxAns, minAns);

    return 0;
}
