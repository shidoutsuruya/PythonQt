#include "qlistwidget.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QListWidget w;
    w.show();

    return a.exec();
}
