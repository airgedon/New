#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *encrypt(char *text, int key) {
  char *encryptedText = malloc(sizeof(char) * strlen(text) + 1);
  strcpy(encryptedText, text);

  for (int i = 0; i < strlen(text); i++) {
    encryptedText[i] += key;
  }

  return encryptedText;
}

char *decrypt(char *encryptedText, int key) {
  char *decryptedText = malloc(sizeof(char) * strlen(encryptedText) + 1);
  strcpy(decryptedText, encryptedText);

  for (int i = 0; i < strlen(encryptedText); i++) {
    decryptedText[i] -= key;
  }

  return decryptedText;
}

int main() {
  char text[100];
  int key = 10;
  char choice[10];

  printf("Enter the text you want to encrypt: ");
  scanf("%s", text);

  char *encryptedText = encrypt(text, key);
  printf("Encrypted text: %s\n", encryptedText);

  printf("Would you like to decrypt the message (yes/no): ");
  scanf("%s", choice);

  if (strcmp(choice, "yes") == 0) {
    char *decryptedText = decrypt(encryptedText, key);
    printf("Decrypted text: %s\n", decryptedText);

    free(decryptedText);
  }

  free(encryptedText);

  return 0;
}
