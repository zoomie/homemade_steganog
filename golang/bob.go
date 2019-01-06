package main

import (
	"fmt"
	"math"
	"net/http"
	"strconv"
)

var publicG float64
var publicP float64
var privatebBob float64

func KeyGen(w http.ResponseWriter, r *http.Request) {
	privatebBob = 3
	publicG = 5
	publicP = 23
	r.ParseForm()
	input := r.FormValue("aliceInter")
	aliceInter, _ := strconv.ParseFloat(input, 64)

	// fmt.Println(reflect.TypeOf(aliceInter))

	key := math.Mod(math.Pow(aliceInter, privatebBob), publicP)
	bobInter := math.Mod(math.Pow(publicG, privatebBob), publicP)
	fmt.Println("Bobs private key is: ", key)
	fmt.Fprint(w, bobInter)
}

func main() {
	http.HandleFunc("/gen", KeyGen)
	http.ListenAndServe(":8001", nil)
}
