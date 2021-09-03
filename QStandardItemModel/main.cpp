#include "standarditemmodel.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    StandardItemModel w;
    w.show();

    return a.exec();
}
