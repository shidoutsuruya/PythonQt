#include "sqlquery.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SqlQuery w;
    w.show();

    return a.exec();
}
