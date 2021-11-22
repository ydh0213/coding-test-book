#include <cstdio>
#include <algorithm>

using namespace std;

long long N, dice[6];

long long getMin1() {
    long long minVal = 50;
    for (int i = 0; i < 6; i++) minVal = min(minVal, dice[i]);

    return minVal;
}

long long getMin2() {
    long long res = 100;
    for (int i = 0; i < 5; i++)
        for (int j = i + 1; j < 6; j++)
            if (i + j != 5)
                res = min(res, dice[i] + dice[j]);

    return res;
}

long long getMin3() {
    long long res = 150;
    for (int i = 0; i < 4; i++)
        for (int j = i + 1; j < 5; j++)
            if (i + j != 5)
                for (int k = j + 1; k < 6; k++)
                    if (j + k != 5 && i + k != 5)
                        res = min(res, dice[i] + dice[j] + dice[k]);

    return res;
}

int main() {
    scanf("%lld", &N);
    for (int i = 0; i < 6; i++) scanf("%lld", &dice[i]);

    if (N == 1) {
        long long maxVal = 0ll;
        long long sum = 0ll;
        for (int i = 0; i < 6; i++) {
            sum += dice[i];
            maxVal = max(maxVal, dice[i]);
        }

        printf("%lld\n", sum - maxVal);
    } else {
        long long ans = getMin3() * 4ll;
        ans += getMin2() * 4ll * (2ll * N - 3ll);
        ans += getMin1() * (N - 2ll) * (5ll * N - 6ll);
        printf("%lld\n", ans);
    }

    return 0;
}