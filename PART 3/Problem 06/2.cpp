/* 연결리스트와 포인터를 이용한 방법
연결 리스트를 항상 오름차순으로 연결 리스트를 유지한다. (정렬한 것과 동일함)
매번 2개의 값을 입력받아 연결리스트 내 어디에 이 값을 어디에 넣을지 위치를 찾아 정렬이 유지되도록 두 값을 넣는다.
it은 항상 중앙값을 가리키고 있는 iterator이다. 위에서 2개의 값을 넣으면서 이 it의 위치를 조정한다. */

#include <cstdio>
#include <list>

using namespace std;

int M, ans[5000];
list<int> l;
list<int>::iterator it;

int main() {
    int tcN;
    scanf("%d", &tcN);

    int ipt1, ipt2;
    for (int tc = 0; tc < tcN; ++tc) {
        l.clear();
        scanf("%d", &M);

        // 첫번째 수
        scanf("%d", &ipt1);
        l.emplace_back(ipt1);
        ans[0] = ipt1;
        it = l.begin();

        // 2개씩 입력받아 반복
        int repeatN = (M - 1) / 2;
        for (int i = 1, move = 0; i <= repeatN; ++i, move = 0) {
            scanf("%d %d", &ipt1, &ipt2);
            if (ipt1 >= *it) ++move;
            else --move;

            if (ipt2 >= *it) ++move;
            else --move;

            if (*(l.rbegin()) <= ipt1)
                l.emplace_back(ipt1);
            else
                for (auto jt = l.begin(); jt != l.end(); ++jt)
                    if (ipt1 < *jt) {
                        l.emplace(jt, ipt1);
                        break;
                    }

            if (*(l.rbegin()) <= ipt2)
                l.emplace_back(ipt2);
            else
                for (auto jt = l.begin(); jt != l.end(); ++jt)
                    if (ipt2 < *jt) {
                        l.emplace(jt, ipt2);
                        break;
                    }

            if (move > 0) ++it;
            else if (move < 0) --it;

            ans[i] = *it;
        }

        printf("%d", repeatN + 1);
        for (int i = 0; i <= repeatN; ++i)
            printf("%s%d", i % 10 ? " " : "\n", ans[i]);

        printf("\n");
    }

    return 0;
}
