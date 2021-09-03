#ifndef GRAPHICSVIDEOITEM_H
#define GRAPHICSVIDEOITEM_H

#include <QMainWindow>

namespace Ui {
class GraphicsVideoItem;
}

class GraphicsVideoItem : public QMainWindow
{
    Q_OBJECT

public:
    explicit GraphicsVideoItem(QWidget *parent = nullptr);
    ~GraphicsVideoItem();

private slots:
    void on_pbtZoomIn_clicked();

    void on_pbtZoomOut_clicked();

    void on_pbtText_clicked();

private:
    Ui::GraphicsVideoItem *ui;
};

#endif // GRAPHICSVIDEOITEM_H
