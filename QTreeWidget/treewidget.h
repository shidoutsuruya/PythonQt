#ifndef TREEWIDGET_H
#define TREEWIDGET_H

#include <QMainWindow>

namespace Ui {
class TreeWidget;
}

class TreeWidget : public QMainWindow
{
    Q_OBJECT

public:
    explicit TreeWidget(QWidget *parent = nullptr);
    ~TreeWidget();

private slots:
    void on_actionAdd_triggered();

    void on_actionAddDocument_triggered();

    void on_treeWidget_currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous);

    void on_actionTraverse_triggered();

    void on_actionHeight_triggered();

    void on_actionFloat_triggered();

    void on_actionVisible_triggered();

    void on_dockWidget_topLevelChanged(bool topLevel);

    void on_dockWidget_visibilityChanged(bool visible);

    void on_actionExit_destroyed();

private:
    Ui::TreeWidget *ui;
};

#endif // TREEWIDGET_H
