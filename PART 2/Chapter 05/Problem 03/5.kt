import java.util.*
import kotlin.math.min

val INF = 987654321
val cache = IntArray(1_000_001) { INF }

fun main() = with(Scanner(System.`in`)) {
    cache[1] = 0
    val ipt = nextInt()
    for (i in 1..ipt) {
        if (i * 3 < 1_000_001)
            cache[i * 3] = min(cache[i * 3], cache[i] + 1)

        if (i * 2 < 1_000_001)
            cache[i * 2] = min(cache[i * 2], cache[i] + 1)

        if (i + 1 < 1_000_001)
            cache[i + 1] = min(cache[i + 1], cache[i] + 1)
    }

    println(cache[ipt])
}