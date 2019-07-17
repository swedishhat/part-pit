# [Part Pit](https://github.com/swedishhat/part-pit)
A git-friendly library manager for Altium

## The Least Fun Part of Electronics Design
Creating electronics components is a huge, annoying time-suck. What's worse is that someone, somewhere has probably created the part already. 

Don't get me wrong... it's not like there aren't ways to find the parts you need already made. Many ECAD tools have their own standard libraries ([KiCad](https://kicad.github.io/) | [Altium](https://designcontent.live.altium.com/) | [Eagle](http://eagle.autodesk.com/eagle/libraries)) and there there are useful services like [EE Concierge](https://eeconcierge.com/), [SnapEDA](https://www.snapeda.com), [PCB Libraries](https://www.pcblibraries.com/) and others that have huge proprietary libraries that can export to a bunch of different ECAD tools. The services will even make parts for you, for some kind of fee if it's not in their library already. 

However, these services have their own styles and standards that may be inconsistent with your system. For example, do parts exported from SnapEDA conform to the [KiCad KLC](http://kicad-pcb.org/libraries/klc/)? Do Altium's unified parts (also EE Concierge because Altium bought them) match your company's own internal library styles and conventions? How are errors reported and corrected if it turns out these third parties borked up? How much manual intervention do you really want to have in pouring over and tweaking the individual library parts?

## What does it do?
The purpose of this project is eventually to create a totally text-based component library system that can import from and export to any arbitrary CAD tool format, but there are some external forces that are guiding the devleopment priorities. This is meant to serve first as an alternative to Altium's Vault system using existing binary library files. Components will be defined using TOML, and the tool will use this to link together the specified symbol / footprint / PDF / parameters and produce an Altium DbLib file that links to a locally hosted SQLite3 database. This allows the library to function without internet access, and all changes to the library can be resolved using a git workflow.

* Components are currently defined with TOML but eventually I'd like to support JSON, YAML, & maybe XML
* Components all stored in a git repository so you can do diffing & merge resolution using those tools
* Written in Python
  * Reads component file
  * Validates correctness of the component file against a schema
  * Generates a sqlite database with the component info
  * Generates an Altium DbLib file formatted with sqlite table info
  * Has ability to pull updates from the git server
  * Digikey parametric search is something I want to add later
