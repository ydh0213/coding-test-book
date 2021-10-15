#include <cstdio>
#include <queue>

using namespace std;

int N;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
    scanf("%d", &N);

    int ipt;
    for (int i = 0; i < N; ++i) {
        scanf("%d", &ipt);
        pq.emplace(ipt);
    }

    for (int i = 1; i < N; ++i)
        for (int j = 0; j < N; ++j) {
            scanf("%d", &ipt);
            if (ipt > pq.top()) {
                pq.pop();
                pq.emplace(ipt);
            }
        }

    printf("%d\n", pq.top());

    return 0;
}