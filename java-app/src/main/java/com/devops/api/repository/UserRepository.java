package com.devops.api.repository;

import com.devops.api.model.User;
import org.springframework.stereotype.Repository;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

@Repository
public class UserRepository {
    private final Map<Long, User> users = new ConcurrentHashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public UserRepository() {
        // Seed initial data
        save(new User(null, "John Doe", "john@example.com", 30));
        save(new User(null, "Jane Smith", "jane@example.com", 25));
        save(new User(null, "Bob Johnson", "bob@example.com", 35));
    }

    public User save(User user) {
        if (user.getId() == null) {
            user.setId(idGenerator.getAndIncrement());
            user.setCreatedAt(java.time.LocalDateTime.now());
        }
        user.setUpdatedAt(java.time.LocalDateTime.now());
        users.put(user.getId(), user);
        return user;
    }

    public Optional<User> findById(Long id) {
        return Optional.ofNullable(users.get(id));
    }

    public List<User> findAll() {
        return new ArrayList<>(users.values());
    }

    public void deleteById(Long id) {
        users.remove(id);
    }

    public boolean existsById(Long id) {
        return users.containsKey(id);
    }
}
