# [Part Pit](https://github.com/swedishhat/part-pit)
A git-friendly electronics library manager

## Introduction
Creating electronics components is a huge, annoying time-suck. What's worse is that someone, somewhere has probably created the part already. It's also a ripe problem space to innovate on and several people and companies have attempted solving this already.

Don't get me wrong... it's not like there aren't ways to find the parts you need already made. Many ECAD tools have their own standard libraries ([KiCad](https://kicad.github.io/) | [Altium](https://designcontent.live.altium.com/) | [Eagle](http://eagle.autodesk.com/eagle/libraries)) and there there are useful services like [EE Concierge](https://eeconcierge.com/), [SnapEDA](https://www.snapeda.com), [PCB Libraries](https://www.pcblibraries.com/) and others that have huge proprietary libraries that can export to a bunch of different ECAD tools. The services will even make parts for you, for some kind of fee if it's not in their library already. 

However, these services have their own styles and standards that may be inconsistent with your system. For example, do parts exported from SnapEDA conform to the [KiCad KLC](http://kicad-pcb.org/libraries/klc/)? Do Altium's unified parts (also EE Concierge because Altium bought them) match your company's own internal library styles and conventions? How are errors reported and corrected if it turns out these third parties borked up? How much manual intervention do you really want to have in pouring over and tweaking the individual library parts?

## What does it do?
The purpose of this project is eventually to create a totally text-based component library system that can import from and export to any arbitrary CAD tool format, but there are some external forces that are guiding the devleopment priorities. This is meant to serve first as an alternative to Altium's Vault system using existing binary library files. Components will be defined using TOML, and the tool will use this to link together the specified symbol / footprint / PDF / parameters and produce an Altium DbLib file that links to a locally hosted SQLite3 database. This allows the library to function without internet access, and all changes to the library can be resolved using a git workflow.

* Components are currently defined with TOML but eventually I'd like to support JSON, YAML, & maybe XML. The input format doesn't really matter, but it should be something that is easy to read, understand, and modify with a text editor
* Components all stored in a git repository so you can do diffing & merge resolution using those tools, rather than the ECAD's interface. 
* Written in Go
  * Reads component file
  * Validates correctness of the component file against a schema
  * Generates a sqlite database with the component info
  * Generates an Altium DbLib file formatted with sqlite table info
  * Has ability to pull updates from the git server
  * Digikey parametric search is something I want to add later

## Schematic Symbols
Schematic symbols are graphical representations of electrical components that first and foremost need to communicate to _humans_ the function of a circuit (as opposed to the physical arrangement). That means that a schematic not only needs to be correctly connected together for the sake of the EDA tool, it also needs to be legible and easy to understand for the sake of the designer. "Legible" and "easy to understand" open up a can of worms since style, convention, and aesthetics are subjective and differ between organizations, tools, and individuals. 

As nice as it would be to define rigid rules that allow symbols to be defined programmatically (e.g. "all input pins go on the left side"), there are a too many "gotchas" and edge cases that provide exceptions to the rule in order to make the schematic capture cleaner (e.g. on switching power supply ICs, the feedback pin is an input, but almost always looks better to place it close to the output inductor on the right side).

So, in Part Pit, schematic symbols are separated conceptually between the following 
* Electrical model (pin names, pin designators, ERC rule classes)
* Graphical model (pin decorators for clocks, active-low signals, etc; physical placement of pins)
* Fuzzy Rules / "Suggestions" (e.g. "VCC pins normally go near the top", "inputs normally go on the left", etc.) that provide sane defaults for positioning pins on new symbols, but allows the designer to move things around 
