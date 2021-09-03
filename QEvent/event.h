#ifndef EVENT_H
#define EVENT_H

#include <QMainWindow>

namespace Ui {
class Event;
}

class Event : public QMainWindow
{
    Q_OBJECT

public:
    explicit Event(QWidget *parent = nullptr);
    ~Event();

private:
    Ui::Event *ui;
};

#endif // EVENT_H
