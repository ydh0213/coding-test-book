#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s;
int cnt[27];
int len;

int main() {
    cin >> s;
    len = s.length();
    for (int i = 0; i < len; i++) cnt[s[i] - 'A']++;

    int oddN = 0;
    for (int i = 0; i < 26; i++)
        if (cnt[i] % 2) oddN++;

    if (oddN > 1) printf("I'm Sorry Hansoo\n");
    else {
        string tmp;
        for (int i = 0; i < 26; i++)
            for (int j = 0; j < cnt[i] / 2; j++) tmp += 'A' + i;

        string ans = tmp;
        for (int i = 0; i < 26; i++)
            if (cnt[i] % 2) {
                ans += 'A' + i;
                break;
            }

        reverse(tmp.begin(), tmp.end());
        ans += tmp;

        cout << ans << endl;
    }

    return 0;
}