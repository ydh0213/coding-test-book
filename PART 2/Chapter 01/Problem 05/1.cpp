#include <cstdio>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int N;
map<string, int> mp;

int main() {
    scanf("%d", &N);
    string book;
    for (int i = 0; i < N; ++i) {
        cin >> book;
        ++mp[book];
    }

    pair<string, int> maxBook;
    for (auto b : mp)
        if (maxBook.second < b.second) maxBook = b;

    cout << maxBook.first << endl;

    return 0;
}