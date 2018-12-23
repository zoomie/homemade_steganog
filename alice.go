package main

import (
	"fmt"
	"io/ioutil"
	"log"
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
	// aliceInter := math.Mod(math.Pow(publicG, privateAlice), publicP)
	// Send info over to bob
	resp, err := http.Get("http://localhost:8001/gen")
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	temp := reflect.TypeOf(body).Kind()
	fmt.Println(temp)
	x := string(body[:])
	fmt.Println(x)
	num, _ := strconv.ParseInt(x, 10, 64)
	fmt.Println("ment to be int", num)
	fmt.Println(reflect.TypeOf(x))
	log.Println(string(body))
	// bobIntermediateKey := request.get("url_to_bob", aliceInter)
	// key := math.Mod(math.Pow(bobIntermediateKey, privateAlice), publicP)
	// http.HandleFunc("/", setup_conn)
	// http.ListenAndServe(":8000", nil)
}

// func setup_conn(w http.ResponseWriter, r *http.Request) {
// 	r.ParseForm()
// 	num := r.FormValue("num")
// 	fmt.Println(num)
// }
