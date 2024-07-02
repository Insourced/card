package main

import (
	"card/pkg/query"
	"os"
)

func main() {
	var arg0 string
	if len(os.Args) > 1 {
		arg0 = os.Args[1]
	}
	query.Parse(arg0)
	return
}
