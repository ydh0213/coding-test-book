#include <string>
#include <algorithm>

using namespace std;

int N, arrA[50], arrB[50];

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; i++) scanf("%d", &arrA[i]);
    for (int i = 0; i < N; i++) scanf("%d", &arrB[i]);

    sort(arrA, arrA + N);
    sort(arrB, arrB + N);
    reverse(arrB, arrB + N);

    int sum = 0;

    for (int i = 0; i < N; i++) sum += arrA[i] * arrB[i];

    printf("%d\n", sum);

    return 0;
}