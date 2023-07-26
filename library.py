import cv2 as cv
import numpy as np

def read_image(image_path):
    """Load an image from the given path."""
    img = cv.imread(image_path)
    cv.imshow('Picture', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    

# def display_image(image, window_name='Image'):
#     """Display an image in a window."""
#     # cv.imshow(window_name, image)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()

def read_video(video_path):
    capture = cv.VideoCapture(video_path)
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', frame)
        if cv.waitKey(20)&0xFF==ord('d'):
            break
    capture.release()
    cv.destroyAllWindows

def rescale_image(image_path, scale):
    frame = cv.imread(image_path)
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    resized_image = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    cv.imshow('Resized Image', resized_image)
    cv.waitKey(0)

# def rescale_video(video_path, scale):
#     capture = cv.VideoCapture(video_path)
#     while True:
#         frame = capture.read()
#         width = int(frame.shape[1]*scale)
#         height = int(frame.shape[0]*scale)
#         dimensions = (width, height)
#         resized_videoframe = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#         isTrue, frame = resized_videoframe.read()
#         cv.imshow('Video', frame)
#         if cv.waitKey(20)&0xFF==ord('d'):
#             break
#     resized_videoframe.release()
#     cv.destroyAllWindows()

def rescale_video(video_path, scale):
    cap = cv.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            # If there are no more frames to read, break out of the loop
            break
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        resized_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
        cv.imshow('Video', resized_frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    cap.release()
    cv.destroyAllWindows()

blank = np.zeros((500,500,3), dtype='uint8')
def paint_image(color):
    # blank = np.zeros((500,500,3), dtype='uint8')
    blank[200:300,300:400] = color
    cv.imshow ('Color Filled', blank)
    cv.waitKey(0)

def draw_rectangle(color, outline):
    # blank = np.zeros((500,500,3), dtype='uint8')
    cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), color, thickness=outline)
    cv.imshow('Rectangle', blank)
    cv.waitKey(0)

def draw_circle(color, outline, radius):
    # blank = np.zeros((500,500,3), dtype='uint8')
    cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius, color, thickness=outline)
    cv.imshow('Circle', blank)
    cv.waitKey(0)

def draw_line(color, outline):
    # blank = np.zeros((500,500,3), dtype='uint8')
    cv.line(blank, (0,0), (300,400), color, outline)
    cv.imshow('Line', blank)
    cv.waitKey(0)

def write_text(text, color, outline):
    # blank = np.zeros((500,500,3), dtype='uint8')
    cv.putText(blank, text, (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, color, outline)
    cv.imshow('Text', blank)
    cv.waitKey(0)



