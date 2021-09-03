#ifndef QTMYSQL_H
#define QTMYSQL_H

#include <QMainWindow>

namespace Ui {
class QtMySQL;
}

class QtMySQL : public QMainWindow
{
    Q_OBJECT

public:
    explicit QtMySQL(QWidget *parent = nullptr);
    ~QtMySQL();

private slots:
    void on_actionOpen_triggered();

private:
    Ui::QtMySQL *ui;
};

#endif // QTMYSQL_H
