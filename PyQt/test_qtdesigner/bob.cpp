#include "bob.h"
#include "ui_bob.h"

Bob::Bob(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Bob)
{
    ui->setupUi(this);
}

Bob::~Bob()
{
    delete ui;
}
