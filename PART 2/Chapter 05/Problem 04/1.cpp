#include <cstdio>

using namespace std;

const int MOD = 10007;

int n, cache[1001] = {0, 1, 2};

int f(int i) {
    if (i < 3) return cache[i];

    for (int j = 3; j <= i; ++j)
        cache[j] = (cache[j - 1] + cache[j - 2]) % MOD;

    return cache[i];
}

int main() {
    scanf("%d", &n);

    printf("%d\n", f(n));

    return 0;
}
