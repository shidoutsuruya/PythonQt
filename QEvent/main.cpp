#include "event.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Event w;
    w.show();

    return a.exec();
}
