import matplotlib.pyplot as plt
import matplotlib.patches as patches

class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.allocated = False
        self.process_id = None

    def __str__(self):
        status = "Allocated" if self.allocated else "Free"
        return f"Size: {self.size}, Status: {status}, Process: {self.process_id if self.allocated else 'N/A'}"


class MemoryAllocator:
    def __init__(self, total_memory, block_sizes):
        self.memory = [MemoryBlock(size) for size in block_sizes]
        self.total_memory = total_memory
        self.fig, self.ax = plt.subplots(figsize=(10, 2))
        self.visualize_memory(init=True)

    def allocate(self, process_id, required_size):
        """
        Allocates memory to a process using the First Fit algorithm.
        :param process_id: Identifier of the process.
        :param required_size: Size of memory required by the process.
        :return: True if allocated, False otherwise.
        """
        for block in self.memory:
            if not block.allocated and block.size >= required_size:
                block.allocated = True
                block.process_id = process_id
                print(f"Process {process_id} allocated {required_size} units.")
                self.visualize_memory()
                return True
        print(f"Process {process_id} could not be allocated {required_size} units.")
        return False

    def deallocate(self, process_id):
        """
        Deallocates memory occupied by a specific process.
        :param process_id: Identifier of the process to deallocate.
        :return: True if deallocated, False otherwise.
        """
        for block in self.memory:
            if block.allocated and block.process_id == process_id:
                block.allocated = False
                block.process_id = None
                print(f"Process {process_id} deallocated.")
                self.visualize_memory()
                return True
        print(f"No memory block found for Process {process_id}.")
        return False

    def display_memory(self):
        """
        Displays the current status of memory blocks.
        """
        print("\nMemory Blocks:")
        for idx, block in enumerate(self.memory):
            print(f"Block {idx+1}: {block}")

    def fragmentation(self):
        """
        Calculates and displays the total external fragmentation.
        """
        fragmented_space = sum(block.size for block in self.memory if not block.allocated)
        print(f"\nTotal External Fragmentation: {fragmented_space} units")

    def visualize_memory(self, init=False):
        """
        Visualizes the memory allocation using matplotlib.
        :param init: If True, initializes the plot.
        """
        if not init:
            self.ax.clear()

        start = 0
        for block in self.memory:
            color = "red" if block.allocated else "green"
            self.ax.add_patch(patches.Rectangle((start, 0), block.size, 1, color=color))
            text = f"{block.size}\n{'P' + str(block.process_id) if block.allocated else 'Free'}"
            self.ax.text(start + block.size / 2, 0.5, text, color="white", ha="center", va="center", fontsize=8)
            start += block.size

        self.ax.set_xlim(0, self.total_memory)
        self.ax.set_ylim(0, 1)
        self.ax.set_xlabel("Memory Units")
        self.ax.set_yticks([])
        self.ax.set_title("Memory Allocation Visualization")
        self.fig.canvas.draw()
        if init:
            plt.ion()
            plt.show()


if __name__ == "__main__":
    print("Welcome to the First Fit Memory Allocator")

    # Initialize memory blocks
    total_memory = int(input("Enter total memory size: "))
    block_sizes = list(map(int, input("Enter sizes of memory blocks separated by spaces: ").split()))

    allocator = MemoryAllocator(total_memory, block_sizes)

    while True:
        print("\nOptions:")
        print("1. Allocate Memory")
        print("2. Deallocate Memory")
        print("3. Display Memory")
        print("4. Show Fragmentation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            process_id = input("Enter Process ID: ")
            required_size = int(input("Enter size of memory required: "))
            allocator.allocate(process_id, required_size)

        elif choice == "2":
            process_id = input("Enter Process ID to deallocate: ")
            allocator.deallocate(process_id)

        elif choice == "3":
            allocator.display_memory()

        elif choice == "4":
            allocator.fragmentation()

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
