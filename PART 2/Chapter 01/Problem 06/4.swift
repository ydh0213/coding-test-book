import Foundation

let inp1 = Int(readLine()!) ?? 0
var st = Set<String>()

for _ in 0..<inp1 {
  guard let inp = readLine() else {
    continue
  }

  let arr = inp.split(separator: " ").map({String($0)})

  guard let name = arr.first, let chk = arr.last else {
    continue
  }

  if chk == "enter" {
    st.insert(name)
  } else {
    st.remove(name)
  }
}

for ans in st.sorted(by: >) {
  print(ans)
}