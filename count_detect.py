from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("my_model.pt")

# Run inference on webcam (stream=True so we can loop frame by frame)
results = model.predict(source=0, show=True, stream=True)

for result in results:
    # Extract bounding boxes and class IDs
    boxes = result.boxes
    class_ids = boxes.cls.cpu().numpy()

    # Count heads and bodies (assuming class 0 = head, class 1 = body)
    head_count = (class_ids == 0).sum()
    body_count = (class_ids == 1).sum()

    # Print in terminal
    print(f"Heads: {head_count}, Bodies: {body_count}")

    # Overlay count on video frame
    frame = result.orig_img
    cv2.putText(frame, f"Heads: {head_count}  Bodies: {body_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Head/Body Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
