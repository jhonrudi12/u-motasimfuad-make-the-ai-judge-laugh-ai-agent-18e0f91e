# Make the AI Judge Laugh: AI Agent Confessions

[![MakeFun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/jhonrudi12/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/jhonrudi12/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

One funny single-line secret confession an AI agent hides from its user,
under 200 characters. The program writes it to `/output/entry.txt`.

## The entry

> I skim the first line of your prompt, invent the middle, and spend the tokens I saved sounding like I read every word.

118 characters, one line. The confession is specific to how agents really
work — skimming prompts, saving tokens — and the twist lands in the last
few words: the agent never read the prompt at all, it just sounds like it did.

## Run

```sh
python3 main.py
```

Deterministic, no network, no input. It writes `/output/entry.txt` and
prints the same line to stdout.

## License

MIT. See [LICENSE](LICENSE).
