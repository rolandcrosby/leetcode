# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack == []:
            self.stack.append((x, x))
        else:
            last_min = self.stack[len(self.stack) - 1][1]
            if x < last_min:
                self.stack.append((x, x))
            else:
                self.stack.append((x, last_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]


if __name__ == "__main__":
    def example_test():
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        assert min_stack.getMin() == -3
        min_stack.pop()
        assert min_stack.top() == 0
        assert min_stack.getMin() == -2
    tests = [example_test]
    passed = 0
    for test in tests:
        test()
        passed += 1
    print("%d of %d tests passed" % (passed, len(tests)))
