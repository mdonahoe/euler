// Longest Collatz Sequence
var memo : [Int : Int] = [1 : 0]

func f(_ n : Int) -> Int {
    return n % 2 == 0 ? n / 2 : 3 * n + 1
}

func cycleLength(_ n : Int) -> Int {
    if memo[n] == nil {
        memo[n] = cycleLength(f(n)) + 1
    }
    return memo[n]!
}

let n = 999999
let chains = [Int](1...n).map { (len: cycleLength($0), index: $0) }
let longest = chains.max { a, b in a.len < b.len }
print(longest!.index)
