package main

import "fmt"

func main() {
	conferenceName :="Go conference"
	const conferenceTickets=50
	var remainingTickets uint=50
	bookings :=[]string{}
	// var bookings []string
	fmt.Printf("hello welcome to %v booking application",conferenceName)
	fmt.Println()
	fmt.Println("we have total of",conferenceTickets,"tickets and",remainingTickets,"remaining tickets")
	fmt.Println("you can book your ticket here")
	for{
	var firstName string
	var lastName string
	var userTicket uint

	fmt.Println("enter your first name: ")
	fmt.Scan(&firstName)
	fmt.Println("enter your last name")
	fmt.Scan(&lastName)
	fmt.Println("How many tickets do you want?")
	fmt.Scan(&userTicket)

	remainingTickets=remainingTickets-userTicket
	bookings=append(bookings,firstName+" "+lastName)

	fmt.Printf("hello, thank You %v %v for booking %v tickets",firstName,lastName,userTicket)
	fmt.Println()
	fmt.Printf("remaining tickets are %v",remainingTickets)
	fmt.Println()
	}


}