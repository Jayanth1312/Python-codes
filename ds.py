import time

class ListOperations:
    def __init__(self):
        self.data = []

    def search(self, search_value):
        start_time = time.perf_counter()
        try:
            _ = self.data.index(search_value)
            result = True
        except ValueError:
            result = False
        end_time = time.perf_counter()
        return end_time - start_time

    def insert(self, value, index=None):
        start_time = time.perf_counter()
        if index is None:
            self.data.append(value)
        else:
            self.data.insert(index, value)
        end_time = time.perf_counter()
        return end_time - start_time

    def delete(self, value):
        start_time = time.perf_counter()
        try:
            self.data.remove(value)
        except ValueError:
            pass
        end_time = time.perf_counter()
        return end_time - start_time

def main():
    sorted_operations = ListOperations()
    unsorted_operations = ListOperations()

    sorted_values = [int(x) for x in input("Enter a list of sorted values, separated by spaces: ").split()]
    unsorted_values = sorted_values.copy()

    search_value = int(input("Enter the value to search: "))
    insert_value = int(input("Enter the value to insert: "))
    index = int(input("Enter the index to insert the value (or leave empty for default): "))
    delete_value = int(input("Enter the value to delete: "))

    for value in sorted_values:
        sorted_operations.insert(value)
    for value in unsorted_values:
        unsorted_operations.insert(value)

    sorted_search_time = sorted_operations.search(search_value)
    sorted_insert_time = sorted_operations.insert(insert_value, index)
    sorted_delete_time = sorted_operations.delete(delete_value)

    unsorted_search_time = unsorted_operations.search(search_value)
    unsorted_insert_time = unsorted_operations.insert(insert_value, index)
    unsorted_delete_time = unsorted_operations.delete(delete_value)

    print("\nOperations completed.\n")

    print("Sorted List:")
    print(sorted_operations.data)
    print(f"Search Time: {sorted_search_time:.6f} s, Insert Time: {sorted_insert_time:.6f} s, Delete Time: {sorted_delete_time:.6f} s")

    print("\nUnsorted List:")
    print(unsorted_operations.data)
    print(f"Search Time: {unsorted_search_time:.6f} s, Insert Time: {unsorted_insert_time:.6f} s, Delete Time: {unsorted_delete_time:.6f} s")

if __name__ == "__main__":
    main()
