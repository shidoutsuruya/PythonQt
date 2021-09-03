#include "relationtable.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    relationTable w;
    w.show();

    return a.exec();
}
