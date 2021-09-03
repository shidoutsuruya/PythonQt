#ifndef STANDARDITEMMODEL_H
#define STANDARDITEMMODEL_H

#include <QMainWindow>

namespace Ui {
class StandardItemModel;
}

class StandardItemModel : public QMainWindow
{
    Q_OBJECT

public:
    explicit StandardItemModel(QWidget *parent = nullptr);
    ~StandardItemModel();

private slots:
    void on_actionfile_triggered();

    void on_actionDelete_row_triggered();

    void on_actionLeft_triggered();

    void on_actionCenter_triggered();

    void on_actionRight_triggered();

    void on_actionAdd_row_triggered();

    void on_actionBold_triggered();

    void on_actionmodel_data_triggered();

    void on_actionsave_triggered();

private:
    Ui::StandardItemModel *ui;
};

#endif // STANDARDITEMMODEL_H
