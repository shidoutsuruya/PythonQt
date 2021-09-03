#ifndef WIDGET_H
#define WIDGET_H

#include <QMainWindow>

namespace Ui {
class Widget;
}

class Widget : public QMainWindow
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void on_pushButton_clicked();

    void on_spinBox_valueChanged(int arg1);

    void on_spinBox_valueChanged(const QString &arg1);

    void on_doubleSpinBox_valueChanged(const QString &arg1);

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
