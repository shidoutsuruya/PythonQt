#include "plt_gui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    plt_gui w;
    w.show();

    return a.exec();
}
