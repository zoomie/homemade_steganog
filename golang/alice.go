package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"net/http"
	"reflect"
	"strconv"
)

var publicG float64
var publicP float64
var privateAlice float64

func main() {
	publicG = 5
	publicP = 23
	privateAlice = 4
	aliceInter := int(math.Mod(math.Pow(publicG, privateAlice), publicP))
	url := fmt.Sprintf("%s%d", "http://localhost:8001/gen?aliceInter=", aliceInter)
	resp, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	bobInter, _ := strconv.ParseFloat(string(body), 64)
	fmt.Println("ment to be int", bobInter)
	fmt.Println(reflect.TypeOf(bobInter))

	key := math.Mod(math.Pow(bobInter, privateAlice), publicP)
	fmt.Println("Alices private key is:", key)
	// http.HandleFunc("/", setup_conn)
	// http.ListenAndServe(":8000", nil)
}

// func setup_conn(w http.ResponseWriter, r *http.Request) {
// 	r.ParseForm()
// 	num := r.FormValue("num")
// 	fmt.Println(num)
// }
