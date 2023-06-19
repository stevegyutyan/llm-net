from llambdao import Message, Node


class FibonacciNode(Node):
    role = "system"

    def receive(self, message):
        a, b = 0, 1
        for _ in range(int(message.content)):
            yield Message(content=str(a), sender=self)
            a, b = b, a + b