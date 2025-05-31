class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

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
