Icewind Dale: King of the Wolves
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
============
The adventure will take place around Good Mead - a small town in Icewind Dale which produces mead from honey.

It'll be a pretty short adventure so not much opportunity for personalised hooks, so create a level 5 character that has a reason to be in Good Mead and is motivated to help the people there.

Character Creation
==================

Golden Rules
------------
1. Create a character that wants to be an adventurer.
2. Create a character that will be fun for the rest of the party to adventure with.
3. Pitch your character idea(s) to me early.

Ability Scores
--------------
I'd like to try a way of rolling for stats that will hopefully open up some more interesting character choices. When people choose where their stats go, most people place them optimally, which leads to all classes being pretty same-y.

I like rolling for stats because it frees people from this optimiser's dilemma. To avoid disparate outcomes, so we're going to have everyone use different permutations of the same randomly generated array - with the opportunity to swap the position of any two stats.

For example, we might generate the array ``6, 7, 13, 13, 14, 16``, and then random permutations of it:

+--------+-----+-----+-----+-----+-----+-----+
| Player | STR | DEX | CON | INT | WIS | CHA |
+========+=====+=====+=====+=====+=====+=====+
|   A    | 13  | 16  |  7  | 13  |  6  |  14 |
+--------+-----+-----+-----+-----+-----+-----+
|   B    | 13  | 6   |  16 | 7   |  14 |  13 |
+--------+-----+-----+-----+-----+-----+-----+
|   C    | 13  | 14  |  13 | 16  |  6  |  7  |
+--------+-----+-----+-----+-----+-----+-----+
|   D    | 6   | 13  |  7  | 13  |  14 |  16 |
+--------+-----+-----+-----+-----+-----+-----+

Player A decides that with decent DEX and CHA, he's going to play a swashbuckler rogue. He swaps his INT score with CON to end up with ``13, 16, 13, 7, 6, 14``, and then adds his racial bonuses.


.. code-block:: python
    :caption: Algorithm to roll for stats

    def d6():
        return random.randint(1, 6)


    def roll():
        """Roll 4d6kh3"""
        return sum(sorted((d6() for _ in range(4)))[1:])


    def main():
        array = sorted((roll() for _ in range(6)))
        total = sum(array)
        lower, upper = 62, 82
        while not (lower < total < upper):
            print(f"Generated: {array}, total: {total}")
            if lower >= total:
                print(f"Too low, replacing lowest: {array[0]}")
                array[0] = roll()
            else:
                print(f"Too high, replacing second highest: {array[-2]}")
                array[-2] = roll()

            array = sorted(array)
            total = sum(array)

        print(f"Final array: {array}, total: {total}")

Playable Races
--------------
- Aasimar
- Custom Lineage
- Dragonborn
- Dwarf
- Elf
- Firbolg
- Gnome
- Goblin
- Goliath
- Gothic Lineage (Dhampir, Hexblood, Reborn)
- Half-elf
- Half-orc
- Halfling
- Hobgoblin
- Human
- Kobold
- Tiefling
- Triton

Let me know if there's something else you really want to play.

Multiclassing
-------------
Sure, but note it's probably a bad idea at level 5.

Backgrounds
-----------
Custom backgrounds are fine.

Innate Spellcasting
-------------------
Pre-TcoE if a racial ability or feat let you cast a spell once per long rest, RAW you don't count as knowing that spell and you cannot cast it with any spell slots you may have. Eg. Tiefling Infernal Legacy.

Post-TcoE this changed, allowing you to also cast the spell using any spell slots you may have. Eg. Fey Touched feat.

I would like to interpret all of these abilities in the post-TcoE way, so if you play a Tiefling you may also cast hellish rebuke using any spell slots you have.

Backstory
---------
Here are some useful resources:

- `Heroic Chronicle: Sword Coast and the North <https://www.dndbeyond.com/posts/783-heroic-chronicle-sword-coast-and-the-north>`_
- `Heroic Chronicle: Wildemount <http://dnd5e.wikidot.com/background:wildemount-heroic-chronicle>`_

Alignment
---------
I don't *really* care about alignment as long as it doesn't conflict with the golden rules.

Bonus points if you read this `hyper nerdy article <https://humanparts.medium.com/the-mtg-color-wheel-c9700a7cf36d>`_ and tell me which colors represent your character's personality.

Miscellaneous
-------------
- I'm generally happy to reskin things, eg. use half-orc mechanics to play a human barbarian.
- All the optional stuff from TcoE is fine.
- Content from Eberron and Critical Role is in general not allowed, let me know if there's something you really want.
- Don't play something that will slow combat down, eg. micromanaging multiple units like summons.
- Don't play something that has lots of crazy random effects like rolling on d100 tables, eg. wild magic sorcerer.

Gameplay
========

Concentration
-------------
It's really hard for me to keep track of everyone's concentration, so I'd like there to be some penalty for players forgetting to keep track over their own. I'll remind you if I remember, but if we both forget and I remember later I'll have you roll at disadvantage.

Spell Components
----------------
You can use a focus instead of any material components that don't have cost requirements.

If you plan on having equipment in each hand (eg. shield + weapon, dual wield), I would recommend you take the Warcaster feat so we don't have to track whether you have a free hand for somatic components.

Disarming
---------
Not allowed because whatever you can do to enemies, they can do to you. It will be sad when goblins throw your magic sword in the lake.

Passive Ability Scores
----------------------
The DC to hide/stealth is the opponent's passive perception.

If your passive score meets the DC for a check you might automatically succeed after some period of time (depending on the task). Eg. if you spend 10 minutes trying to lift something heavy.

Falling Damage
--------------
Falling damage will be increased to 1d8 per 10ft, up to a maximum of 50d8 at 500ft.

You can make a Dexterity (Acrobatics) check to take half damage if you fall voluntarily.

Rolling Dice
============

Invalid Rolls
-------------
Rolls don't count if:

- you weren't asked to roll
- they fall off the table

Percentile Dice (d100)
----------------------
PHB p6: "You generate a number between 1 and 100 by rolling two different ten-sided dice numbered from 0 to 9. One die (designated before you roll) gives the tens digit, and the other gives the ones digit. If you roll a 7 and a 1, for example, the number rolled is 71. **Two Os represent 100.**"



