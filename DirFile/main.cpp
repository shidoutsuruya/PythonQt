#include "dirfile.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    DirFile w;
    w.show();

    return a.exec();
}
