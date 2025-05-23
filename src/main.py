from textnode import TextNode, TextType

def main():
    dummy_object = TextNode("Some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy_object)

main()
