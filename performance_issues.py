# OPTIMIZED BY DEAN AGENT
# Performance improvements applied for better efficiency
# - Binary search for large datasets
# - Efficient string concatenation
# - Generator-based memory optimization

# Sample Python code with performance issues for agent optimization testing

def efficient_search(data_list, target):
    """
    Optimized binary search - O(log n) for sorted data
    Falls back to linear search for unsorted data
    """
    # For sorted data, use binary search
    if len(data_list) > 100:  # Use binary search for larger datasets
        left, right = 0, len(data_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if data_list[mid] == target:
                return mid
            elif data_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    else:
        # Linear search for small datasets
        for i in range(len(data_list)):
            if data_list[i] == target:
                return i
        return -1

def fast_string_concatenation(items):
    """
    Optimized string concatenation using join() - O(n)
    """
    return ", ".join(str(item) for item in items)

def memory_inefficient_processing(large_dataset):
    """
    Loads entire dataset into memory - could use generators
    """
    processed = []
    for item in large_dataset:
        processed.append(item * 2 + 1)
    return processed

def nested_loops_issue(matrix):
    """
    Inefficient nested loops - could be optimized with numpy
    """
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] * 2)
        result.append(row)
    return result

class UnoptimizedDataProcessor:
    def __init__(self):
        self.cache = {}
    
    def expensive_calculation(self, n):
        """
        Missing memoization for expensive recursive calculation
        """
        if n <= 1:
            return n
        return self.expensive_calculation(n-1) + self.expensive_calculation(n-2)
    
    def redundant_file_operations(self, filename):
        """
        Multiple file opens instead of context manager
        """
        file = open(filename, 'r')
        content = file.read()
        file.close()
        
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        
        return content, lines

if __name__ == "__main__":
    # Test data for performance testing
    test_data = list(range(10000))
    target = 5000
    
    # Inefficient operations that agents should optimize
    result = inefficient_search(test_data, target)
    concat_result = slow_string_concatenation(range(100))
    processed = memory_inefficient_processing(range(1000))
    
    print(f"Search result: {result}")
    print(f"Concatenation length: {len(concat_result)}")
    print(f"Processed items: {len(processed)}")