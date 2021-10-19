import java.util.*

var N = 0
var cnt = 0
val board = Array(20) { Array(20) { false } }
val isOnQueenInCol = Array(20) { false }

fun main() = with(Scanner(System.`in`)) {
    N = nextInt()
    backTracking(0)
    println(cnt)
}

fun backTracking(i: Int) {
    if (i >= N) {
        ++cnt
        return
    }

    for (j in 0 until N) {
        if (!isOnQueenInCol[j] && !isOnQueenInDiagonal(i, j)) {
            board[i][j] = true
            isOnQueenInCol[j] = true
            backTracking(i + 1)
            isOnQueenInCol[j] = false
            board[i][j] = false
        }
    }
}

// y, x 기준으로 ↖, ↗ 방향으로 퀸이 있는지
fun isOnQueenInDiagonal(y: Int, x: Int): Boolean {
    for (i in 1..y)
        if (0 <= x - i && board[y - i][x - i]) return true;
        else if (x + i < N && board[y - i][x + i]) return true;

    return false;
}