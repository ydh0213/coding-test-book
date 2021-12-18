import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val mp = emptyMap<String, Int>().toSortedMap()
    repeat(nextInt()) {
        val k = next()
        mp[k]?.let { mp.put(k, mp[k]!! + 1) } ?: mp.put(k, 1)
    }

    println(mp.maxByOrNull { it.value }!!.key)
}