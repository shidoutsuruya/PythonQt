#include "qlistwidget.h"
#include "ui_qlistwidget.h"

QListWidget::QListWidget(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QListWidget)
{
    ui->setupUi(this);
}

QListWidget::~QListWidget()
{
    delete ui;
}

void QListWidget::on_actionplus_triggered()
{

}

void QListWidget::on_btnAll_triggered(QAction *arg1)
{

}

void QListWidget::on_btnUnall_triggered(QAction *arg1)
{

}

void QListWidget::on_actioninverse_triggered()
{

}

void QListWidget::on_listWidget_currentItemChanged(QListWidgetItem *current, QListWidgetItem *previous)
{

}

void QListWidget::on_listWidget_customContextMenuRequested(const QPoint &pos)
{

}
