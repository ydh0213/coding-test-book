import Foundation

// MARK: - LinkedList Start
class LinkedList<T> {
  var head: LinkedNode<T>?
  var tail: LinkedNode<T>?
  var isEmpty: Bool {
    head == nil && tail == nil
  }
  
  func push(_ val: T) {
    head = LinkedNode<T>(val: val, nxt: head)
    if tail == nil {
      tail = head
    }
  }
  
  func append(_ val: T) {
    guard isEmpty == false else {
      push(val)
      return
    }
    
    tail?.nxt = LinkedNode(val: val, nxt: nil)
    tail = tail?.nxt
  }
  
  func removeLast() -> T? {
    guard head?.nxt != nil else {
      head = nil
      return head?.val
    }
    
    var prev: LinkedNode<T>?
    var now = head
    
    while let nxt = now?.nxt {
      prev = now
      now = nxt
    }
    
    prev?.nxt = nil
    tail = prev
    return now?.val
  }
  
  func removeFirst() -> T? {
    defer {
      head = head?.nxt
      if head == nil {
        tail = nil
      }
    }
    
    return head?.val
  }
}

class LinkedNode<T> {
  let val: T
  var nxt: LinkedNode<T>?

  init(val: T, nxt: LinkedNode<T>?) {
    self.val = val; self.nxt = nxt
  }
}

// MARK: - LinkedList End

class Queue<T> {
  var lst: LinkedList<T>
  var isEmpty: Bool {
    lst.isEmpty
  }

  var peek: T? {
    lst.head?.val
  }
    
  init(lst: LinkedList<T>) {
    self.lst = lst
  }

  func enqueue(_ val: T) {
    lst.append(val)
  }

  @discardableResult
  func dequeue() -> T? {
    lst.removeFirst()
  }
}

let input = Int(readLine() ?? "") ?? 0
var q = Queue<Int>(lst: LinkedList())

for i in 1...input {
  q.enqueue(i)
}

while q.isEmpty == false {
  let tmp = q.dequeue()
  
  if q.isEmpty {
    print(tmp ?? 0)
  } else {
    q.enqueue(q.dequeue()!)
  }
}