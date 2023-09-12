import Foundation

let inp1 = Int(readLine()!) ?? 0
var dict = Dictionary<String, Int>()

for _ in 0..<inp1 {
  guard let inp = readLine() else {
    continue
  }
  
  if dict[inp] == nil {
    dict[inp] = 1
  } else {
    dict[inp]! += 1
  }
}

// MARK: - 1. 본문에서 제시하는 방법. 최대값을 배열을 이용해 추출.
let max_val = dict.values.max() ?? 0
var arr = [String]()

for (key, val) in dict {
    if val == max_val {
        arr.append(key)
    }
}

arr.sort(by: <)
print(arr.first ?? "")

// MARK: - 2. Dictionary 만을 이용해서 최대값을 추출.
let max = dict.max { lh, rh in
  if lh.value == rh.value {
    return lh.key > rh.key
  } else {
    return lh.value < rh.value
  }
}

print(max?.key ?? "")