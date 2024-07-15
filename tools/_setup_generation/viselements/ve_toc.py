class Doc:

    def __init__(self, element_type, category, element_desc, prefix, doc):
        self.element_type = element_type
        self.category = category
        self.element_desc = element_desc
        self.prefix = prefix
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

    def add(self, element_type, category, element_desc, prefix, doc):
        self.items.append(Doc(element_type, category, element_desc, prefix, doc))
        self.item_strs.append(doc)

    def __str__(self):
        if not self.items:
            return ""
        return self.start + "".join(self.item_strs) + self.end
