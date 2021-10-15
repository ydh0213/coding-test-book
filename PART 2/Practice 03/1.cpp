#include <cstdio>
#include <algorithm>

using namespace std;

int N, arr[1500 * 1500];

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            scanf("%d", &arr[i * N + j]);

    sort(arr, arr + N * N);
    printf("%d\n", arr[N * N - N]);

    return 0;
}