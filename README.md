# library-build
A library manager for Altium at the moment that eventually can make BoMs

## Why?

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
