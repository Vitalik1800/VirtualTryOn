"""
    Project: Virtual Try-On

    Stage: 4
    Substage: 4.1 - Create Face Detector

    Description:
    Face detection module based on MediaPipe Face Mesh.
"""

# ===
# Stage 4.1
# Import libraries
# ===

import mediapipe as mp
import cv2

# ===
# Stage 4.1
# Face Detector
# ===

class FaceDetector:
    """
    MediaPipe Face Mesh detector.
    """

    def __init__(self):

        # ===
        # Stage 4.1
        # Initialize MediaPipe Face Mesh
        # ===

        self.mp_face_mesh = mp.solutions.face_mesh
        
        # ===
        # Stage 4.2
        # Configure Face Mesh
        # ===

        self.configure_face_mesh()

        # ===
        # Stage 4.9
        # Last detection result
        # ===

        self.last_results = None

    # ===
    # Stage 4.11
    # Release resources
    # ===

    def close(self):
        """
        Release Face Mesh resources.
        """

        if hasattr(self, "face_mesh") and self.face_mesh is not None:

            self.face_mesh.close()
            self.face_mesh = None

    # ===
    # Stage 4.2
    # Configure Face Mesh
    # ===

    def configure_face_mesh(self):
        """
        Configure MediaPipe Face Mesh.
        """

        self.face_mesh = self.mp_face_mesh.FaceMesh(

            # Video stream mode

            static_image_mode=False,

            # Maximum number of detected faces

            max_num_faces=1,

            # Enable iris landmarks

            refine_landmarks=True,

            # Detection confidence

            min_detection_confidence=0.5,

            # Tracking confidence

            min_tracking_confidence=0.5
        )

    # ===
    # Stage 4.3
    # Detect face
    # ===

    def detect(self, frame):
        """
        Detect face on the given frame.

        Args:
            frame: OpenCV frame (BGR).

        Returns:
            MediaPipe detection result.
        """

        if frame is None:

            self.last_results = None
            
            return None

        # Convert BGR to RGB

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        rgb_frame.flags.writable = False

        # Detect face

        results = self.face_mesh.process(
            rgb_frame
        )

        rgb_frame.flags.writable = True

        if results.multi_face_landmarks:

            self.last_results = results

        else:

            self.last_results = None

        return self.last_results

    # ===
    # Stage 4.4
    # Get face landmarks
    # ===

    def get_landmarks(self, results):
        """
        Return list of face landmark coordinates.

        Args:
            results: MediaPipe detection result.

        Returns:
            list[(x, y, z)]
        """

        if (
            results is None
            or
            results.multi_face_landmarks is None
        ):
            return []

        face = results.multi_face_landmarks[0]

        landmarks = []

        for landmark in face.landmark:

            landmarks.append(

                (
                    landmark.x,
                    landmark.y,
                    landmark.z
                )
                
            )

        return landmarks

    # ===
    # Stage 4.5
    # Convert landmarks to pixel coordinates
    # ===

    def get_landmark_points(self, results, frame):
        """
        Convert normalized landmarks to pixel coordinates.

        Args:
            results: MediaPipe detection result.
            frame: OpenCV frame.

        Returns:
            list[(x, y)]
        """

        if (
            results is None
            or
            results.multi_face_landmarks is None
            or
            frame is None
        ):
            return []

        height, width = frame.shape[:2]

        face = results.multi_face_landmarks[0]

        points = []

        for landmark in face.landmark:

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

        return points

    # ===
    # Stage 4.6
    # Draw face landmarks
    # ===

    def draw_landmarks(self, frame, results):
        """
        Draw face landmarks as points.

        Args:
            frame: OpenCV frame.
            results: MediaPipe detection results.

        Returns:
            Frame with landmark points.
        """

        if (
            frame is None
            or
            results is None
            or
            results.multi_face_landmarks is None
        ):
            return frame

        height, width = frame.shape[:2]

        for face_landmarks in results.multi_face_landmarks:

            for landmark in face_landmarks.landmark:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    1,
                    (0, 255, 0),
                    -1
                )

        return frame

    # ===
    # Stage 4.7
    # Draw face mesh
    # ===

    def draw_face_mesh(self, frame, results):
        """
        Draw complete Face Mesh.

        Args:
            frame: OpenCV frame.
            results: MediaPipe detection results.

        Returns:
            OpenCV frame.
        """

        if (
            frame is None
            or
            results is None
            or
            results.multi_face_landmarks is None
        ):
            return frame

        drawing_utils = mp.solutions.drawing_utils

        drawing_styles = (
            mp.solutions.drawing_styles
        )

        for face_landmarks in results.multi_face_landmarks:

            drawing_utils.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=(
                    drawing_styles.get_default_face_mesh_tesselation_style()
                )
            )

        return frame

    # ===
    # Stage 4.8
    # Get face geometry
    # ===

    def get_face_geometry(self, results, frame):
        """
        Calculate face geometry.

        Args:
            results: MediaPipe detection results.
            frame: OpenCV frame.

        Returns:
            dict | None
        """

        points = self.get_landmark_points(
            results,
            frame
        )

        if not points:
            return None

        xs = [point[0] for point in points]
        ys = [point[1] for point in points]

        min_x = min(xs)
        max_x = max(xs)

        min_y = min(ys)
        max_y = max(ys)

        width = max_x - min_x
        height = max_y - min_y

        center_x = min_x + width // 2
        center_y = min_y + height // 2

        return {

            "center": (
                center_x,
                center_y
            ),

            "width": width,

            "height": height,

            "left": min_x,

            "right": max_x,

            "top": min_y,

            "bottom": max_y
        }

    # ===
    # Stage 4.9
    # Check face detection
    # ===

    def has_face(self, results):
        """
        Check whether a face is detected.
        """

        return (
            results is not None
            and
            results.multi_face_landmarks is not None
        )
