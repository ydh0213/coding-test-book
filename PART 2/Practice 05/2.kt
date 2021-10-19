import java.util.*

val dy = arrayOf(-1, -2, -2, -1, 1, 2, 2, 1)
val dx = arrayOf(-2, -1, 1, 2, 2, 1, -1, -2)
var l = 0

fun main() = with(Scanner(System.`in`)) {
    repeat(nextInt()) {
        l = nextInt()
        val chk = MutableList(l) { MutableList(l) { false } }
        val q: Queue<State> = LinkedList()
        val sy = nextInt()
        val sx = nextInt()
        val gy = nextInt()
        val gx = nextInt()
        chk[sy][sx] = true
        q.add(State(sy, sx, 0))
        while (!q.isEmpty()) {
            val now = q.poll()
            if (now.y == gy && now.x == gx) {
                println(now.d)
                break
            }

            for (k in 0 until 8) {
                val ny = now.y + dy[k]
                val nx = now.x + dx[k]
                val nd = now.d + 1
                if (isValidCoord(ny, nx) && !chk[ny][nx]) {
                    chk[ny][nx] = true
                    q.add(State(ny, nx, nd))
                }
            }
        }
    }
}

fun isValidCoord(y: Int, x: Int) = y in 0 until l && x in 0 until l

data class State(val y: Int, val x: Int, val d: Int)
