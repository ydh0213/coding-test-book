#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    for (int n: course) {
        map<string, int> cnt;
        for (string order: orders) {
            sort(order.begin(), order.end());

            if (order.length() >= n) {
                vector<int> v(order.length(), 0);
                for (int i = 0; i < n; ++i)
                    v[order.length() - 1 - i] = 1;

                do {
                    string combination;
                    for (int i = 0; i < order.length(); ++i)
                        if (v[i])
                            combination += order[i];

                    if (cnt.find(combination) == cnt.end())
                        cnt[combination] = 1;
                    else
                        cnt[combination] += 1;
                } while (next_permutation(v.begin(), v.end()));
            }
        }

        int maxVal = 0;
        for (const auto &p: cnt)
            maxVal = max(maxVal, p.second);

        if (maxVal >= 2)
            for (const auto &p: cnt)
                if (p.second == maxVal)
                    answer.emplace_back(p.first);
    }

    sort(answer.begin(), answer.end());
    return answer;
}