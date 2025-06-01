# Problem Description

You are given an array of `n` positive integers, `nums`.

In one `operation` you may do the following:
- Choose any integer `x`.
- For all `i`, if `aᵢ = x` replace `aᵢ` with `0`.

Return the minimum number of operations needed to make the array sorted in non-decreasing order.

### Constraints:

`1 <= n <= 10^5`

`1 <= aᵢ <= n`

## Examples:

### Example 1

Input: `nums = [3, 3, 2]`

Expected: `1`

Explanation: Choose `x = 3` thereby setting the first two elements to `0`. Then `nums` is in sorted order.

### Example 2

Input: `nums = [2, 3, 2, 5, 4]`

Expected: `3`

Explanation: In order for the array to be in sorted order, the `5` must be set to `0`. As a result, the preceding elements must also be set to `0`, which will take `3` operations.
