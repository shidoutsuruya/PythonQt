#ifndef AUDIOINPUT_H
#define AUDIOINPUT_H

#include <QMainWindow>

namespace Ui {
class AudioInput;
}

class AudioInput : public QMainWindow
{
    Q_OBJECT

public:
    explicit AudioInput(QWidget *parent = nullptr);
    ~AudioInput();

private slots:
    void on_actionStart_triggered();

private:
    Ui::AudioInput *ui;
};

#endif // AUDIOINPUT_H
