import cv2


def video_to_image():
    """
    Extracts each individual frame from a video file and saves as a .jpg to a specified directory.
    Output is a list of the image names.
    """
    vidcap = cv2.VideoCapture('sample.mp4')

    # frame
    currentframe = 0
    image_name_list = []

    while True:

        # reading from frame
        ret, frame = vidcap.read()

        if ret:
            # if video is still left continue creating images
            name = '../results/image-frame/frame' + str(currentframe) + '.jpg'

            # writing the extracted images
            cv2.imwrite(name, frame)

            image_name_list.append(name)

            # increasing counter so that it will show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    vidcap.release()
    cv2.destroyAllWindows()

    return image_name_list


video_to_image()
