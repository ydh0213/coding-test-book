#include <cstdio>
#include <queue>

using namespace std;

int N;
queue<int> q;

int main() {
    scanf("%d", &N);

    for (int i = 1; i <= N; ++i)
        q.push(i);

    while (q.size() > 1) {
        q.pop();
        q.push(q.front());
        q.pop();
    }

    printf("%d\n", q.front());

    return 0;
}