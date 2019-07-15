# library-build
A library manager for Altium at the moment that eventually can make BoMs

## Why?
You know what sucks? Trying to make a PCB and not having the part you want in your library. You know what also sucks? The fact that someone already probably made that part, but it's siloed away in some inaccessible company database, behind  some paywall, or in a different file format. 

EE Concierge
SnapEDA
Kicad Standard Libraries
Altium Standard Libraries
https://www.pcblibraries.com

## What does it do?

* Components defined with TOML
  * Should eventually support JSON, YAML, & maybe XML
* Components all stored in a git repository so you can do diffing & merge resolution using those tools (not this one)
* Python app that 
  * Reads component file
  * Validates correctness of the component file against a schema
  * Generates a sqlite database with the component info
  * Generates an Altium DbLib file formatted with sqlite table info
  * Has ability to pull updates from the git server
  * Digikey parametric search
