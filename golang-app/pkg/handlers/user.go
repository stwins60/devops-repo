package handlers

import (
	"encoding/json"
	"log"
	"net/http"
	"strconv"

	"github.com/devops-repo/golang-app/internal/database"
	"github.com/devops-repo/golang-app/pkg/models"
	"github.com/gorilla/mux"
)

// UserHandler handles user-related HTTP requests
type UserHandler struct {
	db *database.Database
}

// NewUserHandler creates a new UserHandler
func NewUserHandler(db *database.Database) *UserHandler {
	return &UserHandler{db: db}
}

// GetAllUsers handles GET /api/users
func (h *UserHandler) GetAllUsers(w http.ResponseWriter, r *http.Request) {
	users := h.db.GetAllUsers()
	
	response := models.UsersResponse{
		Success: true,
		Count:   len(users),
		Data:    make([]models.User, len(users)),
	}
	
	for i, user := range users {
		response.Data[i] = *user
	}
	
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

// GetUser handles GET /api/users/{id}
func (h *UserHandler) GetUser(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		respondWithError(w, http.StatusBadRequest, "Invalid user ID")
		return
	}
	
	user, err := h.db.GetUser(id)
	if err != nil {
		respondWithError(w, http.StatusNotFound, "User not found")
		return
	}
	
	response := models.Response{
		Success: true,
		Data:    user,
	}
	
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

// CreateUser handles POST /api/users
func (h *UserHandler) CreateUser(w http.ResponseWriter, r *http.Request) {
	var input models.UserInput
	
	if err := json.NewDecoder(r.Body).Decode(&input); err != nil {
		respondWithError(w, http.StatusBadRequest, "Invalid request payload")
		return
	}
	
	// Validate input
	if input.Name == "" {
		respondWithError(w, http.StatusBadRequest, "Name is required")
		return
	}
	if input.Email == "" {
		respondWithError(w, http.StatusBadRequest, "Email is required")
		return
	}
	
	user := h.db.CreateUser(input.Name, input.Email, input.Age)
	
	response := models.Response{
		Success: true,
		Message: "User created successfully",
		Data:    user,
	}
	
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(response)
	
	log.Printf("Created user: %d", user.ID)
}

// UpdateUser handles PUT /api/users/{id}
func (h *UserHandler) UpdateUser(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		respondWithError(w, http.StatusBadRequest, "Invalid user ID")
		return
	}
	
	if !h.db.UserExists(id) {
		respondWithError(w, http.StatusNotFound, "User not found")
		return
	}
	
	var input models.UserInput
	if err := json.NewDecoder(r.Body).Decode(&input); err != nil {
		respondWithError(w, http.StatusBadRequest, "Invalid request payload")
		return
	}
	
	user, err := h.db.UpdateUser(id, input.Name, input.Email, input.Age)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, err.Error())
		return
	}
	
	response := models.Response{
		Success: true,
		Message: "User updated successfully",
		Data:    user,
	}
	
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
	
	log.Printf("Updated user: %d", id)
}

// DeleteUser handles DELETE /api/users/{id}
func (h *UserHandler) DeleteUser(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id, err := strconv.Atoi(vars["id"])
	if err != nil {
		respondWithError(w, http.StatusBadRequest, "Invalid user ID")
		return
	}
	
	if err := h.db.DeleteUser(id); err != nil {
		respondWithError(w, http.StatusNotFound, "User not found")
		return
	}
	
	response := models.Response{
		Success: true,
		Message: "User deleted successfully",
	}
	
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
	
	log.Printf("Deleted user: %d", id)
}

// respondWithError sends an error response
func respondWithError(w http.ResponseWriter, code int, message string) {
	response := models.Response{
		Success: false,
		Error:   message,
	}
	
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	json.NewEncoder(w).Encode(response)
}
