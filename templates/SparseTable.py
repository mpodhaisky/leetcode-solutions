class SparseTable:
    def __init__(self, arr, op, neutral):
        self.op = op
        self.neutral = neutral
        n = len(arr)
        target_len = 1 << (n - 1).bit_length()
        padded = list(arr)
        padded.extend([neutral] * (target_len - n))
        self.st = [padded]
        k = target_len.bit_length()

        for i in range(1, k):
            cur = padded.copy()
            size = 1 << i
            half = size >> 1

            for start in range(0, target_len, size):
                mid = start + half
                end = start + size

                cur[mid - 1] = padded[mid - 1]
                for j in range(mid - 2, start - 1, -1):
                    cur[j] = op(padded[j], cur[j + 1])

                cur[mid] = padded[mid]
                for j in range(mid + 1, end):
                    cur[j] = op(cur[j - 1], padded[j])

            self.st.append(cur)

    def query(self, a, b):
        if b < a:
            return self.neutral
        if a == b:
            return self.st[0][a]

        cur = (a ^ b).bit_length()
        return self.op(self.st[cur][a], self.st[cur][b])
