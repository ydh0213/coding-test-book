#include <cstdio>
#include <algorithm>

using namespace std;

int n[9], nn[9] = {0, 0, 1, 1, 1, 1, 1, 1, 1};

int main() {
    for (int i = 0; i < 9; ++i) scanf("%d", &n[i]);
    do {
        int sum = 0;
        for (int i = 0; i < 9; ++i) sum += n[i] * nn[i];

        if (sum == 100) {
            for (int i = 0; i < 9; ++i)
                if (nn[i]) printf("%d\n", n[i]);

            break;
        }
    } while (next_permutation(nn, nn + 9));

    return 0;
}