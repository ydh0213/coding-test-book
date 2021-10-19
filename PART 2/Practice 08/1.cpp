#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int ipt, dp[100005];

int main() {
    scanf("%d", &ipt);

    for (int i = 1; i <= ipt; i++) dp[i] = i; // 1^2 + 1^2 + 1^2 + ...

    int lmt = sqrt(ipt + 1);
    for (int i = 2; i <= lmt; i++)
        for (int idx = i * i; idx <= ipt; idx++)
            dp[idx] = min(dp[idx], dp[idx - i * i] + 1);


    printf("%d\n", dp[ipt]);

    return 0;
}