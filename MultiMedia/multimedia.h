#ifndef MULTIMEDIA_H
#define MULTIMEDIA_H

#include <QWidget>

namespace Ui {
class multimedia;
}

class multimedia : public QWidget
{
    Q_OBJECT

public:
    explicit multimedia(QWidget *parent = nullptr);
    ~multimedia();

private slots:
    void on_btnAdd_clicked();

    void on_btnDelete_clicked();

private:
    Ui::multimedia *ui;
};

#endif // MULTIMEDIA_H
