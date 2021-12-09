#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<string> split(string s) {
    istringstream ss(s);
    string buf;
    vector<string> res;
    while (getline(ss, buf, ' '))
        res.emplace_back(buf);

    return res;
}

vector<int> solution(vector<string> infos, vector<string> queries) {
    map<string, vector<int> > mp;
    for (const string &info: infos) {
        vector<string> s = split(info);
        for (const string &s0: vector<string>{s[0], "-"})
            for (const string &s1: vector<string>{s[1], "-"})
                for (const string &s2: vector<string>{s[2], "-"})
                    for (const string &s3: vector<string>{s[3], "-"})
                        mp[s0 + s1 + s2 + s3].emplace_back(atoi(s[4].c_str()));
    }

    for (auto it = mp.begin(); it != mp.end(); ++it)
        sort(it->second.begin(), it->second.end());

    vector<int> answer;
    for (const string &query: queries) {
        vector<string> s = split(query);
        string q = s[0] + s[2] + s[4] + s[6];
        if (mp.find(q) == mp.end())
            answer.emplace_back(0);
        else {
            auto v = mp[q];
            answer.emplace_back(v.end() - lower_bound(v.begin(), v.end(), atoi(s[7].c_str())));
        }
    }

    return answer;
}