package main

import (
	"log"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Name  string
	Email string `gorm:"unique"`
}

func main() {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		log.Fatal("failed to connect database")
	}
	
	db.AutoMigrate(&User{})
	
	user := User{Name: "John", Email: "john@example.com"}
	db.Create(&user)
	
	var users []User
	db.Find(&users)
	
	log.Printf("Found %d users\n", len(users))
}
