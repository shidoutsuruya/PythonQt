#ifndef PLT_GUI_H
#define PLT_GUI_H

#include <QMainWindow>

namespace Ui {
class plt_gui;
}

class plt_gui : public QMainWindow
{
    Q_OBJECT

public:
    explicit plt_gui(QWidget *parent = nullptr);
    ~plt_gui();

private:
    Ui::plt_gui *ui;
};

#endif // PLT_GUI_H
