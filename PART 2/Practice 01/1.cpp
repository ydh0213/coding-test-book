#include <cstdio>
#include <iostream>
#include <string>
#include <list>

using namespace std;

string lg; // log
list<char> pw;
list<char>::iterator cur; // 커서

int main() {
    int tcN;
    scanf("%d", &tcN);
    for (int tc = 0; tc < tcN; ++tc) {
        pw.clear();
        cur = pw.begin();
        cin >> lg;
        for (char ch : lg)
            if (ch == '<') {
                if (cur != pw.begin()) --cur;
            } else if (ch == '>') {
                if (cur != pw.end()) ++cur;
            } else if (ch == '-') {
                if (cur != pw.begin()) {
                    auto bef = cur;
                    --bef;
                    pw.erase(bef);
                }
            } else pw.insert(cur, ch);

        for (char ch : pw) printf("%c", ch);
        printf("\n");
    }

    return 0;
}