import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# -----------------------------
# Load Pose Model
# -----------------------------
base_options = python.BaseOptions(
    model_asset_path="pose_landmarker_full.task"
)

options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    num_poses=1
)

detector = vision.PoseLandmarker.create_from_options(
    options
)

# -----------------------------
# Landmark Names
# -----------------------------
LANDMARKS = {
    0: "Nose",
    2: "L Eye",
    5: "R Eye",
    7: "L Ear",
    8: "R Ear",
    11: "L Shoulder",
    12: "R Shoulder",
    13: "L Elbow",
    14: "R Elbow",
    15: "L Wrist",
    16: "R Wrist",
    23: "L Hip",
    24: "R Hip",
    25: "L Knee",
    26: "R Knee",
    27: "L Ankle",
    28: "R Ankle"
}

# -----------------------------
# Skeleton Connections
# -----------------------------
POSE_CONNECTIONS = [
    (11, 13), (13, 15),
    (12, 14), (14, 16),
    (11, 12),
    (11, 23), (12, 24),
    (23, 24),
    (23, 25), (25, 27),
    (24, 26), (26, 28)
]

# -----------------------------
# Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    if result.pose_landmarks:

        pose = result.pose_landmarks[0]

        # Draw skeleton
        for start, end in POSE_CONNECTIONS:

            p1 = pose[start]
            p2 = pose[end]

            x1 = int(p1.x * w)
            y1 = int(p1.y * h)

            x2 = int(p2.x * w)
            y2 = int(p2.y * h)

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 0, 0),
                2
            )

        # Draw body parts
        for idx, landmark in enumerate(pose):

            if idx in LANDMARKS:

                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.circle(
                    frame,
                    (x, y),
                    6,
                    (0, 255, 0),
                    -1
                )

                cv2.putText(
                    frame,
                    LANDMARKS[idx],
                    (x + 10, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 255),
                    1
                )

        # Show Nose Coordinates
        nose = pose[0]

        nose_x = int(nose.x * w)
        nose_y = int(nose.y * h)

        cv2.putText(
            frame,
            f"Nose: ({nose_x}, {nose_y})",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "MediaPipe Pose Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()