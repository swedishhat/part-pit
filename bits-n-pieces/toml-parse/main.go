package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os"
)

func main() {
    content, err := ioutil.ReadFile(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("File contents: %s", content)

}