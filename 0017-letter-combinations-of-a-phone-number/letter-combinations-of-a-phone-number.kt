class Solution {
    private val mapping = arrayOf(
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    )

    fun letterCombinations(digits: String): List<String> {
        if (digits.isEmpty()) return emptyList()
        
        val result = mutableListOf<String>()
        backtrack(digits, 0, StringBuilder(), result)
        return result
    }

    private fun backtrack(digits: String, index: Int, current: StringBuilder, result: MutableList<String>) {
        // Base case: if the current combination length matches digits length, add to result
        if (index == digits.length) {
            result.add(current.toString())
            return
        }

        // Get the letters corresponding to the current digit
        val digitChar = digits[index]
        val letters = mapping[digitChar - '0']

        // Iterate through all possible letters for this digit
        for (letter in letters) {
            current.append(letter)                 // Choose
            backtrack(digits, index + 1, current, result) // Explore
            current.deleteCharAt(current.length - 1)  // Un-choose (Backtrack)
        }
    }
}