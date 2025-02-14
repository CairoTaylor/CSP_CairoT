//Cairo Taylor, Silly Sentences
#include <stdio.h>
// String variables for user inputs (minimum of 3)

char name[20];
char place[20];
char verbed[20];
int number1[20];
char object[20];
char cakeingredient[20];
char verbed2[20];
char verbed3[20];

int main(void){
printf("Hello. I am glad you are using my program. You see, you have invoked my power. My power is creating goofy and weird sentences.\nSo, when I ask you to fill in a word, please do so.\n");
printf("What is a male name?\n");
scanf("%s", name);
printf("What is the name of the place this guy lives in?\n");
scanf("%s", place);
printf("What is a verb?\n");
scanf("%s", verbed);
printf("What is your favorite number?\n");
scanf("%d", number1);
printf("What is a random object?\n");
scanf("%s", object);
printf("What is an ingredient in cake?\n");
scanf("%s", cakeingredient);
printf("What is a past-tense verb?\n");
scanf("%s", verbed2);
printf("What is another past-tense verb?\n");
scanf("%s", verbed3);
printf("One day, %s was walking down the street in %s, when suddenly, %d %ss showed up and tried to %s %s. But luckily, %s had experienced this before. So, he pulled out some %s and %s the %ss with it and then they %s, saving %s.", name, place, number1, object, verbed, name, name, cakeingredient, verbed2, object, verbed3, name);
// Insert variables into a sentence to show the user what monstrosity they have created (only 1 statement)

    return 0;
}