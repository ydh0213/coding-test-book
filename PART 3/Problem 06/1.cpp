// 홀수번째마다 정렬해서 중앙값 구하기

#include <cstdio>
#include <algorithm>

using namespace std;

int M, arr[9999], ans[5000];

int main() {
    int tcN;
    scanf("%d", &tcN);
    for (int tc = 0; tc < tcN; ++tc) {
        scanf("%d", &M);
        for (int i = 0; i < M; ++i) {
            scanf("%d", &arr[i]);
            if ((i & 1) == 0) {
                sort(arr, arr + i + 1);
                ans[i / 2] = arr[i / 2];
            }
        }

        int sz = (M + 1) / 2;
        printf("%d", sz);
        for (int i = 0; i < sz; ++i)
            printf("%s%d", i % 10 ? " " : "\n", ans[i]);

        printf("\n");
    }

    return 0;
}