#include <cstdio>
#include <algorithm>

using namespace std;

int n, arr[2][100001], c[2][100001];

void dp() {
    c[0][0] = arr[0][0];
    c[1][0] = arr[1][0];

    if (n > 1) {
        for (int i = 0; i < 2; ++i)
            c[i][1] = c[(i + 1) % 2][0] + arr[i][1];

        for (int j = 2; j < n; ++j)
            for (int i = 0; i < 2; ++i)
                c[i][j] = max(c[(i + 1) % 2][j - 1], c[(i + 1) % 2][j - 2]) + arr[i][j];
    }
}

int main() {
    int tcN;
    scanf("%d", &tcN);
    for (int tc = 0; tc < tcN; ++tc) {
        scanf("%d", &n);
        for (int i = 0; i < 2; ++i)
            for (int j = 0; j < n; ++j)
                scanf("%d", &arr[i][j]);

        dp();

        printf("%d\n", max(c[0][n - 1], c[1][n - 1]));
    }

    return 0;
}
