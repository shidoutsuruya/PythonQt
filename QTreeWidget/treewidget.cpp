#include "treewidget.h"
#include "ui_treewidget.h"

TreeWidget::TreeWidget(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TreeWidget)
{
    ui->setupUi(this);
}

TreeWidget::~TreeWidget()
{
    delete ui;
}

void TreeWidget::on_actionAdd_triggered()
{

}

void TreeWidget::on_actionAddDocument_triggered()
{

}

void TreeWidget::on_treeWidget_currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous)
{

}

void TreeWidget::on_actionTraverse_triggered()
{

}

void TreeWidget::on_actionHeight_triggered()
{

}

void TreeWidget::on_actionFloat_triggered()
{

}

void TreeWidget::on_actionVisible_triggered()
{

}

void TreeWidget::on_dockWidget_topLevelChanged(bool topLevel)
{

}

void TreeWidget::on_dockWidget_visibilityChanged(bool visible)
{

}

void TreeWidget::on_actionExit_destroyed()
{

}
