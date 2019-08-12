package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

type componentConfig struct {
	name          string
	description   string
	category      string
	lifecycle     string
	externals     []external
	stringParams  []stringParam
	numericParams []numericParam
}

type external struct {
	name     string
	category string
	uri      string
}

type stringParam struct {
	name    string
	value   string
	visible bool
}

type numericParam struct {
	name    string
	value   float32
	unit    string
	visible bool
}

func main() {
	// look at the

	content, err := ioutil.ReadFile(os.Args[1])

	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("File contents: %s", content)

}
