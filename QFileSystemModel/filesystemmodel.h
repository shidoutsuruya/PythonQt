#ifndef FILESYSTEMMODEL_H
#define FILESYSTEMMODEL_H

#include <QMainWindow>

namespace Ui {
class FileSystemModel;
}

class FileSystemModel : public QMainWindow
{
    Q_OBJECT

public:
    explicit FileSystemModel(QWidget *parent = nullptr);
    ~FileSystemModel();

private slots:
    void on_treeView_clicked(const QModelIndex &index);

private:
    Ui::FileSystemModel *ui;
};

#endif // FILESYSTEMMODEL_H
