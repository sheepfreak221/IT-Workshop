#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hideTextInBMP(const char *bmpFile, const char *textFile) {
    FILE *bmp = fopen(bmpFile, "rb+");
    FILE *text = fopen(textFile, "rb");
    
    if (!bmp || !text) {
        printf("Fehler beim Öffnen der Dateien.\n");
        return;
    }

    // BMP Header lesen
    fseek(bmp, 0, SEEK_END);
    long bmpSize = ftell(bmp);
    fseek(bmp, 0, SEEK_SET);

    // Textdatei lesen
    fseek(text, 0, SEEK_END);
    long textSize = ftell(text);
    fseek(text, 0, SEEK_SET);

    // Überprüfen, ob genug Platz im BMP ist
    if (textSize + 1 > bmpSize - sizeof(unsigned int)) {
        printf("Nicht genug Platz im BMP-Bild.\n");
        fclose(bmp);
        fclose(text);
        return;
    }

    // Text in BMP schreiben
    fseek(bmp, bmpSize - textSize - 1, SEEK_SET);
    fwrite(text, 1, textSize, bmp);
    fputc('\0', bmp); // Nullterminator hinzufügen

    fclose(bmp);
    fclose(text);
    printf("Text erfolgreich im BMP versteckt.\n");
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Verwendung: %s <bmp-file> <text-file>\n", argv[0]);
        return 1;
    }

    hideTextInBMP(argv[1], argv[2]);
    return 0;
}
