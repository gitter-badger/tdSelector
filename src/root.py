from tdWindows import tdWindows as td

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTreeWidgetItem


def load(ui):
    element=td.getRootElement()
    tree=ui.treeElement
    
    rootNode=QTreeWidgetItem(tree,[element.text])
    rootNode.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
    rootNode.setData(1,Qt.DisplayRole,element)
    
    tree.itemExpanded.connect(onExpandItem)
        
    tree.expandItem(rootNode)
    
    
def onExpandItem(item):
    element=item.data(1,Qt.DisplayRole)
    children=element.children
    for child in children:
        text=child.text
        childNode=QTreeWidgetItem(item,[text])
        childNode.setToolTip(0,text)
        if len(child.children)==0:
            childNode.setChildIndicatorPolicy(QTreeWidgetItem.DontShowIndicator)
        else:
            childNode.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        childNode.setData(1,Qt.DisplayRole,child)