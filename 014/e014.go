package main

import "fmt"

var memo map[int]int

func f(n int) int {
    if n%2 == 0 {
        return n / 2
    } else {
        return 3 * n + 1
    }
}

func cycleLength(n int) int {
    if _, ok := memo[n]; !ok {
        memo[n] = cycleLength(f(n)) + 1
    }
    return memo[n]
}

func main() {
    memo = make(map[int]int)
    memo[1] = 0

    N := 1000000
    chains := make([]int, N)
    for i:=1; i < N; i++ {
        chains[i] = cycleLength(i)
    }

    longest := 1
    index := 1
    for i:=1; i < N; i++ {
        if chains[i] > longest {
            longest = chains[i]
            index = i
        }
    }

    fmt.Println(index)
}
