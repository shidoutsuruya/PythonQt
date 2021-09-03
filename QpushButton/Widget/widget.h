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
    void on_underlineBtn_clicked();

    void on_leftBtn_clicked();

    void on_middleBtn_clicked();

    void on_rightBtn_clicked();

    void on_boldBtn_clicked();

    void on_rendonly_clicked();

    void on_enabled_clicked();

    void on_clearbtn_clicked();

    void on_boldBtn_clicked(bool checked);

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
