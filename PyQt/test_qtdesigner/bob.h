#ifndef BOB_H
#define BOB_H

#include <QMainWindow>

namespace Ui {
    class Bob;
}

class Bob : public QMainWindow
{
    Q_OBJECT

public:
    explicit Bob(QWidget *parent = 0);
    ~Bob();

private:
    Ui::Bob *ui;
};

#endif // BOB_H
