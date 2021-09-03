#ifndef QLISTWIDGET_H
#define QLISTWIDGET_H

#include <QMainWindow>

namespace Ui {
class QListWidget;
}

class QListWidget : public QMainWindow
{
    Q_OBJECT

public:
    explicit QListWidget(QWidget *parent = nullptr);
    ~QListWidget();

private slots:
    void on_actionplus_triggered();

    void on_btnAll_triggered(QAction *arg1);

    void on_btnUnall_triggered(QAction *arg1);

    void on_actioninverse_triggered();

    void on_listWidget_currentItemChanged(QListWidgetItem *current, QListWidgetItem *previous);

    void on_listWidget_customContextMenuRequested(const QPoint &pos);

private:
    Ui::QListWidget *ui;
};

#endif // QLISTWIDGET_H
