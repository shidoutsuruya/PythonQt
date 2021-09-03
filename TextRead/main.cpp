#include "textread.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    TextRead w;
    w.show();

    return a.exec();
}
