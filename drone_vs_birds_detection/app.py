import os
from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image, ImageDraw

app = Flask(__name__)

output_dir = "static"
os.makedirs(output_dir, exist_ok=True)

# Load YOLOv8 model
model = YOLO("best (3).pt")

@app.route("/", methods=['POST', 'GET'])
def get_image():
    if request.method == 'POST':
        image_file = request.files['image']

        if image_file.filename == "":
            return "Error: No image uploaded."

        # Save input image
        input_path = os.path.join(output_dir, "input.png")
        image_file.save(input_path)

        # Run YOLO model
        results = model(input_path)

        detected_objects = results[0].names  # Map from class ID to name
        original_image = Image.open(input_path)
        draw = ImageDraw.Draw(original_image)

        detected_labels = set()  # To store detected object names

        # Loop over detections
        for box in results[0].boxes:
            class_id = int(box.cls)
            class_name = detected_objects[class_id]
            detected_labels.add(class_name)  # Store detected object names

            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
            draw.rectangle([x1, y1, x2, y2], outline="blue", width=3)
            draw.text((x1, y1 - 10), class_name, fill="blue")

        # Save annotated image
        output_path = os.path.join(output_dir, "output.png")
        original_image.save(output_path)

        # Convert set to a list and display detected objects
        detected_labels_list = list(detected_labels)

        return render_template("result.html", image_url="static/output.png", detected_objects=detected_labels_list)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)

