#ifndef PAINTER_H
#define PAINTER_H

#include <QMainWindow>

namespace Ui {
class Painter;
}

class Painter : public QMainWindow
{
    Q_OBJECT

public:
    explicit Painter(QWidget *parent = nullptr);
    ~Painter();

private:
    Ui::Painter *ui;
};

#endif // PAINTER_H
