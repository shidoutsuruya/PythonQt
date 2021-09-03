#ifndef RELATIONTABLE_H
#define RELATIONTABLE_H

#include <QMainWindow>

namespace Ui {
class relationTable;
}

class relationTable : public QMainWindow
{
    Q_OBJECT

public:
    explicit relationTable(QWidget *parent = nullptr);
    ~relationTable();

private slots:
    void on_actionExit_triggered();

private:
    Ui::relationTable *ui;
};

#endif // RELATIONTABLE_H
