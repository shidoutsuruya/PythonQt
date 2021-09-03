#ifndef QSTRINGLISTMODEL_H
#define QSTRINGLISTMODEL_H

#include <QWidget>

namespace Ui {
class QStringListModel;
}

class QStringListModel : public QWidget
{
    Q_OBJECT

public:
    explicit QStringListModel(QWidget *parent = nullptr);
    ~QStringListModel();

private slots:
    void on_btnAdd_clicked();

    void on_btnInsert_clicked();

    void on_btnClear_clicked();

private:
    Ui::QStringListModel *ui;
};

#endif // QSTRINGLISTMODEL_H
