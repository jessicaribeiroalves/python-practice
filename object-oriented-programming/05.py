class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        splitted_path = path[1:].split("/")
        previous_directory = self._find_bottom_node(splitted_path[:-1])
        if splitted_path[-1] in previous_directory.children:
            raise ValueError("Directory already exists")
        new_directory = Directory(splitted_path[-1])
        previous_directory.add_node(new_directory)

    def create_file(self, path, contents):
        splitted_path = path[1:].split("/")
        previous_directory = self._find_bottom_node(splitted_path[:-1])
        if splitted_path[-1] in previous_directory.children:
            raise ValueError("File already exists")
        new_file = File(splitted_path[-1])
        previous_directory.add_node(new_file)
        new_file.write_contents(contents)

    def read_file(self, path):
        splitted_path = path[1:].split("/")
        previous_directory = self._find_bottom_node(splitted_path[:-1])
        if splitted_path[-1] not in previous_directory.children:
            raise ValueError("Invalid operation")
        return previous_directory.children[splitted_path[-1]].contents

    def delete_directory_or_file(self, path):
        splitted_path = path[1:].split("/")
        previous_directory = self._find_bottom_node(splitted_path[:-1])
        if splitted_path[-1] not in previous_directory.children:
            raise ValueError("Invalid operation")
        previous_directory.delete_node(splitted_path[-1])

    def size(self):
        return len(self.root)

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"

    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    def _find_bottom_node(self, node_names):
        previous_directory = self.root
        for name in node_names:
            if name not in previous_directory.children:
                raise ValueError("Directory does not exist")
            previous_directory = previous_directory.children[name]
            if not isinstance(previous_directory, Directory):
                raise ValueError("Not a directory")
        return previous_directory


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __len__(self):
        return sum(len(child) for child in self.children.values())

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)
