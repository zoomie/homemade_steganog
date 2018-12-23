package main

import (
	"fmt"
	"net/http"
)

// var publicG float64
// var publicP float64

func KeyGen(w http.ResponseWriter, r *http.Request) {
	// privatebBob = 3
	// r.ParseForm()
	// publicG := r.FormValue("publicG")
	// publicP := r.FormValue("publicP")
	// aliceInter := r.FormValue("aliceInter")
	// key := math.Mod(math.Pow(aliceInter, privatebBob), publicP)
	// fmt.Println(key)
	// bobInter := math.Mod(math.Pow(publicG, privatebBob), publicP)
	fmt.Fprint(w, 10)
}

func main() {
	http.HandleFunc("/gen", KeyGen)
	http.ListenAndServe(":8001", nil)
}
