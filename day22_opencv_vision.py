import cv2


def main():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access the webcam.")
        return

    frame_count = 0
    print("Webcam started. Press 'q' to quit.")

    try:
        while True:
            success, frame = camera.read()

            if not success:
                print("Error: Could not read a video frame.")
                break

            frame_count += 1

            # Process the frame
            height, width = frame.shape[:2]
            cv2.putText(
                frame,
                f"Day 22 | Frame: {frame_count}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Resolution: {width} x {height}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )

            cv2.imshow("Day 22 - Real-Time OpenCV Processing", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()
        print(f"Webcam closed. Frames processed: {frame_count}")


if __name__ == "__main__":
    main()