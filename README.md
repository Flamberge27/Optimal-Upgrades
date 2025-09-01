# Optimal Upgrades

<<<<<<< HEAD
This branch pares down the work of the main repository into more human-usable
data chunks. Specifically I'm filtering/sorting the CSV data via Excel to determine
a shortlist of the "best" module seeds for fully kitting yourself out.

## Preamble

You'll notice that each main folder (i.e. /Suit) has/will have a significiant number
of CSV files removed - those would be the files which contain data on modules that will
never be optimal, like the C-Rank ones.

In the Ship, Suit, and Weapon folders you'll notice a new file containing "Top 6s" in its
title. These will have ALL the top recommendations for that folder - e.g. "Suit Top 6" has
the 6 best X-Class mods for life support, hazard protection, movement, shields, and even
the top forbiddens.

Suit/Ship have a top 6 because you can apply mods in general inventory and in tech; Weapon
only needs top 3s.

## Usage

You'll need a save editor that allows you to edit your inventory and your module's seeds.
I recommend NomNom (https://github.com/cengelha/NomNom) . Once you load your save into
the editor, you'll want to click on an already-installed module and edit its seed to be
whichever you want.

To repeat - don't edit the seed of an unistalled module, it's not going to do much. Install
first (or generate an installed module), then edit that seed.

Save, and when you next load into the game, you should see that your module has the stats
you want it to.

## Notes

If you want to, you can also just use the same module seed 3x and 6x. I think this is less interesting.

You'll see a "Perfection" stat referenced over and over. The original creator devised it
as a weighted average of how good a mod's stats are against their theoretical maximum. They
scale from 0 to 1, with 1 meaning that a mod's stats are at their maximum. It's generally
pretty useful as an indicator of how generally good a mod is.
=======
![Maintained](https://img.shields.io/maintenance/yes/2025)
![GitHub Release](https://img.shields.io/github/v/release/zencq/Pi?display_name=release)
![GitHub Repo Size](https://img.shields.io/github/repo-size/zencq/Pi)
[![Supported by the No Man's Sky Community Developers & Designers](https://raw.githubusercontent.com/NMSCD/About/master/badge/purple.svg)](https://nmscd.com/)

This repository contains a collection of files with values of stats for every
**P**rocedural **I**tem in [No Man's Sky](https://www.nomanssky.com/). This includes
mainly technology upgrades but also the products (treasures/artifacts in-game).

## Usage

Each item has two files, one easier for humans to read (`.csv`) and one better for
programmatic processing (`.parquet`). Each file includes the seed, its weighted
perfection in percent, the actual stats, and the procedural name in different languages.
The files itself and the stats are named with the game internal names but you can
use them without any developer knowledge.

All values are shown without rounding and without regard to its sign as it does
not matter for the purpose of this. Most, but not all, stats are shown in a in-game
like form. If not, the raw value is used (e.g. `UP_RAIL1` always showed `+2%` but
actually had a range from `30` to `40`).

There is also the `Pi.xlsx` file which is a user friendly collection of best and
most desirable seeds. It is categorized by inventory type and contains the best
values for each stat per item in addition to those already mentioned.

<!-- ## Known Issues

The following items are currently *outdated* or *not available* due to changes in
a newer yet unsupported game version. All supported versions can be can be seen
below and the latest item update in the [releases here on GitHub](https://github.com/zencq/Pi/releases). -->

## How it works 2.2

The current implementation utilizes [NMS.py](https://github.com/monkeyman192/NMS.py)
by [monkeyman192](https://github.com/monkeyman192). NMS.py (and its backend [pyMHF](https://github.com/monkeyman192/pyMHF))
is included in this repository as submodules to ensure best compatibility.

Currently it is designed to work with GOG.com version 4.13 as well as 5.20 and 5.61
which cover all changes/additions since 4.13.

After cloning you must execute `git submodule update --init --recursive` in the
newly created directory to initialize the NMS.py and pyMHF submodules. Then install
both in your Python environment by changing into the respective directories, starting
with pyMHF and the command `pip install .` followed by NMS.py with `pip install --no-deps .`.
Finally adapt the inline [config](https://github.com/monkeyman192/pyMHF/blob/master/docs/settings.md)
at the top of the mod file to your needs and you are ready to go.

To run it, simply execute the command `pymhf run .\NMSpy_mods\Pi.py` and start the
binary when you are asked to. When NMS.py runs, a distinct terminal window opens
where some information are logged. All output is prefixed with `>> Pi` or indented
below it.

As soon as the menu appears in the game, you can start generating via the GUI window
that opens short after the terminal. Both, technology and products, are enabled
by default but and can be toggled separately. The generation will run a couple of
minutes (depending on your machine) in the background with some progress logging.
It is also possible to set custom values for each category to only generate those
specific items (comma separated).

You can also extend the records with the generated names for multiple languages
by running it multiple times with different language settings. After a generation
is done, you can change the in-game language and immediately start it again without
restarting. This will not overwrite existing names of other languages. The
selected/new language will be shown in the log mentioned above.

## Authors

* **Christian Engelhardt** (zencq) - [GitHub](https://github.com/cengelha)

## Credits

* **monkeyman192** - Biggest thanks goes to him for creating NMS.py and the continuous support
* **DHarhan** - Giving feedback about the desirability of certain stats and combinations
* **ICE** and **DarkWalker** - Previously used scripts based on those shared by
  them in the [Creative & Sharing Hub](https://discord.gg/RSGQFQv2pP)
>>>>>>> remotes/upstream/HEAD
