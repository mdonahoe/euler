// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.
func fib(_ n : Int) -> Int {
    var a = 1
    var b = 1
    guard n >= 2 else {
        return a
    }
    for _ in 2...n {
        let tmp = a
        a = a + b
        b = tmp
    }
    return a
}

var n = 0
var term = 0
var sum = 0
while term < Int(4e6) {
    if term % 2 == 0 {
        sum += term
    }
    n += 1
    term = fib(n)
    print("n = \(n), fib(n) = \(term)")
}
print(sum)
