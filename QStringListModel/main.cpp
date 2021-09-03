#include "qstringlistmodel.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QStringListModel w;
    w.show();

    return a.exec();
}
