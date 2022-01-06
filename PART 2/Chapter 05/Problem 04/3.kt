import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val n = nextInt()
    val dp = IntArray(3) { it }
    for (i in 3..n)
        dp[i % 3] = (dp[(i - 1) % 3] + dp[(i - 2) % 3]) % 10007

    println(dp[n % 3])
}
