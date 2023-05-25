import Foundation

typealias ITEM = (Int32)
typealias SORT = (ITEM, ITEM) -> Bool

class PriorityQueue {
  
  var elements: Heap
  var sort: SORT
  var isEmpty: Bool { 
    elements.isEmpty 
  }
  var peek: ITEM? {
    elements.items.first
  }
  
  init(sort: @escaping SORT) {
    self.sort = sort
    self.elements = Heap(sort: sort)
  }
  
  func enqueue(_ val: ITEM) {
    elements.insert(val)
  }
  
  @discardableResult
  func dequeue() -> ITEM? {
    elements.remove(0)
  }
}

/// 초기화 시 sort 로 '<' 를 전달하면 MinHeap. 대체적으로 MinHeap 많이 사용.
/// '>' 를 전달하면 MaxHeap.
class Heap {
  private(set) var items = [ITEM]()
  var isEmpty: Bool { items.isEmpty }
  
  let sort: SORT
  
  init(sort: @escaping SORT, items: [ITEM] = []) {
    self.sort = sort
    self.items = items
  }
    
  func leftIndex(_ index: Int) -> Int { (index * 2) + 1 }
  func rightIndex(_ index: Int) -> Int { (index * 2) + 2 }
  func parentIndex(_ index: Int) -> Int {
    guard index > 0 else { return 0 }
    return (index - 1) / 2
  }
    
  func siftUp(_ index: Int) {
    var child = index, parent = parentIndex(index)
    
    while child > 0 && sort(items[child], items[parent]) {
      items.swapAt(child, parent)
      child = parent
      parent = parentIndex(child)
    }
  }
    
  func siftDown(_ index: Int) {
    var parent = index, candidate = 0
    
    while true {
      let lh = leftIndex(parent), rh = rightIndex(parent)
      candidate = parent
        
      if lh < items.count, sort(items[lh], items[candidate]) {
        candidate = lh
      }
      if rh < items.count, sort(items[rh], items[candidate]) {
        candidate = rh
      }
      if candidate == parent {
        return
      }
      
      items.swapAt(parent, candidate)
      parent = candidate
    }
  }
    
  func insert(_ item: ITEM) {
    items.append(item)
    siftUp(items.count-1)
  }
    
  func remove(_ index: Int) -> ITEM? {
    guard index < items.count else { return nil }
    
    if index == items.count - 1 {
      return items.removeLast()
    }
    else {
      items.swapAt(index, items.count-1)
      
      defer {
        siftUp(index)
        siftDown(index)
      }
      
      return items.removeLast()
    }
  }
}

// MARK: - 문제 입력은 -2 의 31 승 ~ 2 의 31 승 이므로 Int32 를 이용한다.
let inp1 = Int32(readLine() ?? "") ?? 0
let minq = PriorityQueue(sort: <) // 양수
let maxq = PriorityQueue(sort: >) // 음수

for _ in 1...inp1 {
  let inp = Int32(readLine() ?? "") ?? 0

  if inp > 0 {
    minq.enqueue(inp)
  }
  else if inp < 0 {
    maxq.enqueue(inp)
  }
  else {
    if let minp = minq.peek {
      if maxq.isEmpty || minp < abs(maxq.peek ?? 0) {
        print(minq.dequeue() ?? 0)
      }
      else {
        print(maxq.dequeue() ?? 0)
      }
    }
    else {
      print(maxq.dequeue() ?? 0)
    }
  }
}