#include <cstdio>
#include <queue>
#include <cmath>

using namespace std;

int N;
priority_queue<int, vector<int>, greater<> > a; // 양수 저장할 최소힙
priority_queue<int> b; // 음수 저장할 최대힙

int main() {
    scanf("%d", &N);

    int x;
    for (int i = 0; i < N; ++i) {
        scanf("%d", &x);
        if (x > 0)
            a.emplace(x);
        else if (x < 0)
            b.emplace(x);
        else { // x == 0
            if (a.empty()) {
                if (b.empty())
                    printf("0\n");
                else {
                    printf("%d\n", b.top());
                    b.pop();
                }
            } else {
                if (b.empty()) {
                    printf("%d\n", a.top());
                    a.pop();
                } else {
                    if (a.top() < abs(b.top())) {
                        printf("%d\n", a.top());
                        a.pop();
                    } else {
                        printf("%d\n", b.top());
                        b.pop();
                    }
                }
            }
        }
    }

    return 0;
}