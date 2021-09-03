#include "multimedia.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    multimedia w;
    w.show();

    return a.exec();
}
