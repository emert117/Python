class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        return f"{self.name!r} Connected by: {self.connected_by}"

    def disconnect(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} remainig capacity: {self.remaining_pages}"

    def print_page(self, page_count):
        self.remaining_pages -= page_count

my_printer = Printer("HP 1100", "USB", 500)
my_printer.print_page(20)
print(my_printer)