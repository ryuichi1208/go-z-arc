package main

import (
	"fmt"
	"os"
	"testing"
)

func TestMain(m *testing.M) {
	fmt.Println("before test")
	code := m.Run()
	fmt.Println("after test")
	os.Exit(code)
}
