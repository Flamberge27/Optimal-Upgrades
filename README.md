# Optimal Upgrades

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

## Credits

* **Christian Engelhardt** (zencq) - [GitHub](https://github.com/cengelha)
* **monkeyman192** - Biggest thanks goes to him for creating NMS.py and the continuous support
* **DHarhan** - Giving feedback about the desirability of certain stats and combinations
* **ICE** and **DarkWalker** - Previously used scripts based on those shared by
  them in the [Creative & Sharing Hub](https://discord.gg/RSGQFQv2pP)
