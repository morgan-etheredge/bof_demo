#include <stdio.h>

void vuln() {
    char buf[50];
    gets(buf);
}

int main(int argc, char *argv[]) {
    vuln();
    return 0;
}
