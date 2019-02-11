
class Node:
    def __init__(self, id, pid, item=None):
        self.id = id
        self.pid = pid
        self.item = item
        self.child = []

    def add_child(self, node):
        self.child.append(node)

    def __repr__(self):
        return '{}: {}'.format(self.id, self.pid)

    def to_json(self):
        child = []
        for node in self.child:
            child.append(node.to_json())

        rv = {'id': self.id, 'pid': self.pid}
        if self.item:
            rv.update(self.item.to_dict())

        if child:
            rv['child'] = child

        return rv


class NodeManager:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_root(self):
        root_nodes = []
        for node in self.nodes:
            if node.pid == 0:
                root_nodes.append(node)

        return root_nodes

    def get_node(self, id):
        for node in self.nodes:
            if node.id == id:
                return node

        return None

    def to_json(self):
        for node in self.nodes:
            if node.pid != 0:
                parent_node = self.get_node(node.pid)
                if parent_node:
                    parent_node.add_child(node)

        return self.get_root()