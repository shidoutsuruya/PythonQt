#ifndef DIRFILE_H
#define DIRFILE_H

#include <QMainWindow>

namespace Ui {
class DirFile;
}

class DirFile : public QMainWindow
{
    Q_OBJECT

public:
    explicit DirFile(QWidget *parent = nullptr);
    ~DirFile();

private:
    Ui::DirFile *ui;
};

#endif // DIRFILE_H
