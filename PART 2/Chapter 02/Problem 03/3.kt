import java.util.*
import kotlin.math.max

var N = 0
var ans = 0
var board = Array(0) { StringBuilder() }

fun main() = with(Scanner(System.`in`)) {
    N = nextLine().toInt()
    board = Array(N) { StringBuilder(nextLine()) }
    for (i in 0 until N)
        for (j in 0 until N) {
            if (i + 1 < N) {
                board[i][j] = board[i + 1][j].also { board[i + 1][j] = board[i][j] }
                getMaxCandies()
                board[i][j] = board[i + 1][j].also { board[i + 1][j] = board[i][j] }
            }

            if (j + 1 < N) {
                board[i][j] = board[i][j + 1].also { board[i][j + 1] = board[i][j] }
                getMaxCandies()
                board[i][j] = board[i][j + 1].also { board[i][j + 1] = board[i][j] }
            }
        }

    println(ans)
}

fun getMaxCandies() {
    for (i in 0 until N) {
        var tot = 1
        for (j in 1 until N)
            if (board[i][j - 1] == board[i][j]) {
                ++tot
                ans = max(ans, tot)
            } else
                tot = 1
    }

    for (j in 0 until N) {
        var tot = 1
        for (i in 1 until N)
            if (board[i - 1][j] == board[i][j]) {
                ++tot
                ans = max(ans, tot)
            } else
                tot = 1
    }
}
