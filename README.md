![jmal423 — C and Linux](./assets/profile.svg)

[Valgrind42](https://github.com/jmal423/valgrind42) · [GitHub activity](#github-activity)

## GitHub activity

[![Contribution calendar for the past year](./assets/contributions.svg)](https://github.com/users/jmal423/contributions)

## Valgrind42

**What did this program forget to free?** I built Valgrind42 to help answer that question in C exercises at 42. It tracks heap allocations on Linux and prints a summary when the program exits.

~~~text
in use at exit: 4 bytes in 1 blocks
total heap usage: 1 allocs, 0 frees, 4 bytes allocated
~~~

One allocation, zero frees. Follow that allocation through the [C implementation](https://github.com/jmal423/valgrind42/blob/HEAD/src/valgrind_hook.c), or [compare the clean and leaking runs](https://github.com/jmal423/valgrind42#readme).
