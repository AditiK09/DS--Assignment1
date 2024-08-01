import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0
        self.cap = 1
        self.arr = self.create_arr(self.cap)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        return self.arr[k]

    def append(self, ele):
        if self.n == self.cap:
            self._resize(2 * self.cap)
        self.arr[self.n] = ele
        self.n += 1

    def prepend(self, ele):
        self.insertAt(ele, 0)

    def insertAt(self, item, ind):
        if ind < 0 or ind > self.n:
            print("Please enter an appropriate index.")
            return
        if self.n == self.cap:
            self._resize(2 * self.cap)

    def delete(self):
        if self.n == 0:
            print("Array is empty; deletion not possible")
            return
        self.arr[self.n-1] = 0
        self.n -= 1

    def removeAt(self, ind):
        if self.n == 0:
            print("Array is empty; deletion not possible")
            return
        if ind < 0 or ind >= self.n:
            return IndexError("Index out of bound...deletion not possible")
        for i in range(ind, self.n-1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.n-1] = 0
        self.n -= 1

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def rotate_right(self, k):
        k = k % self.n
        if k == 0:
            return
        self.reverse(0, self.n - 1)
        self.reverse(0, k - 1)
        self.reverse(k, self.n - 1)

    def reverse(self, start=0, end=None):
        if end is None:
            end = self.n - 1
        while start < end:
            self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
            start += 1
            end -= 1

    def merge(self, other):
        for i in range(len(other)):
            self.append(other[i])

    def middle_element(self):
        if self.n == 0:
            return None
        return self.arr[self.n // 2]

    def index_of(self, value):
        for i in range(self.n):
            if self.arr[i] == value:
                return i
        return -1

    def _resize(self, new_cap):
        B = self.create_arr(new_cap)
        for k in range(self.n):
            B[k] = self.arr[k]
        self.arr = B
        self.cap = new_cap

    