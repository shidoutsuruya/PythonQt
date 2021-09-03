#ifndef QT_H
#define QT_H

#include <QMainWindow>

namespace Ui {
class qt;
}

class qt : public QMainWindow
{
    Q_OBJECT

public:
    explicit qt(QWidget *parent = nullptr);
    ~qt();

private slots:
    void on_OK_clicked();

    void on_clear_clicked();

    void on_Bold_toggled(bool checked);

    void on_buttonBox_accepted();

    void on_Ok_clicked();

    void on_pushButton_clicked();

    void on_btnSetName_clicked();

    void on_SliderSetAge_sliderMoved(int position);

    void on_SliderSetAge_valueChanged(int value);

private:
    Ui::qt *ui;
};

#endif // QT_H
