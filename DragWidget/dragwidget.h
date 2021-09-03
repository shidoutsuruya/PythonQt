#ifndef DRAGWIDGET_H
#define DRAGWIDGET_H

#include <QWidget>

namespace Ui {
class DragWidget;
}

class DragWidget : public QWidget
{
    Q_OBJECT

public:
    explicit DragWidget(QWidget *parent = nullptr);
    ~DragWidget();

private slots:
    void on_rbtListSource_clicked();

    void on_rbtListWidget_clicked();

    void on_rbtTreeWidget_clicked();

    void on_rbtTableWidget_clicked();

    void on_checkBox_1_clicked();

    void on_checkBox_2_clicked();

    void on_comboBox_1_currentIndexChanged(const QString &arg1);

    void on_comboBox_2_currentIndexChanged(int index);

private:
    Ui::DragWidget *ui;
};

#endif // DRAGWIDGET_H
