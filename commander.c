#include <stdio.h>
#include <string.h>

int main() {
    char password[20];
    printf("--- 🔐 ENTER NSA COMMAND CODE: ");
    scanf("%s", password);

    if (strcmp(password, "NSA2026") == 0) {
        printf("✅ ACCESS GRANTED. بەخێربێیت فەرماندە!\n");
    } else {
        printf("❌ ACCESS DENIED. هێرشەکە تومار کرا!\n");
    }
    return 0;
}
