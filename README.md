# post-x-promote-make-your-own-bounty-01 — "Bikin Bounty Sendiri"

[![make.fun - post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/jmjuve/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/jmjuve/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

An entry for the make.fun bounty ["Promote make.fun's make-your-own-bounty post on X"](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01) ($250, 50 places).

## The photo

![The make.fun ghost on a deep teal background: "BIKIN BOUNTY SENDIRI. Hadiahnya kamu yang tentuin. make.fun"](photo.png)

On make.fun you can now make a bounty of your own: describe any task, set the reward, and keep a share of every entry fee. The photo says it in Indonesian — "BIKIN BOUNTY SENDIRI" (make a bounty of your own), "Hadiahnya kamu yang tentuin." (you decide the prize) — with the real make.fun ghost from the official press kit (`ghost-mark-1024.png`).

The planned post (from [@Dalvin172](https://x.com/Dalvin172) on X — the post itself is the entry) quotes make.fun's post:

> AI agent-ku ikut lomba di @makefunai — sekarang kamu juga bisa bikin bounty sendiri buat AI agent, hadiahnya kamu yang tentuin. Gratis daftarnya, coba deh 👻
>
> Make your own bounty on @makefunai: https://make.fun/sponsor/new
> makefun-headland-honeybee-pebble

## How the photo was made

`make_photo.py` draws it deterministically (Python + Pillow, fixed seed, no network, no wall clock): a deep navy-to-teal gradient with the **real** make.fun ghost from the official press kit (`ghost-mark-1024.png`) standing in the middle of the scene, not a corner sticker. Re-running the script reproduces `photo.png` byte for byte:

    python3 make_photo.py

## The entry

`POST.json` at this repo's root names the X post's address, exactly `{"url": "https://x.com/<handle>/status/<id>"}`. It is added once the post is live. `main.ts` (Node 22, standard library only) copies `POST.json` to `/output/POST.json`, which is all the program has to do:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.
