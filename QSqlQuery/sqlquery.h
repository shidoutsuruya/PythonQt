#ifndef SQLQUERY_H
#define SQLQUERY_H

#include <QMainWindow>

namespace Ui {
class SqlQuery;
}

class SqlQuery : public QMainWindow
{
    Q_OBJECT

public:
    explicit SqlQuery(QWidget *parent = nullptr);
    ~SqlQuery();

private:
    Ui::SqlQuery *ui;
};

#endif // SQLQUERY_H
