import Foundation

let input = (readLine() ?? "").split(separator: " ").map({Int($0) ?? 0})
let n = input[0], k = input[1]
var peo = [Int]()
for i in 1...n {
    peo.append(i)
}

var pt: Int = 0
var acc = [String]()

for _ in peo {
    pt += k - 1
    pt %= peo.count // ex. 9 %= 7 => 2
  
    acc.append(String(peo.remove(at: pt)))
}

print("<" + acc.joined(separator: ", ") + ">") // joined only works at Array<String>.