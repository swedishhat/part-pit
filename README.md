# [part-pit](https://github.com/swedishhat/part-pit)
A git-friendly library manager for Altium

## Why?
You know what sucks? Trying to make a PCB and not having the part you want in your library. You know what also sucks? The fact that someone already probably made that part, but it's siloed away in some inaccessible company database, behind  some paywall, or in a different file format. 

EE Concierge
SnapEDA
Kicad Standard Libraries
Altium Standard Libraries
https://www.pcblibraries.com

## What does it do?
The purpose of this project is to create a component library system for Altium that allows schematic symbols and PCB footprints to be linked together using a text-based component definition, and then produce a DbLib file that can be consumed by Altium. The git repository containing the models and component definitions is the global source of truth, not the DbLib. This means that all modifications, additions, deletions, and issue resolutions occur using a standard git workflow in the tool of your choice. The DbLib is destroyed and recreated each time the git repository is updated.

The database that links to the DbLib is designed to be self-hosted on each developer's machine so that the library remains fully decentralized. 

* Components are currently defined with TOML but eventually I'd like to support JSON, YAML, & maybe XML
* Components all stored in a git repository so you can do diffing & merge resolution using those tools
* Written in Python
  * Reads component file
  * Validates correctness of the component file against a schema
  * Generates a sqlite database with the component info
  * Generates an Altium DbLib file formatted with sqlite table info
  * Has ability to pull updates from the git server
  * Digikey parametric search is something I want to add later
