#ifndef DRAG_H
#define DRAG_H

#include <QWidget>

namespace Ui {
class Drag;
}

class Drag : public QWidget
{
    Q_OBJECT

public:
    explicit Drag(QWidget *parent = nullptr);
    ~Drag();

private:
    Ui::Drag *ui;
};

#endif // DRAG_H
