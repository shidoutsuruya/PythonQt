#include "graphicsvideoitem.h"
#include "ui_graphicsvideoitem.h"

GraphicsVideoItem::GraphicsVideoItem(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::GraphicsVideoItem)
{
    ui->setupUi(this);
}

GraphicsVideoItem::~GraphicsVideoItem()
{
    delete ui;
}

void GraphicsVideoItem::on_pbtZoomIn_clicked()
{

}

void GraphicsVideoItem::on_pbtZoomOut_clicked()
{

}

void GraphicsVideoItem::on_pbtText_clicked()
{

}
