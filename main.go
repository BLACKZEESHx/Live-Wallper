package main

import (
	"os"

	"github.com/therecipe/qt/core"
	"github.com/therecipe/qt/multimedia"
	"github.com/therecipe/qt/widgets"
)

func main() {
	// Initialize the application
	app := widgets.NewQApplication(len(os.Args), os.Args)

	// Create the main window
	window := widgets.NewQMainWindow(nil, 0)
	window.SetWindowTitle("Video Player")
	window.SetMinimumSize2(800, 600)

	// Create a video widget
	videoWidget := multimedia.NewQVideoWidget(nil)
	window.SetCentralWidget(videoWidget)

	// Create a media player
	player := multimedia.NewQMediaPlayer(nil, multimedia.QMediaPlayer__VideoSurface)
	player.SetVideoOutput(videoWidget)

	// Load the video file
	fileName := core.NewQFile2("video.mp4")
	fileName.Open(core.QIODevice__ReadOnly)
	if fileName.IsOpen() {
		// mediaContent := multimedia.NewQMediaContent()
		// player.SetMedia(mediaContent)
		player.SetVideoOutput(videoWidget)
		player.Play()
	} else {
		widgets.QMessageBox_Critical(nil, "Error", "Failed to open video file", widgets.QMessageBox__Ok, widgets.QMessageBox__NoButton)
	}

	// Show the main window
	window.Show()

	// Execute the application
	app.Exec()
}
