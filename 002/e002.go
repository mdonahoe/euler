package main

import "fmt"

// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.
func fib(n int) int {
    var a = 1
    var b = 1
    if n < 2 {
        return a
    }
    for i := 2; i < n; i++ {
        tmp := a
        a = a + b
        b = tmp
    }
    return a
}

func main() {
    n := 0
    term := 0
    sum := 0
    for term < 4e6 {
        if term % 2 == 0 {
            sum += term
        }
        n += 1
        term = fib(n)
        fmt.Printf("n = %v, fib(n) = %v\n", n, term)
    }
    fmt.Println(sum)
}
