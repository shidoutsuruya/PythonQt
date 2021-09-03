#include "qtmysql.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QtMySQL w;
    w.show();

    return a.exec();
}
