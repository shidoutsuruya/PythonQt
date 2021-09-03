#include "dragwidget.h"
#include "ui_dragwidget.h"

DragWidget::DragWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::DragWidget)
{
    ui->setupUi(this);
}

DragWidget::~DragWidget()
{
    delete ui;
}

void DragWidget::on_rbtListSource_clicked()
{

}

void DragWidget::on_rbtListWidget_clicked()
{

}

void DragWidget::on_rbtTreeWidget_clicked()
{

}

void DragWidget::on_rbtTableWidget_clicked()
{

}

void DragWidget::on_checkBox_1_clicked()
{

}

void DragWidget::on_checkBox_2_clicked()
{

}

void DragWidget::on_comboBox_1_currentIndexChanged(const QString &arg1)
{

}

void DragWidget::on_comboBox_2_currentIndexChanged(int index)
{

}
