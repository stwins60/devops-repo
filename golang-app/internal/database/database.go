package database

import (
	"errors"
	"sync"
	"time"

	"github.com/devops-repo/golang-app/pkg/models"
)

// Database represents an in-memory database
type Database struct {
	users  map[int]*models.User
	nextID int
	mu     sync.RWMutex
}

// NewDatabase creates a new database instance with seed data
func NewDatabase() *Database {
	db := &Database{
		users:  make(map[int]*models.User),
		nextID: 1,
	}
	
	// Seed initial data
	db.CreateUser("John Doe", "john@example.com", 30)
	db.CreateUser("Jane Smith", "jane@example.com", 25)
	db.CreateUser("Bob Johnson", "bob@example.com", 35)
	
	return db
}

// CreateUser creates a new user
func (db *Database) CreateUser(name, email string, age int) *models.User {
	db.mu.Lock()
	defer db.mu.Unlock()
	
	user := &models.User{
		ID:        db.nextID,
		Name:      name,
		Email:     email,
		Age:       age,
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
	}
	
	db.users[db.nextID] = user
	db.nextID++
	
	return user
}

// GetUser retrieves a user by ID
func (db *Database) GetUser(id int) (*models.User, error) {
	db.mu.RLock()
	defer db.mu.RUnlock()
	
	user, exists := db.users[id]
	if !exists {
		return nil, errors.New("user not found")
	}
	
	return user, nil
}

// GetAllUsers retrieves all users
func (db *Database) GetAllUsers() []*models.User {
	db.mu.RLock()
	defer db.mu.RUnlock()
	
	users := make([]*models.User, 0, len(db.users))
	for _, user := range db.users {
		users = append(users, user)
	}
	
	return users
}

// UpdateUser updates an existing user
func (db *Database) UpdateUser(id int, name, email string, age int) (*models.User, error) {
	db.mu.Lock()
	defer db.mu.Unlock()
	
	user, exists := db.users[id]
	if !exists {
		return nil, errors.New("user not found")
	}
	
	if name != "" {
		user.Name = name
	}
	if email != "" {
		user.Email = email
	}
	if age > 0 {
		user.Age = age
	}
	user.UpdatedAt = time.Now()
	
	return user, nil
}

// DeleteUser deletes a user by ID
func (db *Database) DeleteUser(id int) error {
	db.mu.Lock()
	defer db.mu.Unlock()
	
	if _, exists := db.users[id]; !exists {
		return errors.New("user not found")
	}
	
	delete(db.users, id)
	return nil
}

// UserExists checks if a user exists
func (db *Database) UserExists(id int) bool {
	db.mu.RLock()
	defer db.mu.RUnlock()
	
	_, exists := db.users[id]
	return exists
}
