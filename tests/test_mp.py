import mediapipe as mp

print("MediaPipe:", mp.__version__)

face_mesh = mp.solutions.face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1
)

print("OK")
face_mesh.close()
