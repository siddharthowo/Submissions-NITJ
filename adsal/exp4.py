class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        new_node= SNode(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        new_node = SNode(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        print(f"Inserted {data} at the end.")

    def delete(self, key):
        curr = self.head
        if not curr:
            print("List is empty.")
            return

        if curr.data == key:
            self.head = curr.next
            print(f"Deleted {key}.")
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if not curr:
            print(f"Value {key} not found.")
            return

        prev.next = curr.next
        print(f"Deleted {key}.")

    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(f"{curr.data},", end=" ")
            curr = curr.next


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        new_node = DNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        print(f"Inserted {data} at the end.")

    def delete(self, key):
        curr = self.head
        if not curr:
            print("List is empty.")
            return

        while curr and curr.data != key:
            curr = curr.next

        if not curr:
            print(f"Value {key} not found.")
            return

        if curr == self.head:
            self.head = curr.next
            if self.head: #if list isnt empty after del
                self.head.prev = None
        else:
            if curr.next:
                curr.next.prev = curr.prev
            if curr.prev:
                curr.prev.next = curr.next
        print(f"Deleted {key}.")

    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(f"{curr.data},", end=" ")
            curr = curr.next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        new_node = SNode(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_end(self, data):
        new_node = SNode(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
        print(f"Inserted {data} at the end.")

    def delete(self, key):
        if not self.head:
            print("List is empty.")
            return

        curr = self.head

        #head contains key
        if curr.data == key:
            if curr.next == self.head: #only one node
                self.head = None
                print(f"Deleted {key}.")
                return
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            print(f"Deleted {key}.")
            return

        #key is in other nodes
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                print(f"Deleted {key}.")
                return
            prev = curr
            curr = curr.next

        print(f"Value {key} not found.")

    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while True:
            print(f"{curr.data},", end=" ")
            curr = curr.next
            if curr == self.head:
                break

def menu(ll_instance, list_name):
    while True:
        print(f"\n{list_name} Operations")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Delete by value")
        print("4. Traverse")
        print("5. Back to main menu")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            val = input("Enter value to insert: ").strip()
            ll_instance.insert_beg(val)
        elif choice == "2":
            val = input("Enter value to insert: ").strip()
            ll_instance.insert_end(val)
        elif choice == "3":
            val = input("Enter value to delete: ").strip()
            ll_instance.delete(val)
        elif choice == "4":
            ll_instance.traverse()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please select 1-5.")

sll = SinglyLinkedList()
dll = DoublyLinkedList()
cll = CircularLinkedList()

while True:
    print("1. Singly Linked List (SLL)")
    print("2. Doubly Linked List (DLL)")
    print("3. Circular Linked List (CLL)")
    print("4. Exit")
    choice = input("Select List Type (1-4): ").strip()

    if choice == "1":
        menu(sll, "Singly Linked List")
    elif choice == "2":
        menu(dll, "Doubly Linked List")
    elif choice == "3":
        menu(cll, "Circular Linked List")
    elif choice == "4":
        print("Exiting program.")
        exit()
    else:
        print("Invalid choice, please select 1-4.")
