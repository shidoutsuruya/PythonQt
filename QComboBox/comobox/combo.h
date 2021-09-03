#ifndef COMBO_H
#define COMBO_H

#include <QMainWindow>

namespace Ui {
class combo;
}

class combo : public QMainWindow
{
    Q_OBJECT

public:
    explicit combo(QWidget *parent = nullptr);
    ~combo();

private:
    Ui::combo *ui;
};

#endif // COMBO_H
