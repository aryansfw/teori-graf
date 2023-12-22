class LongestIncreasingSubsequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length_of_lis = 0
        self.subsequence_lengths = []
        self.subsequence_indices = []

    def compute_longest_increasing_subsequence(self):
        sequence_length = len(self.sequence)
        self.subsequence_indices = [0] * sequence_length
        self.subsequence_lengths = [-1] * (sequence_length + 1)
        self.subsequence_lengths[0] = -1

        for i in range(sequence_length):
            lower_bound = 1
            upper_bound = self.length_of_lis + 1

            while lower_bound < upper_bound:
                mid = lower_bound + (upper_bound - lower_bound) // 2

                if self.sequence[self.subsequence_lengths[mid]] >= self.sequence[i]:
                    upper_bound = mid
                else:
                    lower_bound = mid + 1

            new_length = lower_bound
            self.subsequence_indices[i] = self.subsequence_lengths[new_length - 1]
            self.subsequence_lengths[new_length] = i

            if new_length > self.length_of_lis:
                self.length_of_lis = new_length

        lis = [0] * self.length_of_lis
        k = self.subsequence_lengths[self.length_of_lis]
        for j in range(self.length_of_lis - 1, -1, -1):
            lis[j] = self.sequence[k]
            k = self.subsequence_indices[k]

        return lis, self.length_of_lis

if __name__ == "__main__":
    sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
    lis_calculator = LongestIncreasingSubsequence(sequence)
    longest_subsequence, length = lis_calculator.compute_longest_increasing_subsequence()
    print("Longest Increasing Subsequence: ", longest_subsequence)
    print("Length of Longest Increasing Subsequence: ", length)