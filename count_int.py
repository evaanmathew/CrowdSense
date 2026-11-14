from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("my_model.pt")

# Run inference on webcam (stream=True so we can process frame-by-frame)
results = model.predict(source=0, show=False, stream=True, verbose=False)

# Optional: track previous counts to avoid repeating same output
prev_head, prev_body = -1, -1

for result in results:
    # Extract bounding boxes and class IDs
    boxes = result.boxes
    class_ids = boxes.cls.cpu().numpy() if boxes is not None else []

    # Count heads and bodies (assuming class 0 = head, class 1 = body)
    head_count = int((class_ids == 0).sum())
    body_count = int((class_ids == 1).sum())

    # Print only if count changes
    if head_count != prev_head or body_count != prev_body:
        print(head_count, body_count)
        prev_head, prev_body = head_count, body_count

    # Press 'q' to exit cleanly
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
