class Stack:
    def init(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def search(self, item):
        try:
            index = len(self.items) - self.items[::-1].index(item)
            return len(self.items) - index
        except ValueError:
            return -1

    def empty(self):
        return len(self.items) == 0


st = Stack()

st.push("Aku")
st.push("Anak")
st.push("Indonesia")

print("Next :", st.peek())
st.push("Raya")
print(st.pop())
st.push("!")

count = st.search("Aku")
while count != -1 and count > 1:
    st.pop()
    count -= 1

print(st.pop())
print(st.empty())