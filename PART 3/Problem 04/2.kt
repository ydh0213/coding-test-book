// Floyd-Warshall

import java.util.*
import kotlin.math.min

val INF = 987654321

fun main() = with(Scanner(System.`in`)) {
    val N = nextInt()
    val gr = List(N) { MutableList(N) { INF } }
    for (i in 0 until nextInt()) {
        val a = nextInt() - 1
        val b = nextInt() - 1
        gr[a][b] = 1
        gr[b][a] = 1
    }

    for (k in 0 until N)
        for (i in 0 until N)
            if (gr[i][k] < INF)
                for (j in 0 until N)
                    if (i != j && gr[k][j] < INF)
                        gr[i][j] = min(gr[i][j], gr[i][k] + gr[k][j])

    val kevinBacon = MutableList(N) {0}
    for (i in 0 until N)
        for (j in 0 until N)
            if (i != j) kevinBacon[i] += gr[i][j]

    for (i in 0 until N)
        if (kevinBacon[i] == kevinBacon.minOrNull()) {
            println(i + 1)
            break
        }
}
