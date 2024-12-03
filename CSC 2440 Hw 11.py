#Jayden
def inputTreeValues():
    n = int(input("Enter the number of elements: "))
    print("Enter the elements")
    arr = []
    for i in range(n):
        print(f"Element {i + 1}: ", end="")
        value = int(input())
        arr.append(value)
    return arr

def minHeapify(heap, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] < heap[smallest]:
        smallest = left

    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        minHeapify(heap, n, smallest)

def buildMinHeap(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(heap, n, i)

def heapSortDescending(arr):
    buildMinHeap(arr)
    sorted_arr = []
    while arr:
        sorted_arr.insert(0, arr[0])
        arr[0] = arr[-1]
        arr.pop()
        minHeapify(arr, len(arr), 0)
    return sorted_arr

def printSortedArray(sorted_arr):
    print("Sorted array in decreasing order:")
    print(" ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    print("Heap Sort Program")
    array = inputTreeValues()
    sorted_array = heapSortDescending(array)
    printSortedArray(sorted_array)
