#ifndef AUDIORECORDER_H
#define AUDIORECORDER_H

#include <QMainWindow>

namespace Ui {
class AudioRecorder;
}

class AudioRecorder : public QMainWindow
{
    Q_OBJECT

public:
    explicit AudioRecorder(QWidget *parent = nullptr);
    ~AudioRecorder();

private slots:
    void on_actionExit_triggered();

private:
    Ui::AudioRecorder *ui;
};

#endif // AUDIORECORDER_H
