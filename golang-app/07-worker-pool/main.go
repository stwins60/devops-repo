package main

import (
	"fmt"
	"sync"
	"time"
)

type Job struct {
	ID   int
	Data string
}

type Worker struct {
	ID       int
	JobQueue chan Job
	Quit     chan bool
	wg       *sync.WaitGroup
}

func NewWorker(id int, jobQueue chan Job, wg *sync.WaitGroup) *Worker {
	return &Worker{
		ID:       id,
		JobQueue: jobQueue,
		Quit:     make(chan bool),
		wg:       wg,
	}
}

func (w *Worker) Start() {
	go func() {
		for {
			select {
			case job := <-w.JobQueue:
				fmt.Printf("Worker %d processing job %d\n", w.ID, job.ID)
				time.Sleep(time.Second)
				w.wg.Done()
			case <-w.Quit:
				return
			}
		}
	}()
}

func main() {
	numWorkers := 5
	numJobs := 20
	
	jobQueue := make(chan Job, numJobs)
	var wg sync.WaitGroup
	
	// Start workers
	for i := 1; i <= numWorkers; i++ {
		worker := NewWorker(i, jobQueue, &wg)
		worker.Start()
	}
	
	// Add jobs
	for i := 1; i <= numJobs; i++ {
		wg.Add(1)
		jobQueue <- Job{ID: i, Data: fmt.Sprintf("Job %d", i)}
	}
	
	wg.Wait()
	fmt.Println("All jobs completed")
}
