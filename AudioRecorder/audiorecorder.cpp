#include "audiorecorder.h"
#include "ui_audiorecorder.h"

AudioRecorder::AudioRecorder(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::AudioRecorder)
{
    ui->setupUi(this);
}

AudioRecorder::~AudioRecorder()
{
    delete ui;
}

void AudioRecorder::on_actionExit_triggered()
{

}
