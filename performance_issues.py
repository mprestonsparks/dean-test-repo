# Sample Python code with performance issues for agent optimization testing

def inefficient_search(data_list, target):
    """
    Inefficient linear search - could be optimized with binary search for sorted data
    """
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1

def slow_string_concatenation(items):
    """
    Inefficient string concatenation - should use join()
    """
    result = ""
    for item in items:
        result += str(item) + ", "
    return result[:-2]  # Remove trailing comma

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