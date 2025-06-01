# Problem Description

Given a password (a string of lowercase English letters) return its `variability`.

The `variability` of a password is the number of distinct password strings, obtained by reversing any one substring of the password.

## Examples:

### Example 1

Input: `abc`

Expected: `4`

Explanation: There are 4 distinct password strings that can be created by reversing any one substring of the password.

Reversing each one character substring gives `abc`.

Reversing `ab` gives `bac`.

Reversing `bc` gives `acb`.

Reversing `abc` gives `cba`.


### Example 2

Input: `abcab`

Expected: `9`
