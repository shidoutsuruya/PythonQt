#include "filesystemmodel.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    FileSystemModel w;
    w.show();

    return a.exec();
}
