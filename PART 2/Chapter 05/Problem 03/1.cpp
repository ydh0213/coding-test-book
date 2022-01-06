#include <cstdio>
#include <algorithm>

using namespace std;

int N, cache[1000001];

// x를 1로 만드는 연산의 최소 횟수
int f(int x) {
    if (x == 1) return 0;

    if (cache[x] != -1) return cache[x];

    int &res = cache[x];

    res = f(x - 1) + 1;
    if (x % 3 == 0) res = min(res, f(x / 3) + 1);
    if (x % 2 == 0) res = min(res, f(x / 2) + 1);

    return res;
}

int main() {
    fill(cache, cache + 1000001, -1);

    scanf("%d", &N);

    printf("%d\n", f(N));

    return 0;
}
