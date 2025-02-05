import cv2

# 1. Load the pre-trained Haar Cascade classifier for face detection.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Load an image where you want to detect faces.
#    Make sure the image file (e.g., 'image.jpg') is in your project directory or provide the full path.
image_path = r'C:\Users\Draconian\Desktop\Detect.png'
img = cv2.imread(image_path)

# Check if the image was loaded successfully.
if img is None:
    print("Error: Unable to load image!")
    exit()

# 3. Convert the image to grayscale (Haar Cascades work on grayscale images).
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Perform the face detection.
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,   # Adjusts how much the image size is reduced at each scale.
    minNeighbors=5,    # How many neighbors each candidate rectangle should have.
    minSize=(30, 30)   # Minimum size for detected objects.
)

print(f"Found {len(faces)} face(s)")

# 5. Draw rectangles around the detected faces.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 6. Display the output image with detections.
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)  # Wait for a key press to close the window.
cv2.destroyAllWindows()
