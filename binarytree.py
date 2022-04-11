# return an in-order list of all items in this binary search tree.
def items_in_order(self):
    """Return an in-order list of all items in this binary search tree."""
    items = []
    if not self.is_empty():
        # Traverse tree in-order from root, appending each node's item
        self._traverse_in_order_recursive(self.root, items.append)
    # Return in-order list of all items in tree
    return items
