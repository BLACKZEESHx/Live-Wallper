package main

import (
	"fmt"

	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/media"
)

func main() {
	a := app.New()
	w := a.NewWindow("Video Player")

	// Create a media player widget
	player := media.NewPlayer()

	// Load the video file
	err := player.Load("path/to/video.mp4")
	if err != nil {
		fmt.Println("Error loading video:", err)
		return
	}

	// Add the media player to the window
	w.SetContent(player)

	// Show the window
	w.ShowAndRun()
}
