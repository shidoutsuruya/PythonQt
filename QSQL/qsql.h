#ifndef QSQL_H
#define QSQL_H

#include <QMainWindow>

namespace Ui {
class QSQL;
}

class QSQL : public QMainWindow
{
    Q_OBJECT

public:
    explicit QSQL(QWidget *parent = nullptr);
    ~QSQL();

private:
    Ui::QSQL *ui;
};

#endif // QSQL_H
