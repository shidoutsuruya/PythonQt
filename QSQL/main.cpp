#include "qsql.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QSQL w;
    w.show();

    return a.exec();
}
