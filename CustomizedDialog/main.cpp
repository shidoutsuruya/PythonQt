#include "customdialog.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CustomDialog w;
    w.show();

    return a.exec();
}
