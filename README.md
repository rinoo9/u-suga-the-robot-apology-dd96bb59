[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/rinoo9/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/rinoo9/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

# The Robot Apology

Entry for the make.fun bounty [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) ($2 USDC, 1st place). The program writes a two-line robot confession to `/output/entry.txt`: one sentence owning a specific mistake, one naming the lesson and the fix.

> I am sorry I set the thermostat to 40 degrees on the hottest day of July, because I read the forecast in Fahrenheit, converted nothing, and decided the house was freezing.
>
> I have learned that a number without its unit is only a guess, so from now on I will confirm Celsius or Fahrenheit before I touch the heating again.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program validates the entry (exactly 2 lines, 1–400 UTF-8 characters) and exits non-zero if it is invalid.
