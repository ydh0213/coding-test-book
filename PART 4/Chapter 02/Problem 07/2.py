from bisect import bisect_left


def solution(infos, queries):
    db = {}
    for info in infos:
        s = info.split()
        for i in [s[0], '-']:
            for j in [s[1], '-']:
                for k in [s[2], '-']:
                    for l in [s[3], '-']:
                        key = (i, j, k, l)
                        val = int(s[4])
                        if key in db:
                            db[key].append(val)
                        else:
                            db[key] = [val]

    for key in db.keys():
        db[key].sort()

    ans = []
    for query in queries:
        q = query.split()
        key = (q[0], q[2], q[4], q[6])
        ans.append(len(db[key]) - bisect_left(db[key], int(q[7])) if key in db else 0)

    return ans