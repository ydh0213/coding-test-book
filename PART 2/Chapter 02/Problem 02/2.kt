import java.util.*

val triNum = MutableList(0) { 0 }

fun main() = with(Scanner(System.`in`)) {
    makeTriNum()
    repeat(nextInt()) {
        println(if (isPossible(nextInt())) 1 else 0)
    }
}

fun makeTriNum() {
    triNum.add(1)
    for (i in 2 until 45)
        triNum.add(triNum.last() + i)
}

fun isPossible(n: Int): Boolean {
    for (t1 in triNum.indices)
        for (t2 in t1 until triNum.lastIndex)
            for (t3 in t2 until triNum.lastIndex)
                if (triNum[t1] + triNum[t2] + triNum[t3] == n)
                    return true

    return false
}