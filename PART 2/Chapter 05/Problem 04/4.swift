let n = Int(readLine()!)!
var dp = [Int](repeating: 1, count: 2)
if n > 1 {
    for i in 2...n {
        dp.append((dp[i - 1] + dp[i - 2]) % 10007)
    }
}

print(dp[n])