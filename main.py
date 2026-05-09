from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        arr = data[:]
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class PythonSort(SortStrategy):
    def sort(self, data): return sorted(data)

class ReverseSort(SortStrategy):
    def sort(self, data): return sorted(data, reverse=True)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

if __name__ == "__main__":
    data = [5, 2, 8, 1, 9, 3]
    sorter = Sorter(BubbleSort())
    print("Bubble:", sorter.sort(data))

    sorter.set_strategy(ReverseSort())
    print("Teskari:", sorter.sort(data))

    sorter.set_strategy(PythonSort())
    print("Python:", sorter.sort(data))
