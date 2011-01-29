#include <QtGui/QApplication>
#include "bob.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Bob w;
    w.show();

    return a.exec();
}
