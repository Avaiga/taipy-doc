class VisualElement:

    def __init__(self, element_type, category, doc):
        self.element_type = element_type
        self.category = category
        self.doc = doc

    def __str__(self):
        return self.doc


class VEToc:

    def __init__(self, start: str, end: str, hook: str):
        self.start = start
        self.end = end
        self.hook = hook
        self.items = []
        self.item_strs = []

    def add(self, element_type, category, doc):
        self.items.append(VisualElement(element_type, category, doc))
        self.item_strs.append(doc)

    def __str__(self):
        if not self.items:
            return ""
        return self.start + "".join(self.item_strs) + self.end
