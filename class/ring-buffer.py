
# The size of the queue = it is not allowed to grow!
N = 10

# The actual queue - only indexing (i.e. queue[<index>]) is alowed - no append()
queue = [None] * N

# Feel free to add more variables that you might need!


# TASK: Fill the four fucntions below with the correct implementation

def enqueue(element: any) -> bool:
    """Enqueue the given element in the `queue`.

    Args:
        element (any): the element to be enqueue

    Returns:
        bool: If there were enough space and the element added
    """
    pass


def dequeue() -> any:
    """Dequeue an element from the `queue`.

    Returns:
        any: The dequeued element.
    """
    pass


def is_empty() -> bool:
    """Checks if the queue is empty

    Returns:
        bool: `True` if there are no elements in the queue
    """
    pass


def is_full() -> bool:
    """Checks if the `queue` is full, or it has space for more elements.

    Returns:
        bool: `True` if there is NO more space for elements
    """
    pass


assert (is_empty())
assert (not is_full())
assert (enqueue(5))
assert (not is_empty())
assert (enqueue(6))
assert (dequeue() == 5)
