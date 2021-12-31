let dy = [0, 1, 0, -1]
let dx = [1, 0, -1, 0]

let rc = readLine()!.split(separator: " ").map {
    Int(String($0))!
}
let R = rc[0], C = rc[1]
let asciiA = UnicodeScalar("A").value
var chk = [Bool](repeating: false, count: 26)
var board: [[Int]] = []
for _ in 0..<R {
    board.append(readLine()!.map {
        Int(UnicodeScalar(String($0))!.value - asciiA)
    })
}

// 입력으로 들어온 알파벳 종류 수를 센다. 그게 가능한 최댓값이다
var maximum = 0
for i in board {
    for j in i {
        if !chk[j] {
            chk[j] = true
            maximum += 1
        }
    }
}

var ans = 0

func backtracking(_ y: Int, _ x: Int, _ d: Int, _ bitmask: Int) {
    if ans < d {
        ans = d
        if ans >= maximum {
            return
        }
    }

    for k in 0..<4 {
        let ny = y + dy[k]
        let nx = x + dx[k]
        if 0..<R ~= ny && 0..<C ~= nx {
            let nb = 1 << board[ny][nx]
            if bitmask & nb == 0 {
                backtracking(ny, nx, d + 1, bitmask | nb)
                if ans >= maximum {
                    return
                }
            }
        }
    }
}

backtracking(0, 0, 1, 1 << board[0][0])
print(ans)