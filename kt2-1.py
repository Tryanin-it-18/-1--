import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.codes = {}
        self.root = None
        self._build_tree()

    def _build_tree(self):
        if not self.text:
            return

        freq_dict = Counter(self.text)
        heap = []

        for char, freq in freq_dict.items():
            node = Node(char, freq)
            heapq.heappush(heap, node)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        self.root = heap[0] if heap else None
        self._generate_codes(self.root, "")

    def _generate_codes(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            return

        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root

        if node.char is not None:
            char_display = f"'{node.char}'" if node.char != ' ' else "[space]"
            print(prefix + ("├─0─ " if is_left else "└─1─ ") + f"{char_display}")
        else:
            print(prefix + ("├─0─ " if is_left else "└─1─ ") + "•")

        new_prefix = prefix + ("│    " if is_left else "     ")

        if node.left:
            self.print_tree(node.left, new_prefix, True)
        if node.right:
            self.print_tree(node.right, new_prefix, False)

    def print_codes(self):
        print("Коды Хаффмана:")
        for char, code in sorted(self.codes.items()):
            if char == ' ':
                print(f"  [пробел]: {code}")
            else:
                print(f"  {char}: {code}")


def main():
    text = input("Введите фразу: ").strip()

    if not text:
        print("Ошибка: пустая строка")
        return

    huffman = HuffmanTree(text)

    print(f"\nИсходный текст: '{text}'")
    print(f"Уникальных символов: {len(set(text))}")

    huffman.print_codes()

    print("\nДерево Хаффмана:")
    print("(0 - левая ветвь, 1 - правая ветвь)")
    huffman.print_tree()


if __name__ == "__main__":
    main()