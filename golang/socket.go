package main

import (
	"math"
)

var privateAlice float64
var privatebBob float64
var publicG float64
var publicP float64

func BobInter1(publicG, publicP float64) float64 {
	privatebBob = 3
	bobInter := math.Mod(math.Pow(publicG, privatebBob), publicP)
	return bobInter
}

func AliceInter1(publicG, publicP float64) float64 {
	privateAlice = 4
	aliceInter := math.Mod(math.Pow(publicG, privateAlice), publicP)
	return aliceInter
}

func BobInter2(aliceInter, publicP float64) float64 {
	privatebBob = 3
	final := math.Mod(math.Pow(aliceInter, privatebBob), publicP)
	return final
}

func AliceInter2(bobInter, publicP float64) float64 {
	privateAlice = 4
	final := math.Mod(math.Pow(bobInter, privateAlice), publicP)
	return final
}

func main() {
	// Alice
	publicG = 5
	publicP = 23
	aliceInter := AliceInter1(publicG, publicP)
	// Bob
	bobInter := BobInter1(publicG, publicP)
	key1 := BobInter2(aliceInter, publicP)
	// Alice
	key2 := AliceInter2(bobInter, publicP)
}
