/**
 * The main Tool class!
 */

#pragma once

#include <QMainWindow>
#include <QTabWidget>
#include <QPushButton>
#include <QToolBar>
#include <QScrollArea>
#include <QResizeEvent>
#include <QPixmap>
#include <QImage>
#include <QLabel>

#include "ToolDiagram.h"
#include "DataSelector.h"
#include "logview/LogViewer.h"

namespace tool {

class EmptyTool : public QMainWindow {
    Q_OBJECT;

public:
    EmptyTool(const char* title = "TOOL");
    ~EmptyTool();

public slots:
    void setUpModules();

protected:
    // For keyboard control
    virtual void keyPressEvent(QKeyEvent * event);

    void resizeEvent(QResizeEvent*);

    // Modules in this diagram will be run when data is updated
    ToolDiagram diagram;

    DataSelector selector;
    logview::LogViewer logView;
    // GUI stuff
    QTabWidget* toolTabs;
    QToolBar* toolbar;
    QPushButton* prevButton;
    QPushButton* nextButton;
    QPushButton* scrollButton;
    QScrollArea* scrollArea;
    QSize* scrollBarSize;
    QSize* tabStartSize;
    QRect* geometry;
};
}
