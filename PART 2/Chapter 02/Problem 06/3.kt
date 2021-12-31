import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

var N = 0
var M = 0
var gr = Array(0) { Array(0) { false } }
var chk = Array(0) { false }
var ans = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    BufferedWriter(OutputStreamWriter(System.out)).use { bw ->
        val nm = readLine().split(" ").map { it.toInt() }
        N = nm[0]
        M = nm[1]
        gr = Array(N) { Array(N) { false } }
        chk = Array(N) { false }
        repeat(M) {
            val (u, v) = readLine().split(" ").map { it.toInt() - 1 }
            gr[u][v] = true
            gr[v][u] = true
        }

        for (i in 0 until N)
            if (!chk[i]) {
                ++ans
                dfs(i)
            }

        bw.write("${ans}\n")
    }
}

fun dfs(i: Int) {
    if (chk[i]) return

    chk[i] = true

    for (j in 0 until N)
        if (gr[i][j] && !chk[j])
            dfs(j)
}
