#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int N, M, houseSz, chickenSz, ans = 987654321;
vector<pair<int, int> > house, chicken;

int getDistance(int i, int j) {
    return abs(house[i].first - chicken[j].first) + abs(house[i].second - chicken[j].second);
}

int main() {
    scanf("%d %d", &N, &M);

    int ipt;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) {
            scanf("%d", &ipt);
            if (ipt == 1) house.emplace_back(i, j);
            else if (ipt == 2) chicken.emplace_back(i, j);
        }

    houseSz = house.size();
    chickenSz = chicken.size();
    vector<int> v(chickenSz, 0);
    for (int i = 0; i < M; ++i) v[v.size() - 1 - i] = 1;

    do {
        int chickenRoad = 0;
        for (int i = 0; i < houseSz; ++i) {
            int cr = 987654321;
            for (int j = 0; j < chickenSz; ++j)
                if (v[j])
                    cr = min(cr, getDistance(i, j));

            chickenRoad += cr;
        }

        ans = min(ans, chickenRoad);
    } while (next_permutation(v.begin(), v.end()));

    printf("%d\n", ans);

    return 0;
}
