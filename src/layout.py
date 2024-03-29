# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"res/icon/logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionValidate = QAction(MainWindow)
        self.actionValidate.setObjectName(u"actionValidate")
        icon1 = QIcon()
        icon1.addFile(u"res/icon/validate_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionValidate.setIcon(icon1)
        self.actionIndicate_Element = QAction(MainWindow)
        self.actionIndicate_Element.setObjectName(u"actionIndicate_Element")
        icon2 = QIcon()
        icon2.addFile(u"res/icon/indicate_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionIndicate_Element.setIcon(icon2)
        self.actionIndicate_Anchor = QAction(MainWindow)
        self.actionIndicate_Anchor.setObjectName(u"actionIndicate_Anchor")
        icon3 = QIcon()
        icon3.addFile(u"res/icon/indicate_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionIndicate_Anchor.setIcon(icon3)
        self.actionRepair = QAction(MainWindow)
        self.actionRepair.setObjectName(u"actionRepair")
        icon4 = QIcon()
        icon4.addFile(u"res/icon/repair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRepair.setIcon(icon4)
        self.actionHighlight = QAction(MainWindow)
        self.actionHighlight.setObjectName(u"actionHighlight")
        icon5 = QIcon()
        icon5.addFile(u"res/icon/highlight_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHighlight.setIcon(icon5)
        self.actionOptions = QAction(MainWindow)
        self.actionOptions.setObjectName(u"actionOptions")
        icon6 = QIcon()
        icon6.addFile(u"res/icon/option.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOptions.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Vertical)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeElement = QTreeWidget(self.tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeElement.setHeaderItem(__qtreewidgetitem)
        self.treeElement.setObjectName(u"treeElement")
        self.treeElement.setFrameShape(QFrame.NoFrame)
        self.treeElement.header().setVisible(False)

        self.horizontalLayout.addWidget(self.treeElement)

        self.tabWidget.addTab(self.tab, "")
        self.splitter.addWidget(self.tabWidget)
        self.tabWidget_2 = QTabWidget(self.splitter)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableProperty = QTableWidget(self.tab_3)
        self.tableProperty.setObjectName(u"tableProperty")
        self.tableProperty.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.tableProperty)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.splitter.addWidget(self.tabWidget_2)
        self.splitter_2.addWidget(self.splitter)
        self.tabWidget_3 = QTabWidget(self.splitter_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy1)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter_4 = QSplitter(self.tab_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(6)
        sizePolicy2.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy2)
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.listSelector = QListWidget(self.splitter_3)
        self.listSelector.setObjectName(u"listSelector")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listSelector.sizePolicy().hasHeightForWidth())
        self.listSelector.setSizePolicy(sizePolicy3)
        self.splitter_3.addWidget(self.listSelector)
        self.treeSelector = QTreeWidget(self.splitter_3)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeSelector.setHeaderItem(__qtreewidgetitem1)
        self.treeSelector.setObjectName(u"treeSelector")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.treeSelector.sizePolicy().hasHeightForWidth())
        self.treeSelector.setSizePolicy(sizePolicy4)
        self.splitter_3.addWidget(self.treeSelector)
        self.splitter_4.addWidget(self.splitter_3)
        self.textSelector = QTextEdit(self.splitter_4)
        self.textSelector.setObjectName(u"textSelector")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.textSelector.sizePolicy().hasHeightForWidth())
        self.textSelector.setSizePolicy(sizePolicy5)
        self.splitter_4.addWidget(self.textSelector)

        self.horizontalLayout_3.addWidget(self.splitter_4)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.splitter_2.addWidget(self.tabWidget_3)

        self.verticalLayout.addWidget(self.splitter_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setMinimumSize(QSize(0, 35))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.txtSelectorElement = QLineEdit(self.frame)
        self.txtSelectorElement.setObjectName(u"txtSelectorElement")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.txtSelectorElement.sizePolicy().hasHeightForWidth())
        self.txtSelectorElement.setSizePolicy(sizePolicy7)
        self.txtSelectorElement.setMinimumSize(QSize(260, 0))
        self.txtSelectorElement.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txtSelectorElement)

        self.btnSelectorElement = QPushButton(self.frame)
        self.btnSelectorElement.setObjectName(u"btnSelectorElement")
        sizePolicy7.setHeightForWidth(self.btnSelectorElement.sizePolicy().hasHeightForWidth())
        self.btnSelectorElement.setSizePolicy(sizePolicy7)
        icon7 = QIcon()
        icon7.addFile(u"res/icon/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSelectorElement.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.btnSelectorElement)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy8)
        self.widget.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_4.addWidget(self.widget)

        self.txtSelectorAnchor = QLineEdit(self.frame)
        self.txtSelectorAnchor.setObjectName(u"txtSelectorAnchor")
        sizePolicy7.setHeightForWidth(self.txtSelectorAnchor.sizePolicy().hasHeightForWidth())
        self.txtSelectorAnchor.setSizePolicy(sizePolicy7)
        self.txtSelectorAnchor.setMinimumSize(QSize(260, 0))
        self.txtSelectorAnchor.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txtSelectorAnchor)

        self.btnSelectorAnchor = QPushButton(self.frame)
        self.btnSelectorAnchor.setObjectName(u"btnSelectorAnchor")
        sizePolicy7.setHeightForWidth(self.btnSelectorAnchor.sizePolicy().hasHeightForWidth())
        self.btnSelectorAnchor.setSizePolicy(sizePolicy7)
        self.btnSelectorAnchor.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.btnSelectorAnchor)

        self.lblAPI = QLabel(self.frame)
        self.lblAPI.setObjectName(u"lblAPI")
        self.lblAPI.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lblAPI)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionValidate)
        self.toolBar.addAction(self.actionIndicate_Element)
        self.toolBar.addAction(self.actionIndicate_Anchor)
        self.toolBar.addAction(self.actionRepair)
        self.toolBar.addAction(self.actionHighlight)
        self.toolBar.addAction(self.actionOptions)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"tdSelector", None))
        self.actionValidate.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.actionIndicate_Element.setText(QCoreApplication.translate("MainWindow", u"Indicate Element", None))
        self.actionIndicate_Anchor.setText(QCoreApplication.translate("MainWindow", u"Indicate Anchor", None))
        self.actionRepair.setText(QCoreApplication.translate("MainWindow", u"Repair", None))
        self.actionHighlight.setText(QCoreApplication.translate("MainWindow", u"Highlight", None))
        self.actionOptions.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Visual Tree", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Property Explorer", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Selector Editor", None))
        self.btnSelectorElement.setText("")
        self.btnSelectorAnchor.setText("")
        self.lblAPI.setText(QCoreApplication.translate("MainWindow", u"tdAPI v0.1.1", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

