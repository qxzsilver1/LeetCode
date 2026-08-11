class Solution {
    func findSafeWalk(_ grid: [[Int]], _ health: Int) -> Bool {
        let m = grid.count
        let n = grid[0].count

        let directions: [(Int, Int)] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        var bestCost: [[Int]] = Array(repeating: Array(repeating: 10_000, count: n), count: m)

        var heap = Heap<Node>()

        heap.insert(Node(r: 0, c: 0, cost: grid[0][0]))

        while let node = heap.popMin() {
            let r = node.r
            let c = node.c
            let cost = node.cost

            guard cost < bestCost[r][c] else { continue }

            bestCost[r][c] = cost

            if r == m - 1, c == n - 1 {
                break
            }

            for (dr, dc) in directions {
                let nr = r + dr
                let nc = c + dc

                guard nr >= 0, nr < m, nc >= 0, nc < n else { continue }

                let candidate = cost + grid[nr][nc]

                if candidate < bestCost[nr][nc] {
                    heap.insert(Node(r: nr, c: nc, cost: candidate))
                }
            }
        }

        return health - bestCost[m-1][n-1] >= 1
    }

    struct Node: Comparable {
        var r: Int
        var c: Int

        var cost: Int

        static func < (_ lhs: Node, _ rhs: Node) -> Bool {
            lhs.cost < rhs.cost
        }
    }
}
