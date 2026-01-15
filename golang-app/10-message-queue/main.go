package main

import (
	"log"
	"time"
)

type Message struct {
	ID      string
	Payload string
}

type Consumer struct {
	queue chan Message
}

func NewConsumer() *Consumer {
	return &Consumer{
		queue: make(chan Message, 100),
	}
}

func (c *Consumer) Start() {
	go func() {
		for msg := range c.queue {
			log.Printf("Processing message: %s - %s\n", msg.ID, msg.Payload)
			time.Sleep(time.Millisecond * 100)
		}
	}()
}

func (c *Consumer) AddMessage(msg Message) {
	c.queue <- msg
}

func main() {
	consumer := NewConsumer()
	consumer.Start()
	
	// Simulate messages
	for i := 1; i <= 10; i++ {
		consumer.AddMessage(Message{
			ID:      string(rune(i)),
			Payload: "Message content",
		})
	}
	
	time.Sleep(time.Second * 2)
	log.Println("Consumer finished")
}
