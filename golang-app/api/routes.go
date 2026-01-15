package api

import (
	"encoding/json"
	"net/http"

	"github.com/devops-repo/golang-app/internal/database"
	"github.com/devops-repo/golang-app/pkg/handlers"
	"github.com/devops-repo/golang-app/pkg/middleware"
	"github.com/gorilla/mux"
)

// SetupRoutes configures all application routes
func SetupRoutes(db *database.Database) *mux.Router {
	router := mux.NewRouter()
	
	// Apply global middleware
	router.Use(middleware.Recovery)
	
	// Health check endpoint
	router.HandleFunc("/health", healthCheckHandler).Methods("GET")
	
	// User handler
	userHandler := handlers.NewUserHandler(db)
	
	// API routes
	api := router.PathPrefix("/api").Subrouter()
	
	// User routes
	api.HandleFunc("/users", userHandler.GetAllUsers).Methods("GET")
	api.HandleFunc("/users/{id}", userHandler.GetUser).Methods("GET")
	api.HandleFunc("/users", userHandler.CreateUser).Methods("POST")
	api.HandleFunc("/users/{id}", userHandler.UpdateUser).Methods("PUT")
	api.HandleFunc("/users/{id}", userHandler.DeleteUser).Methods("DELETE")
	
	return router
}

// healthCheckHandler handles health check requests
func healthCheckHandler(w http.ResponseWriter, r *http.Request) {
	response := map[string]interface{}{
		"status":  "healthy",
		"message": "Go web server is running",
	}
	
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}
