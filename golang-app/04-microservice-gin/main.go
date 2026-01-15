package main

import (
	"github.com/gin-gonic/gin"
	"github.com/gin-contrib/cors"
)

func main() {
	r := gin.Default()
	
	r.Use(cors.Default())
	
	api := r.Group("/api")
	{
		api.GET("/users", getUsers)
		api.GET("/users/:id", getUser)
		api.POST("/users", createUser)
	}
	
	r.GET("/health", func(c *gin.Context) {
		c.JSON(200, gin.H{"status": "healthy"})
	})
	
	r.Run(":8080")
}

func getUsers(c *gin.Context) {
	c.JSON(200, gin.H{"users": []string{}})
}

func getUser(c *gin.Context) {
	id := c.Param("id")
	c.JSON(200, gin.H{"id": id})
}

func createUser(c *gin.Context) {
	c.JSON(201, gin.H{"status": "created"})
}
