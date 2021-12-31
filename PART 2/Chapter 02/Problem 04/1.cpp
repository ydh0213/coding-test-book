#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

class Meeting {
public:
    Meeting(int l, int r) : l(l), r(r) {};

    bool operator < (const Meeting &m) const {
        if (r != m.r) return r < m.r;

        return l < m.l;
    }

    int l, r;
};

int N, t, ans;
vector<Meeting> v;

int main() {
    scanf("%d", &N);

    int a, b;
    for (int i = 0; i < N; ++i) {
        scanf("%d %d", &a, &b);
        v.emplace_back(a, b);
    }

    sort(v.begin(), v.end());

    for (int i = 0; i < N; ++i)
        if (t <= v[i].l) {
            ++ans;
            t = v[i].r;
        }

    printf("%d\n", ans);

    return 0;
}