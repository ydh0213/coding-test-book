import java.util.*
import kotlin.math.max

fun main() = with(Scanner(System.`in`)) {
    repeat(nextInt()) {
        val N = nextInt()
        val sticker = Array(2) { IntArray(N) { nextInt() } }
        val dp = Array(2) { IntArray(N) { 0 } }
        for (i in 0 until 2)
            dp[i][0] = sticker[i][0]

        if (N > 1) {
            for (i in 0 until 2)
                dp[i][1] = dp[i xor 1][0] + sticker[i][1]

            if (N > 2) {
                for (j in 2 until N)
                    for (i in 0 until 2)
                        dp[i][j] = max(dp[i xor 1][j - 2], dp[i xor 1][j - 1]) + sticker[i][j]
            }
        }

        println(max(dp[0][N - 1], dp[1][N - 1]))
    }
}
