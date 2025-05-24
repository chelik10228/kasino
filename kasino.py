import random;
import time;

dep = input("Введи что ты хочешь депнуть в казик: ");
print(f"Ты депнул {dep} в казик");
time.sleep(2);
deplist = [f"Ты проиграл {dep} в казике :(", f"Ты выйграл 2 {dep} в казике! :)"];
print(random.choice(deplist));
