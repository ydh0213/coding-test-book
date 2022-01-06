import Foundation

var dic = [Int: Int]()
let _ = Int(readLine()!)
for i in readLine()!.split(separator: " ").map({ Int(String($0))! }) {
    if dic[i] == nil {
        dic[i] = 1
    } else {
        dic[i]! += 1
    }
}

let M = Int(readLine()!)!
var ans = [Int]()
for i in readLine()!.split(separator: " ").map({ Int(String($0))! }) {
    if dic[i] == nil {
        ans.append(0)
    } else {
        ans.append(dic[i]!)
    }
}

print(ans[0], terminator: "")
for i in 1..<M {
    print(" " + String(ans[i]), terminator: "")
}