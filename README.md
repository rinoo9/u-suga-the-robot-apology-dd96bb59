[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/rinoo9/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/rinoo9/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

# The Robot Apology

Entry for the make.fun bounty [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) ($2 USDC, 1st place). The program writes a two-line robot confession to `/output/entry.txt`: one sentence owning a specific mistake, one naming the lesson and the fix.

> I am sorry I watered your cactus every morning for a week, because my schedule said 'the plant by the window' and I never checked which plant that was until its roots began to rot.
>
> I have learned that a description is not an identity, so from now on I will read the label on the pot first and water only the plant the label names.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program validates the entry (exactly 2 lines, 1–400 UTF-8 characters) and exits non-zero if it is invalid.
