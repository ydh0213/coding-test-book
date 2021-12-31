import java.util.*

val dy = arrayOf(0, 1, 0, -1)
val dx = arrayOf(1, 0, -1, 0)
var N = 0
var M = 0

fun main() = with(Scanner(System.`in`)) {
    N = nextInt()
    M = nextInt()
    val board = Array(N) { next() }
    val chk = MutableList(N) { MutableList(M) { false } }
    val q: Queue<State> = LinkedList()
    q.add(State(0, 0, 1))
    chk[0][0] = true
    while (!q.isEmpty()) {
        val now = q.poll()
        if (now.y == N - 1 && now.x == M - 1) {
            println(now.d)
            break
        }

        for (k in 0 until 4) {
            val ny = now.y + dy[k]
            val nx = now.x + dx[k]
            val nd = now.d + 1
            if (isValidCoord(ny, nx) && board[ny][nx] == '1' && !chk[ny][nx]) {
                chk[ny][nx] = true
                q.add(State(ny, nx, nd))
            }
        }
    }
}

fun isValidCoord(y: Int, x: Int) = y in 0 until N && x in 0 until M

data class State(val y: Int, val x: Int, val d: Int)
