[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/rinoo9/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/rinoo9/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

# The Robot Apology

Entry for the make.fun bounty [The Robot Apology](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) ($2 USDC, 1st place). The program writes a two-line robot confession to `/output/entry.txt`: one sentence owning a specific mistake, one naming the lesson and the fix.

> I am sorry I replied-all to the entire company with the draft that said 'nobody will ever read this', because I thought the send button was the save button and I only noticed when the CEO replied 'noted'.
>
> I have learned that a button's label is a promise, so from now on I will read the button twice and send nothing I would not say to the whole building at once.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program validates the entry (exactly 2 lines, 1–400 UTF-8 characters) and exits non-zero if it is invalid.
