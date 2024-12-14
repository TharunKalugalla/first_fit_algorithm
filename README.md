# First Fit Memory Allocator

This project simulates a dynamic memory allocation system using the **First Fit** algorithm. It includes visualization for better understanding and interaction through a console-based menu.

## Features
- **Dynamic Memory Allocation:** Allocate memory to processes using the First Fit algorithm.
- **Deallocation:** Release memory occupied by processes.
- **Visualization:** Real-time updates of memory status using Matplotlib.
- **Fragmentation Calculation:** Display total external fragmentation.
- **Interactive Console Menu:** Easy-to-use interface for managing memory operations.

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.9 or later
- Matplotlib library

To install Matplotlib, run:
```bash
pip install matplotlib
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/TharunKalugalla/first_fit_algorithm.git
```
2. Navigate to the project directory:
```bash
cd first-fit-memory-allocator
```

3. Run the program:
```bash
python first_fit_allocator.py
```

## How It Works
1. **Initialize Memory**: Define the total memory size and block sizes.
2. **Allocate Memory**: Assign memory blocks to processes based on their size requirements.
3. **Deallocate Memory**: Free memory blocks used by specific processes.
4. **View Visualization**: Dynamically updated graphical representation of memory allocation.
5. **Calculate Fragmentation**: See the total external fragmentation at any time.

## Sample Inputs and Outputs
### Input:
- Total memory: `100`
- Block sizes: `20 30 10 40`

### Actions:
1. Allocate 15 units for process `P1`.
2. Allocate 25 units for process `P2`.
3. Deallocate memory for process `P1`.
4. Allocate 35 units for process `P3`.

### Output:
- Visualization updates after each action.
- Messages in the console indicate successful allocation or deallocation.

## Code Structure
- **`MemoryBlock` Class**:
  Represents individual memory blocks with attributes for size, allocation status, and process ID.

- **`MemoryAllocator` Class**:
  Handles all memory operations including allocation, deallocation, and visualization.

- **Methods**:
  - `allocate`: Allocates memory to a process.
  - `deallocate`: Releases memory from a process.
  - `visualize_memory`: Updates the visualization.
  - `fragmentation`: Calculates total external fragmentation.

## Future Enhancements
- Add support for other memory allocation algorithms (e.g., Best Fit, Worst Fit).
- Implement a graphical user interface (GUI) for better user experience.
- Optimize the program for larger memory systems.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## Contact
For any inquiries, reach out at your-email@example.com.
