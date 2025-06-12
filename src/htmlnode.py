class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("value must be here")
        if self.tag == None:
            return str(self.value)
        return self.tag

    def props_to_html(self):
        html_props = ""
        if self.props == None:
            return ""
        for attribute in self.props:
            value = self.props[attribute]
            attribute_to_add = " " + str(attribute) + '="' + str(value) + '"'
            html_props += attribute_to_add
        return html_props

    def __repr__(self):
        return (
            "HTMLNode(\n"
            f"  tag={self.tag}, \n"
            f"  value={self.value}, \n"
            f"  children={self.children}, \n"
            f"  props={self.props}\n"
            ")"
            )

    def __eq__(self, other):
        return (
        self.tag == other.tag
        and self.value == other.value
        and self.children == other.children
        and self.props == other.props
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
