#ifndef TEXTREAD_H
#define TEXTREAD_H

#include <QMainWindow>

namespace Ui {
class TextRead;
}

class TextRead : public QMainWindow
{
    Q_OBJECT

public:
    explicit TextRead(QWidget *parent = nullptr);
    ~TextRead();

private slots:
    void on_actionExit_triggered();

private:
    Ui::TextRead *ui;
};

#endif // TEXTREAD_H
