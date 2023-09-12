import Foundation

struct Stack<T> { // struct, class doesn't matter
    var arr = [T]()
    
    /// O(1)
    mutating func push(_ val: T) {
      arr.append(val)
    }

    /// O(1)
    mutating func pop() -> T? {
      if arr.isEmpty {
        return nil
      }
      return arr.removeFirst()
    }
    
    /// O(1)
    func peek() -> T? {
      arr.last
    }
}

let tot = Int(readLine() ?? "") ?? 0
var chk = [[String]]()

for _ in 0 ..< tot {
    chk.append(
        (readLine() ?? "")
            .map({ String($0) }) // String aka [Character] -> [String]
    )
}

var stk = Stack<String>()

func chkVPS(_ input: [String]) -> Bool {
    defer {
      stk.arr.removeAll()
    }

    for ch in input {
        if ch == "(" {
            stk.push(ch)
        } else {
            if stk.pop() == nil {
                return false
            }
        }
    }
    
    return stk.peek() != nil ? false : true
}

for val in chk {
  print(chkVPS(val) ? "YES" : "NO")
}