#include "audioinput.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    AudioInput w;
    w.show();

    return a.exec();
}
