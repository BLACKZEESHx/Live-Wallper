import cv2

def save_first_frame(video_path, output_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the first frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        return

    # Save the first frame as an image
    cv2.imwrite(output_path, frame)
    print("First frame saved as", output_path)

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    video_path = input("Enter the path to the video file: ")
    output_path = input("Enter the path to save the first frame (include file extension): ")
    save_first_frame(video_path, output_path)
