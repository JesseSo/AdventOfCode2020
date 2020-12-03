package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	move(1, 1)
	move(3, 1)
	move(5, 1)
	move(7, 1)
	move(1, 2)
}

func move(x int, y int) {
	file, err := os.Open("map.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var pos = 0
	var count = 0
	var scanRow = 0
	const tree = "#"

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		var ch = string(scanner.Text()[pos])
		if scanRow%y == 0 {
			pos = pos + x
			if strings.EqualFold(ch, tree) {
				count++
			}
			if pos >= 31 {
				pos = pos - 31
			}
		}
		scanRow++
	}

	fmt.Println(count)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
