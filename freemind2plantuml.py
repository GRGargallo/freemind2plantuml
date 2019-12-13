import argparse
import xml.etree.ElementTree as ET

def printNode(node, deep):
    deepString = deep * "*"
    line = deepString + " " 
    line = line + node.get("TEXT")
    print(line)

def recursiveNodes(node, deep):
    printNode(node,deep)
    childrens = node.getchildren()
    if len(childrens) == 0:
        return
    for child in childrens:
        recursiveNodes(child, deep+1)

        

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pathtofile', help='Path to file')
    args = parser.parse_args()
    tree = ET.parse(args.pathtofile)
    print("@startmindmap")
    recursiveNodes(tree.getroot().getchildren()[0], 1)
    print("@endmindmap")

if __name__ == "__main__":
    main()
